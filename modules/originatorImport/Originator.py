from modules.ConfigParserJson import configParserJson

class originator:
    # pylint: disable = no-member
    importerConfig = configParserJson().importer
    originatorConfig = configParserJson().originator
    ProviderId = int()
    Originator = str()
    OriginatorChange = str()
    ContractorLegalEntity = str()
    ContractorInn = int()
    IsIncorrectInn = bool()
    OperatorGroupId = int()
    ServiceTypeId = int()
    StatusId = int()
    AccountId = str()
    ServiceTypes = dict()
    OperatorsGroups = dict()
    Statuses = dict()
    Providers = dict()
    StatusesPriority = dict()

    def __init__(self, string, onlySuccess = False):
        self.ServiceTypes = self.originatorConfig['ServiceTypes']
        self.OperatorsGroups = self.originatorConfig['OperatorsGroups']
        self.Statuses = self.originatorConfig['Statuses']
        self.StatusesPriority = self.originatorConfig['StatusesPriority']
        self.Providers = self.originatorConfig['Providers']
        
        self.loadConfig()

        self.create(string, onlySuccess)

    def loadConfig(self):
        ''

    def checkInn(self, inn):
        if len(inn) not in (10, 12) or int(inn) == 0:
            return '1'

        def inn_csum(inn):
            k = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
            pairs = zip(k[11-len(inn):], [int(x) for x in inn])
            return str(sum([k * v for k, v in pairs]) % 11 % 10)

        if len(inn) == 10:
            if inn[-1] == inn_csum(inn[:-1]):
                result = '0'
            else:
                result = '1'
        else:
            if inn[-2:] == list(inn_csum(inn[:-2]) + inn_csum(inn[:-1])):
                result = '0'
            else:
                result = '1'
        return result

    def provider(self):
        return self.Providers.get(str(self.ProviderId))
    
    def serviceType(self):
        return self.ServiceTypes.get(str(self.ServiceTypeId))

    def operatorGroup(self):
        return self.OperatorsGroups.get(str(self.OperatorGroupId))

    def status(self):
        return self.Statuses.get(str(self.StatusId))

    def output(self):
        return dict(
            provider=self.provider(),
            #provider_id=str(self.ProviderId),
            originator=self.Originator,
            originator_change=self.OriginatorChange,
            contractor_inn=self.ContractorInn,
            contractor_legal_entity=self.ContractorLegalEntity,
            is_incorrect_inn=str(int(self.IsIncorrectInn)),
            operator_group_id=self.OperatorGroupId,
            service_type_id=self.ServiceTypeId,
            status_id=self.StatusId,
            account_id=self.AccountId,
            #service_type=self.serviceType(),
            #operator_group=self.operatorGroup(),
            #status=self.status()
        )

    def getStatusPriority(self):
        return self.StatusesPriority.get(str(self.StatusId))