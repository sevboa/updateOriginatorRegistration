
from states.ImportState import importState

class stateController():
    Active = True
    _context = object()
    Input = str()

    Provider = str()
    FileName = str()

    def input(self):
        self.Input = input('> ')

    def getText(self):
        self._context.getText(self)
    
    def getHelp(self):
        print(' Доступные комманды:')
        self._context.getHelp()

    def setState(self, state):
        self._context = state

    def invokeCommand(self):
        if self.Input == '':
            print('пустой ввод')
            self.getHelp()
        if self.Input in ('h', 'help'):
            self.getHelp()
        elif self.Input in ('q', 'quit'):
            print('Выходим')
            self.Active = False
        else:
            self._context.invokeCommand(self)
    def backState(self):
        self._context = importState(self)