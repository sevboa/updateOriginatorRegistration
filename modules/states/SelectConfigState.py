
from modules.states.BaseState import baseState
from modules.states.ChangeConfigState import changeConfigState

class selectConfigState(baseState):
    
    def __init__(self, controller):
        super().__init__(controller)
        params = dir(controller.Config)
        for param in params:
            if param[0] != '_':
                self.addCommand(param[0], param)
        self.addSystemCommand('c',   'cancel')
        
        self.Message = 'Выберите раздел:'

    def invokeCommand(self, controller):
        command = list(filter(lambda person: controller.Input in person['aliases'], list(self.Commands + self.SystemCommands)))
        commandName = command[0]['name']
        
        if len(command) < 1:
            print('ошибка!')
            controller.getHelp()
        elif commandName == 'cancel':
            controller.backState()
        else:
            print('выбран раздел ' + commandName)
            controller.setState(changeConfigState(controller, controller.Config.__dict__.get(commandName)))