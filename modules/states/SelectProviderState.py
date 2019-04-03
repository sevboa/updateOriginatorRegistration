
from modules.states.BaseState import baseState

class selectProviderState(baseState):
    
    def __init__(self, controller):
        super().__init__(controller)
        self.addCommand('b',    'beeline')
        self.addCommand('m',    'mts')
        self.addCommand('t',    'tele2')
        self.addCommand('s',   'smsc')
        self.addCommand('mt',   'motiv', 'не работает!')
        self.addCommand('bt',   'bt', 'не работает!')
        self.addSystemCommand('c',   'cancel')
        
        self.Message = 'Укажите провайдера:'

    def invokeCommand(self):
        command = self.Controller.Command
        commandName = command['name']
        
        if commandName == 'cancel':
            self.Controller.backState()
        elif commandName in ('motiv', 'bt'):
            print(commandName + ' пока не работает!')
        else:
            self.Controller.Provider = commandName
            self.Controller.backState()