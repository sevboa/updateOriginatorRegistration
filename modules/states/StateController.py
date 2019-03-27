
from modules.ConfigParserJson import configParserJson

class stateController():
    Active = True
    _context = object()
    _previousContext = object()
    Input = str()

    Provider = str()
    FileName = str()
    
    Config = configParserJson()

    def input(self):
        self.Input = input('> ')

    def getText(self):
        self._context.getText(self)
    
    def getHelp(self):
        print(' Доступные комманды:')
        self._context.getHelp()

    def setState(self, state):
        self._previousContext = self._context
        self._context = state

    def invokeCommand(self):
        if self.Input == '':
            print('пустой ввод')
            self.getHelp()
        elif self.Input in ('h', 'help'):
            self.getHelp()
        elif self.Input in ('q', 'quit'):
            print('Выходим')
            self.Active = False
        else:
            self._context.invokeCommand(self)
    def backState(self):
        self._previousContext.reset()
        self.setState(self._previousContext)