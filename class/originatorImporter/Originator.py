class originator:
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
    ServiceTypes = dict({
        '5': 'Платная регистрация',
        '4': 'Бесплатная регистрация'
    })
    OperatorsGroups = dict ({
        '2': 'Билайн',
        '1': 'Мегафон',
        '3': 'МТС',
        '4': 'Теле2',
        '15':'Yota'
    })
    Statuses = dict({
        '3': 'Зарегистрированно',
        '4': 'Отклонено',
        '7': 'Недостаточно документов',
        '2': 'отправлено на регистрацию'
    })
    Providers = dict({
        '10': 'Beeline',
        '11': 'MTS',
        '16': 'SMSC',
        '31': 'Tele2',
        '47': 'BT'
    })
    StatusesPriority = dict({
        '3': 7,
        '4': 1,
        '7': 4,
        '2': 5
    })

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