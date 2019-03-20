#import sys

from Originator import originator

class originatorTele2(originator):
    def __init__(self, string):
        if string[5] != '':
            self.ProviderId = 31
            self.Originator = string[5]
            self.OriginatorChange = string[5]
            self.ContractorInn = string[2]
            self.ContractorLegalEntity = string[1]
            self.OperatorGroupId = 4
            self.ServiceTypeId = 5
            if string[4] == 'active':
                self.StatusId = 3
            self.IsIncorrectInn = self.checkInn(self.ContractorInn)