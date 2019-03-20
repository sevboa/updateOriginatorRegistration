import csv
import re
import sys

from Originator import originator

sys.path.append('./class/originatorImporter')

class originatorMts(originator):
    rejectMessageMts = dict()
    
    def __init__(self, stringObject, rejectMessageMts=None):
        self.ProviderId = 11
        self.Originator = stringObject[0].value
        self.OriginatorChange = self.Originator
        self.ContractorInn = re.sub(r'[^\d]+', '', str(stringObject[2].value))
        self.ContractorLegalEntity = stringObject[1].value
        self.OperatorGroupId = 3
        self.ServiceTypeId = 4
        
        if rejectMessageMts is not None:
            self.StatusId, self.IsIncorrectInn = rejectMessageMts.get(str(stringObject[3].value)).split(';')
        else:
            self.StatusId = 3
            self.IsIncorrectInn = 0
        
        if self.IsIncorrectInn == 0:
            self.IsIncorrectInn = self.checkInn(self.ContractorInn)
