
from modules.states.BaseState import baseState

class changeConfigState(baseState):
    
    ConfigPart = dict()
    
    def __init__(self, controller):
        super().__init__(controller)
        print(type(self.Controller.Config.Part))
        if type(self.Controller.Config.Part) == type(dict()):
            params = list(self.Controller.Config.Part.keys())
            print(params)
            for param in params:
                #print(param)
                if param[0] != '_':
                    self.addCommand(param[0], param, self.Controller.Config.Part[param])
        elif type(self.Controller.Config.Part) == type(list()):
            if len(self.Controller.Config.Part) > 20:
                params = self.Controller.Config.Part[:20]
            else:
                params = self.Controller.Config.Part
            for paramNum in range(len(params)):
                self.addCommand(str(paramNum + 1), str(paramNum), self.Controller.Config.Part[paramNum])
        
        
        self.addSystemCommand('c',   'cancel')
        
        self.Message = 'Выберите параметр:'

    def invokeCommand(self):
        command = self.Controller.Command
        commandName = command['name']

        if commandName == 'cancel':
            self.Controller.Config.setParentPart()
            self.Controller.backState()
        elif type(command['option']) == type(str()):
            #self.Controller.setState(changeConfigState(self.Controller, self.Controller.Config.__dict__.get(commandName)))
            print('\nВведите значение ' + commandName)
            string_input = input('> ')
            self.Controller.Config.setPartParam(commandName, string_input)
            command['option'] = string_input
            self.FirstRun = True
        elif type(command['option']) == type(int()):
            #self.Controller.setState(changeConfigState(self.Controller, self.Controller.Config.__dict__.get(commandName)))
            while True:
                print('\nВведите значение ' + commandName)
                string_input = input('> ')
                if string_input.isdigit():
                    self.Controller.Config.setPartParam(commandName, int(string_input))
                    command['option'] = int(string_input)
                    self.FirstRun = True
                    break
                else:
                    print('Введите число!')
        elif type(command['option']) == type(dict()):
            #self.Controller.setState(changeConfigState(self.Controller, self.Controller.Config.__dict__.get(commandName)))
            if type(self.Controller.Config.Part) == type(dict()):
                self.Controller.Config.setChildPart(commandName)
            elif type(self.Controller.Config.Part) == type(list()):
                self.Controller.ConfigPart = self.Controller.ConfigPart[int(commandName)]
            self.reset()
        elif type(command['option']) == type(list()):
            #self.Controller.setState(changeConfigState(self.Controller, self.Controller.Config.__dict__.get(commandName)))
            self.Controller.Config.setChildPart(commandName)
            self.reset()

        else:
            print('выбран раздел ' + commandName)
