import re
import sys
import csv

from openpyxl import load_workbook

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorMts import originatorMts

class importerMts(importer):
    
    RejectMessageMts = dict()
    
    def load(self, extension, providerCode, fileName):
        if extension == 'xlsx' and providerCode in ('MTS'):
            filePath = self.loadRejectMessageMts()
            
            with open(filePath, 'a', encoding='cp1251', newline='') as fileCsv:
                writeCsv = csv.writer(fileCsv, delimiter=';')

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
                                if re.sub(r'[^\d]+', '', str(stringObject[2].value)) != '':
                                    if 'MTS_error_' in fileName:
                                        stateMessage = str(stringObject[3].value)
                                        statusAndIsIncorrectInn = self.RejectMessageMts.get(stateMessage)
                                        if statusAndIsIncorrectInn == None:
                                            print(str(stringObject[3].value))
                                            print('Неожиданный статус!')
                                            writeCsv.writerow([stringObject[3].value, '', ''])
                                            self.RejectMessageMts.update({stringObject[3].value : '0' + ';' + '0'})
                                        elif statusAndIsIncorrectInn != '0;0':
                                            self.input(stringObject, True)
                                    else:
                                        self.input(stringObject)
                        except AttributeError:
                            break
        else:
            print('Неподдерживаемое расширение входящего файла!')
            quit()
    
    def input(self, stringObject, rejected=False):
        if rejected == True:
            originator = originatorMts(stringObject, self.RejectMessageMts)
        else:
            originator = originatorMts(stringObject)
        if self.GlobalOriginators.isdisjoint({originator.Originator + ';' + str(originator.ProviderId)}):
            self.Originators.add(originator)

    def loadRejectMessageMts(self):
        filePath = './input/' + 'rejectMessageMts.csv'
        with open(filePath, 'r', encoding='cp1251') as fileCsv:
            for string in csv.DictReader(fileCsv, delimiter=';'):
                if string['status_id'] > '0':
                    self.RejectMessageMts.update({string['message'] : string['status_id'] + ';' + string['is_incorrect_inn']})
        return filePath
        

