
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

    def invokeCommand(self, controller):
        command = list(filter(lambda person: controller.Input in person['aliases'], list(self.Commands + self.SystemCommands)))
        commandName = command[0]['name']
        
        if len(command) < 1:
            print('ошибка!')
            controller.getHelp()
        elif commandName == 'cancel':
            controller.backState()
        elif commandName in ('motiv', 'bt'):
            print(commandName + ' пока не работает!')
        else:
            controller.Provider = commandName
            controller.backState()