import csv
import re

from openpyxl import load_workbook

class importer:
    Originators = set()
    GlobalOriginators = set()
    OriginatorsString = set()
    
    def __init__(self, fileName):
        self.Originators.clear()

        extension = fileName.split('.')[-1]
        providerCode = fileName.split('_')[0]
        
        self.loadGlobalOriginator()
        
        print('import ' + fileName + ' ...')

        self.load(extension, providerCode, fileName)

    def load(self, extension, providerCode, fileName):
        
        limit = 100000000
        offset = 1

        if extension == 'csv' and providerCode in ('Beeline', 'SMSC'):
            with open('./originators/' + fileName, 'r', encoding='cp1251') as fileCsv:
                i = int()
                for string in csv.DictReader(fileCsv, delimiter=';'):
                    i+=1
                    if i>= offset: 
                        self.input(string)
                    if i > limit: break
        
        elif extension == 'csv' and providerCode in ('Tele2'):
            with open('./originators/' + fileName, 'r', encoding='cp1251') as fileCsv:
                i = int()
                for string in csv.reader(fileCsv, delimiter=';'):
                    i+=1
                    if i>= offset: 
                        self.input(string)
                    if i > limit: break
        
        elif extension == 'xlsx' and providerCode in ('BT'):
            wb = load_workbook(filename = './originators/' + fileName)
            for sheetName in wb.sheetnames[:1]:
                sheet = wb[sheetName]
                i = int()
                while True:
                    i+=1
                    if sheet['A' + str(i)].value == None:
                        break
                    try:
                        if sheet['A' + str(i)].value == None:
                            break
                        for stringObject in sheet['A' + str(i):'D' + str(i)]:
                            if i>= offset: 
                                self.input(stringObject)
                    except AttributeError:
                        break
                    if i > limit:
                        break

        elif extension == 'xlsx' and providerCode in ('Motiv'):
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
        
        print('import ' + fileName + ' complete')
    
    def input(self, string, rejected=False):
        ''
    
    def loadGlobalOriginator(self):
        filePath = './input/' + 'globalOriginators.csv'
        with open(filePath, 'r', encoding='cp1251') as fileCsv:
            for string in csv.DictReader(fileCsv, delimiter=';'):
                self.GlobalOriginators.update({string['originator'] + ';' + string['operator_group_id']})

    def outerOriginatorsAppend(self, originator):
        if (self.GlobalOriginators.isdisjoint({originator.Originator + ';' + str(originator.OperatorGroupId)}) and 
         originator.Originator != ''):
            #self.OriginatorsString.add(originator.Originator + ';' + str(originator.OperatorGroupId))
            self.Originators.add(originator)
