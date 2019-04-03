
from modules.ConfigParserJson import configParserJson

class stateController():
    Active = True
    _context = object()
    _previousContext = list()
    Input = str()
    Command = dict()

    Provider = str()
    FileName = str()
    
    Config = configParserJson()
    ConfigPart = configParserJson()

    def input(self):
        self.Input = input('> ')

    def getText(self):
        self._context.getText(self)
    
    def getHelp(self):
        print(' Доступные комманды:')
        self._context.getHelp()

    def setState(self, state):
        if self.Input not in ('c', 'cancel'):
            self._previousContext.append(self._context)
        self._context = state

    def invokeCommand(self):
        if self.Input == '':
            print('пустой ввод')
            self.getHelp()
        elif self.Input in ('?', 'help'):
            self.getHelp()
        elif self.Input in ('q', 'quit'):
            print('Выходим')
            self.Active = False
        else:
            command = list(
                filter(
                    lambda person: self.Input in person['aliases'], 
                    list(
                        self._context.Commands + self._context.SystemCommands
                    )
                )
            )
            
            if len(command) < 1:
                print('ошибка!')
                self.getHelp()
            else:    
                self.Command = command[0]
                self._context.invokeCommand()
    
    def backState(self):
        self._previousContext[-1].reset()
        self.setState(self._previousContext.pop(-1))