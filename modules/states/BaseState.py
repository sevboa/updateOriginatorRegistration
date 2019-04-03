
class baseState:
    FirstRun = bool()
    Commands = list()
    SystemCommands = list()
    Message = str()
    Controller = object()

    def __init__(self, controller):
        self.FirstRun = True
        self.Commands.clear()
        self.SystemCommands.clear()
        self.addSystemCommand('q', 'quit')
        self.Controller = controller

    def addCommand(self, shortName, fullName, option=None):
        
        
        self.Commands.append(
            dict(
                name = fullName,
                aliases = [shortName.lower(), fullName],
                option = option
            )
            
        )

    def addSystemCommand(self, shortName, fullName):
        self.SystemCommands.insert(
            0,
            dict(
                name = fullName,
                aliases = [shortName, fullName]
            )
        )

    def loadData(self, controller):
        ''
    def getText(self, controller):
        if self.FirstRun == True:
            for command in self.Commands:
                print(' [' + command['aliases'][0] + '] ' + command['aliases'][1], end='')
                if command.get('option') != None:
                    print(' | ', end='')
                    if type(command['option']) == type(str()):
                        if command['option'] == '':
                            print('не выбрано')
                        else:
                            print('\'' + str(command['option']) + '\'')
                    elif type(command['option']) == type(dict()):
                        print('{' + str(list(command['option'].keys())) + '}')
                    elif type(command['option']) == type(list()):
                        print('[' + str(len(command['option'])) + ']')
                    elif type(command['option']) == type(int()):
                        print(str(command['option']))
                    else:
                        print('неизвестный тип!')
                    
                else:
                    print('')
            self.FirstRun = False

        print('\n' + self.Message)

    def getHelp(self):
        for command in self.Commands:
            print(' [' + command['aliases'][0] + '] ' + command['aliases'][1])
        print('')
        for command in self.SystemCommands:
            print(' [' + command['aliases'][0] + '] ' + command['aliases'][1])

    def reset(self):
        self.__init__(self.Controller)

    