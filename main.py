import sys
import re

sys.path.append('./class')
from Commons import csvUnload, sortingByFieldNames

sys.path.append('./originatorImporter')
from OriginatorImporter import originatorImporter

sys.path.append('./class/originatorImporter')
from ImporterBeeline import importerBeeline
from ImporterMts import importerMts
from ImporterSmsc import importerSmsc
from ImporterTele2 import importerTele2

## Начало программы
Originators = originatorImporter()

### от сих ==>

#Originators.originatorsImport(importerBeeline('Beeline_21.12.2018.csv'))
Originators.originatorsImport(importerSmsc('SMSC_18.03.2019.csv'))
#Originators.originatorsImport(importerTele2('Tele2_21.12.2018.csv'))
#Originators.originatorsImport(importerMts('MTS_12.02.2019.xlsx'))
#Originators.originatorsImport(importerMts('MTS_error_21.12.2018.xlsx'))

### <== до сих переместить в класс OriginatorImporter и добавить автоматический определитель свежего файла


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
