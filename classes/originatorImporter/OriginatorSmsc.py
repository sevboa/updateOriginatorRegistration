import re
import sys
from html.parser import HTMLParser

from Originator import originator

sys.path.append('./class/originatorImporter')

class originatorSmsc(originator):
    
    def __init__(self, string):
        #if string['Статус'] == 'Допущено' and string['Имя'] != '' and string['Оператор'] != '':
        #if string['Имя'] == 'Alta-Soft':
            self.ProviderId = int(16)
            self.Originator = str(string['Имя'])
            self.OriginatorChange = str(string['originator_change'])
            self.ContractorLegalEntity, self.ContractorInn, self.IsIncorrectInn = self.getLegalEntityInn(string['Комментарий'])
            self.OperatorGroupId = int(string['operator_group_id'])
            self.ServiceTypeId = int(string['service_type_id'])
            self.StatusId = int(string['status_id'])

    def getLegalEntityInn(self, legalEntity):
        HtmlParser = HTMLParser()
        allInnUnique = set(re.findall(r'(?<=[^\d])\d{10,12}(?=[^\d])*', legalEntity))
        allInn = list(allInnUnique)
        for tempInn in allInn:
            legalEntity = legalEntity.replace(tempInn, '')
        legalEntity = re.sub(r'\s+', ' ', legalEntity)
        legalEntity = re.sub(r'^\s|\s$', '', legalEntity)
        legalEntity = re.sub(r'"+', '"', legalEntity)
        
        if len(allInn) > 0:
            inn = allInn.pop()

        if len(allInnUnique) < 1:
            contractorInn = '123'
            isIncorrectInn = True
        else:
            contractorInn = inn
            if len(allInnUnique) > 1:
                isIncorrectInn = True
            else:
                isIncorrectInn = self.checkInn(inn)
        return str(HtmlParser.unescape(legalEntity)), str(contractorInn), bool(isIncorrectInn)
