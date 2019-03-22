import sys
import re

from states.StateController import stateController
from states.ImportState import importState

print('    Татьяна 0.4')
print(' Добро пожаловать!')
print(' Данная программа предназначена для парсинга')
print(' файлов регистраций имен поставщиков.')
print(' P.S. для помощи введите \'h\'\n')

Controller = stateController()
Controller.setState(importState(Controller))

while Controller.Active:
    Controller.getText()
    Controller.input()
    Controller.invokeCommand()
    print('===================================')


exit()