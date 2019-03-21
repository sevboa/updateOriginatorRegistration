import os


class selectFileState:
    
    Files = list()

    def __init__(self):
        self.Files = os.listdir('./originators')
        self.Files.remove('.gitkeep')

    def getText(self, controller):
        if controller.FileName == '':
            print('Укажите имя файла:')
        else:
            print('Укажите имя файла(' + controller.FileName + '):')

    def getHelp(self):
        i = 1
        for fileName in self.Files:
            print('[' + str(i) + ']' + fileName)
            i = i + 1
        print('\n[c]cancel')

    def invokeCommand(self, controller):
        try:
            if int(controller.Input) <= len(self.Files):
                controller.FileName = self.Files[int(controller.Input) - 1]
                controller.backState()
        except ValueError:
            if self.Files.count(controller.Input) > 0:
                controller.FileName = controller.Input
                controller.backState()
            elif controller.Input in ('c', 'cancel'):
                controller.backState()
            else:
                print('ошибка!')
                controller.getHelp()