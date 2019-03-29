
from modules.states.BaseState import baseState

class changeConfigState(baseState):
    
    ConfigPart = dict()
    
    def __init__(self, controller, configPart):
        super().__init__(controller)
        self.ConfigPart = configPart
        params = self.ConfigPart.keys()
        for param in params:
            print(param)
            if param[0] != '_':
                self.addCommand(param[0], param, self.ConfigPart[param])
        self.addSystemCommand('c',   'cancel')
        
        self.Message = 'Выберите параметр:'

    def invokeCommand(self, controller):
        command = list(
        	filter(
        		lambda person: controller.Input in person['aliases'], 
        		list(
        			self.Commands + self.SystemCommands
        		)
        	)
        )
        
        if len(command) < 1:
            print('ошибка!')
            controller.getHelp()
        else:
            commandName = command[0]['name'].lower()
            if commandName == 'cancel':
                controller.backState()
            else:
                print('выбран раздел ' + commandName)