import os
from states.BaseState import baseState

class selectFileState(baseState):
    Directory = str()
    Files = list()

    def loadData(self, controller):
        self.Directory = './originators'
        self.Files = os.listdir(self.Directory)
        self.Files.remove('.gitkeep')
        
        self.addCommand(        'd',    'directory',    self.Directory)
        
        for fileNameNum in range(len(self.Files)):
            self.addCommand(    str(fileNameNum + 1), self.Files[fileNameNum])
        
        self.addSystemCommand(  'c',    'cancel')
        
        self.Message = 'Выберите файл:'

    def invokeCommand(self, controller):
        command = list(filter(lambda person: controller.Input in person['aliases'], list(self.Commands + self.SystemCommands)))
        commandName = command[0]['name']
        
        if len(command) < 1:
            print('ошибка!')
            controller.getHelp()
        elif commandName == 'directory':
            print(commandName + ' пока не работает!')
        elif commandName == 'cancel':
            controller.backState()
        else:
            controller.FileName = commandName
            controller.backState()