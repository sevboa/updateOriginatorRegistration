
from modules.OriginatorImporter import originatorImporter

from modules.states.BaseState import baseState
from modules.states.SelectProviderState import selectProviderState
from modules.states.SelectFileState import selectFileState
from modules.states.SelectConfigState import selectConfigState

class importState(baseState):
    Provider = str()
    FileName = str()
    
    def __init__(self, controller):
        super().__init__(controller)
        self.Provider = self.Controller.Provider
        self.FileName = self.Controller.FileName
        
        self.addCommand('p',    'provider',    self.Provider)
        self.addCommand('f',    'file_name',   self.FileName)
        self.addCommand('s',    'setings')
        self.addCommand('ok',   'start_import')
        
        self.Message = 'Выберите пункт меню:'

    def invokeCommand(self):
        command = self.Controller.Command
        commandName = command['name']
        
        if commandName == 'provider':
            self.Controller.setState(selectProviderState(self.Controller))
        elif commandName == 'file_name':
            self.Controller.setState(selectFileState(self.Controller))
        elif commandName == 'setings':
            self.Controller.setState(selectConfigState(self.Controller))
        elif commandName == 'start_import':
            if self.Controller.Provider == '' or self.Controller.FileName == '':
                print('Недостаточно данных для импорта!')
            else:
                originatorImporter(self.Controller.Provider, self.Controller.FileName)