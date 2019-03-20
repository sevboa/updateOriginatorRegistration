
from modules.originatorImport.Originator import originator

class originatorBeeline(originator):
    
    def create(self, string, onlySuccess):
        self.ProviderId = 10
        self.Originator = string['Имя отправителя']
        self.OriginatorChange = self.Originator
        self.ContractorInn = string['ИНН аккаунта']
        self.ContractorLegalEntity = string['Наименование аккаунта']
        self.OperatorGroupId = 2
        if string['Категория трафика'] == 'information':
            self.ServiceTypeId = 5
        if string['Статус аккаунта'] == 'active':
            self.StatusId = 3
        self.IsIncorrectInn = self.checkInn(self.ContractorInn)
        self.AccountId = str(string['account_id'])