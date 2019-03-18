import csv
import re
import sys

from openpyxl import load_workbook

sys.path.append('./class')
from ConfigParserJson import configParserJson

class importer:
    Config = configParserJson().originatorImporter
    Originators = set()
    GlobalOriginators = list()
    GlobalOriginatorsCache = set()
    OriginatorsString = set()
    
    def __init__(self, fileName):
        self.loadConfig()
        
        self.Originators.clear()

        extension = fileName.split('.')[-1]
        providerCode = fileName.split('_')[0]
        
        self.loadGlobalOriginators()

        self.createGlobalOriginatorsCache()
        
        print('import ' + fileName + ' ...')

        self.load(extension, providerCode, fileName)

        print('import ' + fileName + ' complete')

    def loadConfig(self):
        ''
    
    def load(self, extension, providerCode, fileName):
        
        if extension == 'xlsx' and providerCode in ('Motiv'):
            '''
            def exportMotiv(fileName):
                print('export originator of provider Motiv')
                originators = set()
                wb = openpyxl.load_workbook(filename = './originators/' + fileName)
                sheet = wb['Лист1']
                i = 4
                while True:
                    if sheet['C' + str(i)].value == None:
                        break
                    originators.add(str(sheet['C' + str(i)].value))
                    i += 1
                counter = Counter(len(originators), 0.2)
                outerOriginators = list()
                for originator in originators:
                    counter.step('export...')
                    outerOriginators.append({
                        'originator': originator,
                        'operator_group_id': '13',
                        'provider': 'Motiv',
                        'originator_change': ''
                    })
                counter.lastTell('exported')
                outerOriginators = sortingByFieldNames(outerOriginators, ['originator'])
                return outerOriginators
            '''

        else:
            print('Неподдерживаемое расширение входящего файла!')
            quit()
    
    def input(self, string, rejected=False):
        ''
    
    def loadGlobalOriginators(self):
        for globalOriginator in self.Config['all']['globalOriginators']:
            self.GlobalOriginators.append(globalOriginator)
            if globalOriginator['operator_group_id'] == 1:
                globalOriginatorYota = globalOriginator.copy()
                globalOriginatorYota['operator_group_id'] = 15
                self.GlobalOriginators.append(globalOriginatorYota)
    
    def createGlobalOriginatorsCache(self):
        for globalOriginator in self.GlobalOriginators:
            self.GlobalOriginatorsCache.update({globalOriginator['originator'] + ';' + str(globalOriginator['operator_group_id'])})
    
    def outerOriginatorsAppend(self, originator):
        if (self.GlobalOriginatorsCache.isdisjoint({originator.Originator + ';' + str(originator.OperatorGroupId)}) and 
         originator.Originator != ''):
            self.Originators.add(originator)
