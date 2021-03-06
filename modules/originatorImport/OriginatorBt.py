
from modules.originatorImport.Originator import originator

class originatorBt(originator):
    mtsStatuses = dict({
        'ИНН ок, документов нет': '3;0',
        'на 20.12.2018': '3;0',
        'ок': '3;0',
        'ИНН ок, докум. Ок': '3;0',
        'преждоставить документ': '7;0',
        'необходимо письмо о нераспространении рекламы на алкоголь': '7;0',
        'иностранная организация, необходимо предоставить документы': '7;0',
        'аббревиатура, необходимо предоставить документы': '7;0',
        'зарегистрирован товарный знак, необходимо изменить имя и предоставить документы': '7;0',
        'существует домен, необходимо предоставить документы': '7;0',
        'существует домен, необходимо предоставить документы или изменить имя': '7;0',
        'зарегистрированный ТЗ, предоставить документ или изменить Имя': '7;0',
        'нет совпадения': '7;0',
        'предоставить документ': '7;0',
        'зарегистрированный ТЗ, изменить или предоставить документ': '7;0',
        'Предоставить документы': '7;0',
        'Гарантийное письмо на другого агента': '7;0',
        'Документы на другое юр.лицо': '7;0',
        'документы не подстверждают принажлежность подписи': '7;0',
        'В письме указано неизвестное юрлицо': '7;0',
        'Предоставить документы. Гарантийные письма допустимы только от ИП': '7;0',
        'Документы на другого человека': '7;0',
        'Домен принадлежит другому лицу': '7;0',
        'необходимы документы': '7;0',
        'Докутенты на другую организацию. А также необходимо письмо о нераспространении рекламы о курении': '7;0',
        'Необходимы подтверждающие документы, письмо от организации не принимается': '7;0',
        'Необходимы другие подтверждающие документы': '7;0',
        'Общее имя, рекомендуется изменить в соответствии с товарным знаком': '7;0',
        'Необходимы подтвердающие документы': '7;0',
        'Документ не подтверждает право использование подписи': '7;0',
        'Документы на другое лицо': '7;0',
        'Письмо для другого агента': '7;0',
        'Предоставить документы или изменить подпись по совпадению.': '7;0',
        'Другое юр.лицо в документах': '7;0',
        'Документы на тругое юр лицо': '7;0',
        'Срок действия документа истек': '7;0',
        'Предоставить подтверждающие документы и письмо о нераспространнии рекламы пива': '7;0',
        'Прикладываемые документы не соответствуют подписи': '7;0',
        'Документы на другое юр лицо': '7;0',
        'нкорректный ИНН': '4;1',
        'ИНН другого лица': '4;1',
        'инн другой компании': '4;1',
        'некорректный ИНН, агрегационное': '4;1',
        'инн другого ИП': '4;1',
        'ИНН пренадлежит ООО "Акация", слово Русалка не упоминается': '4;1',
        'инн компании, которая прекратила деятельность': '4;1',
        'некорректный ИНН или данные': '4;1',
        'некорректный ИНН': '4;1',
        'Непонятная подпись для получателя': '4;0',
        'имя общее': '4;0',
        'Общее имя': '4;0',
        'Ликвидировано': '4;0',
        'Подпись общая, рекомендуем изменить до полного совпадения': '4;0',
        'Деятельность прекращена': '4;0',
        'Предоставить подтверждающие документы': '4;0',
        'Общее имя, рекомендуем изменить на полное совпадение': '4;0',
        'Некорректные данные': '4;0',
        'Необходимо изменить на полное совпадение': '4;0',
        'Очень общее имя, необходимо дополнить подпись, например "ООО" или кодом региона': '4;0',
        'Подпись общая, необходимо изменить до полного совпадения': '4;0',
        'Подпись не отображает наименование организации и её деятельность': '4;0',
        'Письмо о нераспространении рекламы алкоголя': '4;0',
        'Подпись общая, необходимо изменить до полного совпадения или предоставить документы': '4;0',
        'необходимо предоставить документы': '4;0',
        'агрегационное имя': '4;0',
        'действие прекращено': '4;0',
        'агрегационное': '4;0',
        'компания называется по другому': '4;0',
        'совпадение с наименованием, есть сайт': '4;0',
        'совпадение с наименованием': '4;0',
        'физ лицо': '4;0',
        'агрегационное имя ': '4;0',
        'агрегационное имя + зарегистрирован товарный знак ': '4;0',
        'некорректно указано название организации': '4;0',
        'агрегационное имя, рекомендуем к имени добавить код региона': '4;0',
        'зарегистрированный домен, изменить Имя, добавить признак региона, города': '4;0',
        'агрегационное, изменить': '4;0',
        'зарегистрированный домен, добавить S': '4;0',
        'агрегационное, изменить согласно домену prvsmp': '4;0',
        'Имя собственное, добавить ТД': '4;0',
        'добавить ТД или регион, город': '4;0',
        'Подпись общая, необходимо изменить на полное совпадение': '4;0',
        'Общая подпись': '4;0',
        'Письмо о нераспространнии рекламы алкоголя': '4;0',
        'Общее имя, рекомендуется изменить в соответствии с доменом': '4;0',
        'Имя общее, рекомендуется изменить в соответствии с доменом': '4;0',
        'Недопустимый символ': '4;0',
        'Общее имя, предлагаем изменить в соответствии с товарным знаком': '4;0'
    })
    
    def create(self, stringObject, onlySuccess):
        self.ProviderId = 11
        self.Originator = stringObject[0].value
        self.OriginatorChange = self.Originator
        self.ContractorInn = str(stringObject[2].value)
        self.ContractorLegalEntity = stringObject[1].value
        self.OperatorGroupId = 3
        self.ServiceTypeId = 4
        stateMessage = str(stringObject[3].value)
        statusAndInn = self.mtsStatuses.get(stateMessage)
        if statusAndInn == None:
            print(str(stringObject[3].value))
            print('Неожиданный статус!')
            quit()
        self.StatusId, self.IsIncorrectInn = statusAndInn.split(';')
        if self.IsIncorrectInn == 0:
            self.IsIncorrectInn = self.checkInn(self.ContractorInn)