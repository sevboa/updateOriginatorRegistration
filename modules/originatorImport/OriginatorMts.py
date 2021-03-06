import csv
import re

from modules.originatorImport.Originator import originator

class originatorMts(originator):
    MtsStatuses = list()
    MtsStatusesCache = dict()

    def loadConfig(self):
        self.MtsStatuses.extend(self.originatorConfig['mts']['Statuses'])
        self.MtsStatusesCache.update(self.originatorConfig['mts']['StatusesCache'])

    def create(self, stringObject, onlySuccess):
        self.ProviderId = 11
        self.Originator = stringObject[0].value
        self.OriginatorChange = self.Originator
        self.ContractorInn = re.sub(r'[^\d]+', '', str(stringObject[2].value))
        self.ContractorLegalEntity = stringObject[1].value
        self.OperatorGroupId = 3
        self.ServiceTypeId = 4
        
        if onlySuccess == True:
            self.StatusId = 3
            self.IsIncorrectInn = 0
            
        else:
            stateMessage = str(stringObject[3].value)
            statusAndIsIncorrectInn = self.MtsStatusesCache.get(stateMessage)
            if statusAndIsIncorrectInn == None:
                print(str(stringObject[3].value))
                print('Неожиданный статус!')
                #writeCsv.writerow([stringObject[3].value, '', ''])
                self.MtsStatusesCache.update({stringObject[3].value : '0' + ';' + '0'})
            elif statusAndIsIncorrectInn != '0;0':
                ''
            else:
                status, isIncorrectInn = statusAndIsIncorrectInn.split(';')
                self.StatusId = int(status)
                self.IsIncorrectInn = bool(isIncorrectInn)
        
        if self.IsIncorrectInn == 0:
            self.IsIncorrectInn = self.checkInn(self.ContractorInn)
