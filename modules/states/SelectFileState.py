import os
from modules.states.BaseState import baseState

class selectFileState(baseState):
    Directory = str()
    Files = list()

    def __init__(self, controller):
        super().__init__(controller)
        self.Directory = './originators'
        self.Files = os.listdir(self.Directory)
        self.Files.remove('.gitkeep')
        
        self.addCommand(        'd',    'directory',    self.Directory)
        
        for fileNameNum in range(len(self.Files)):
            self.addCommand(    str(fileNameNum + 1), self.Files[fileNameNum])
        
        self.addSystemCommand(  'c',    'cancel')
        
        self.Message = 'Выберите файл:'

    def invokeCommand(self):
        command = self.Controller.Command
        commandName = command['name']
        
        if commandName == 'directory':
            print(commandName + ' пока не работает!')
        elif commandName == 'cancel':
            self.Controller.backState()
        else:
            self.Controller.FileName = commandName
            self.Controller.backState()