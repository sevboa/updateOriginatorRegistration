
from modules.OriginatorImporter import originatorImporter

from modules.states.BaseState import baseState
from modules.states.SelectProviderState import selectProviderState
from modules.states.SelectFileState import selectFileState
from modules.states.SelectConfigState import selectConfigState

class importState(baseState):
    Provider = str()
    FileName = str()
    
    def loadData(self, controller):
        self.Provider = controller.Provider
        self.FileName = controller.FileName
        
        self.addCommand('p',    'provider',    self.Provider)
        self.addCommand('f',    'file_name',   self.FileName)
        self.addCommand('s',    'setings')
        self.addCommand('ok',   'start_import')
        
        self.Message = 'Выберите пункт меню:'

    def invokeCommand(self, controller):
        command = list(filter(lambda person: controller.Input in person['aliases'], list(self.Commands + self.SystemCommands)))
        commandName = command[0]['name']
        
        if len(command) < 1:
            print('ошибка!')
            controller.getHelp()
        elif commandName == 'provider':
            controller.setState(selectProviderState(controller))
        elif commandName == 'file_name':
            controller.setState(selectFileState(controller))
        elif commandName == 'setings':
            controller.setState(selectConfigState(controller))
        elif commandName == 'start_import':
            if controller.Provider == '' or controller.FileName == '':
                print('Недостаточно данных для импорта!')
            else:
                originatorImporter(controller.Provider, controller.FileName)