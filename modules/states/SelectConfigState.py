
from modules.states.BaseState import baseState
from modules.states.ChangeConfigState import changeConfigState

class selectConfigState(baseState):
    
    def __init__(self, controller):
        super().__init__(controller)
        params = dir(self.Controller.ConfigPart)
        for param in params:
            if param[0] != '_':
                self.addCommand(param[0], param)
        self.addSystemCommand('c',   'cancel')
        
        self.Message = 'Выберите раздел:'

    def invokeCommand(self):
        command = self.Controller.Command
        commandName = command['name']
        
        if commandName == 'cancel':
            self.Controller.backState()
        else:
            print('выбран раздел ' + commandName)
            if type(self.Controller.ConfigPart.__dict__.get(commandName)) == type(dict()):
                self.Controller.ConfigPart = self.Controller.ConfigPart.__dict__.get(commandName)
                self.Controller.setState(changeConfigState(self.Controller))