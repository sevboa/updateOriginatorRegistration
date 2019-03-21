import sys
import json
import csv
import os

class stateController:
    Active = True
    _context = object()
    Input = str()

    Provider = str()
    FileName = str()

    def __init__(self, state):
        self.setState(state)

    def input(self):
        self.Input = input('> ')

    def getText(self):
        self._context.getText(self)
    
    def getHelp(self):
        print('Доступные комманды:')
        self._context.getHelp()
        print('\n[q]quit')

    def setState(self, state):
        self._context = state

    def invokeCommand(self):
        if self.Input == '':
            print('пустой ввод')
            self.getHelp()
        if self.Input in ('h', 'help'):
            self.getHelp()
        elif self.Input in ('q', 'quit'):
            print('Выходим')
            self.Active = False
        else:
            self._context.invokeCommand(self)

class importState:
    def getText(self, controller):
        if controller.Provider != '':
                print('Поставщик: ' + controller.Provider)
        else:
            print('поставщик неуказан')
        if controller.FileName != '':
            print('Имя файла: ' + controller.FileName)
        else:
            print('файл неуказан')

    def getHelp(self):
        print('[p]provider')
        print('[f]file_name')
        print('[s]setting')
        print('[ok]start_import')

    def invokeCommand(self, controller):
        if   controller.Input in ('p','provider'):
            controller.setState(selectProviderState())
        elif controller.Input in ('f','file_name'):
            controller.setState(selectFileState())
        elif controller.Input in ('s', 'setting'):
            print('Вот настройки')
        elif controller.Input in ('ok','start_import'):
            if controller.Provider == '' or controller.FileName == '':
                print('Недостаточно данных для импорта!')
            else:
                print('Начало импорта...')
                #controller.setState(selectFileState())
        
        else:
            print('ошибка!')
            controller.getHelp()

class selectProviderState:
    
    def getText(self, controller):
        if controller.Provider == '':
            print('Укажите провайдера:')
        else:
            print('Укажите провайдера(' + controller.Provider + '):')

    def getHelp(self):
        print('[b]beeline')
        print('[m]mts')
        print('[t]tele2')
        print('[m]motiv (не работает)')
        print('[s]smsc')
        print('[bt]bt')
        print('\n[c]cancel')

    def invokeCommand(self, controller):
        if   controller.Input in ('b','beeline'):
            controller.Provider = 'beeline'
            controller.setState(importState())
        elif controller.Input in ('m','mts'):
            controller.Provider = 'mts'
            controller.setState(importState())
        elif controller.Input in ('t','tele2'):
            controller.Provider = 'tele2'
            controller.setState(importState())
        elif controller.Input in ('m','motiv'):
            print('motiv пока не работает!')
        elif controller.Input in ('s','smsc'):
            controller.Provider = 'smsc'
            controller.setState(importState())
        elif controller.Input in ('bt','bt'):
            controller.Provider = 'bt'
            controller.setState(importState())
        elif controller.Input in ('c', 'cancel'):
            controller.setState(importState())
        else:
            print('ошибка!')
            controller.getHelp()

class selectFileState:

    Files = list()

    def __init__(self):
        self.Files = os.listdir('./originators')
        self.Files.remove('.gitkeep')

    def getText(self, controller):
        if controller.FileName == '':
            print('Укажите имя файла:')
        else:
            print('Укажите имя файла(' + controller.FileName + '):')

    def getHelp(self):
        i = 1
        for fileName in self.Files:
            print('[' + str(i) + ']' + fileName)
            i = i + 1
        print('\n[c]cancel')

    def invokeCommand(self, controller):
        try:
            if int(controller.Input) <= len(self.Files):
                controller.FileName = self.Files[int(controller.Input) - 1]
                controller.setState(importState())
        except ValueError:
            if self.Files.count(controller.Input) > 0:
                controller.FileName = controller.Input
                controller.setState(importState())
            elif controller.Input in ('c', 'cancel'):
                controller.setState(importState())
            else:
                print('ошибка!')
                controller.getHelp()
        


print('    Татьяна 0.3')
print(' Добро пожаловать!')
print(' Данная программа предназначена для парсинга')
print(' файлов регистраций имен поставщиков.')
print(' P.S. для помощи введите \'h\'\n')

Controller = stateController(importState())

while Controller.Active:
    Controller.getText()
    Controller.input()
    Controller.invokeCommand()
    print('===================================')
    
    

exit()

class a:
    def __init__(
        self, 
        ident: int, 
        max_num: int, 
        name: str
    ):
        self._ident = ident
        self._max_num = max_num
        self._name = name
    
    def __getitem__(self, qwe):
        return self._ident + 1
    
    def __setitem__(self, qwe, ident):
        self._ident = ident
    
    def __call__(self):
        return self._ident, self._max_num, self._name
     
b = a(1,3,'ewr')

b['qwe'] = 5

print(b['qwe'])

exit()

RejectMessageMts = list()

filePath = './input/' + 'rejectMessageMts.csv'
with open(filePath, 'r', encoding='utf-8') as fileCsv:
    for string in csv.DictReader(fileCsv, delimiter=';'):
        if string['registration_status_id'] > '0':
            RejectMessageMts.append(string)

with open("statusesMts.json", "w", encoding="utf-8") as file:
    json.dump(RejectMessageMts, file,ensure_ascii=False,indent=4)