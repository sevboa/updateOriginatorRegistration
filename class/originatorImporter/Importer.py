import csv
import re

from openpyxl import load_workbook

class importer:
    Originators = set()
    RejectMessageMts = dict()
    GlobalOriginators = set()
    OriginatorsString = set()
    rejectMessageMts2 = dict({
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
        'Общее имя, предлагаем изменить в соответствии с товарным знаком': '4;0',
        'ИнН ок, документов нет': '3;0',
        'Имя общее': '4;0',
        'Некорректный ИНН': '4;1',
        'деятельность прекращена': '4;0',
        'Необходимы документы': '7;0'
    })
    
    def __init__(self, fileName):
        self.load(fileName)

    def load(self, fileName):
        self.Originators.clear()

        extension = fileName.split('.')[-1]
        providerCode = fileName.split('_')[0]
        
        self.loadGlobalOriginator()
        
        print('import ' + fileName + ' ...')

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
        
        elif extension == 'xlsx' and providerCode in ('MTS'):
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
                                if i>= offset: 
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
                        if i > limit:
                            break

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
    
    def loadRejectMessageMts(self):
        filePath = './input/' + 'rejectMessageMts.csv'
        with open(filePath, 'r', encoding='cp1251') as fileCsv:
            for string in csv.DictReader(fileCsv, delimiter=';'):
                if string['status_id'] > '0':
                    self.RejectMessageMts.update({string['message'] : string['status_id'] + ';' + string['is_incorrect_inn']})
        return filePath
    
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
