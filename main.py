import sys
import re

from states.StateController import stateController
from states.ImportState import importState

print('    Татьяна 0.3')
print(' Добро пожаловать!')
print(' Данная программа предназначена для парсинга')
print(' файлов регистраций имен поставщиков.')
print(' P.S. для помощи введите \'h\'\n')

Controller = stateController(importState())

while Controller.Active:
    Controller.getText()
    Controller.input()
    Controller.invokeCommand()
    print('===================================')


exit()
####################################


from modules.Commons import csvUnload, sortingByFieldNames
from modules.ConfigParserJson import configParserJson
from modules.OriginatorImporter import originatorImporter

from modules.originatorImport.Importer import importer
from modules.originatorImport.ImporterBeeline import importerBeeline
from modules.originatorImport.ImporterMts import importerMts
from modules.originatorImport.ImporterSmsc import importerSmsc
from modules.originatorImport.ImporterTele2 import importerTele2

## Начало программы

### подгрузка конфигов
Config = configParserJson()

### подгрузка импортера
Originators = originatorImporter()

### от сих ==>

#Originators.importOriginators(importerBeeline('Beeline_21.12.2018.csv'))
#Originators.importOriginators(importerSmsc('SMSC_18.03.2019.csv'))
#Originators.importOriginators(importerTele2('Tele2_21.12.2018.csv'))
Originators.importOriginators(importerMts('MTS_20.12.2018.xlsx'))
#Originators.importOriginators(importerMts('MTS_error_21.12.2018.xlsx'))
#

### <== до сих переместить в класс originatorImport и добавить автоматический определитель свежего файла? или лучше MVC?


## Сохранение в файл

csvUnload(Originators.outputListDict(), 'OriginatorsSmscRegistrations.csv', [
    'provider',
    'operator_group_id', 
    'service_type_id', 
    'originator_change', 
    'originator', 
    'contractor_legal_entity', 
    'contractor_inn', 
    'is_incorrect_inn', 
    'status_id',
    'account_id'
])

'''
## Генерация запроса по операторам на разные файлы
for key in list(Originators.OriginatorsByOperatorsGropupId.keys()):
    queryList = Originators.sqlGenerate(Originators.OriginatorsByOperatorsGropupId.get(key), 20000)
    fileCount = int()
    for query in queryList:
        fileCount += 1
        f = open('./output/originators_smsc_' + key + '_' + str(fileCount) + '.sql', 'w', encoding='utf8')
        f.write(query)
'''

## Генерация запроса в один файл
queryString = Originators.sqlGenerate(Originators.Originators, 20000)
queryString = re.sub(r'\n+\s+', ' ', queryString)
queryString = re.sub(r'\s+\n+', ' ', queryString)
queryString = re.sub(r'\n+', ' ', queryString)
queryString = re.sub(r'\s', ' ', queryString)
f = open('./output/originators_smsc.sql', 'w', encoding='utf8')
f.write(queryString)

## Генерация запроса написания имен
querySpellingString = Originators.spellingOriginatorsSqlGenerate()
querySpellingString = re.sub(r'\n+\s+', ' ', querySpellingString)
querySpellingString = re.sub(r'\s+\n+', ' ', querySpellingString)
querySpellingString = re.sub(r'\n+', ' ', querySpellingString)
querySpellingString = re.sub(r'\s', ' ', querySpellingString)
f = open('./output/spelling_originators_smsc.sql', 'w', encoding='utf8')
f.write(querySpellingString)
