
class baseState:
    FirstRun = True
    Commands = list()
    SystemCommands = list()
    Message = str()

    def __init__(self, controller):
        self.Commands.clear()
        self.SystemCommands.clear()
        self.addSystemCommand('q', 'quit')
        self.loadData(controller)

    def addCommand(self, shortName, fullName, option=None):
        self.Commands.append(
            dict(
                name = fullName,
                aliases = [shortName, fullName],
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
                    if command['option'] == '':
                        print('не выбрано')
                    else:
                        print(command['option'])
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

    