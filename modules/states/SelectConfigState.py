
from modules.states.BaseState import baseState

class selectConfigState(baseState):
    
    def loadData(self, controller):
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