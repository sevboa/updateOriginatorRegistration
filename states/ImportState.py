
from states.SelectProviderState import selectProviderState
from states.SelectFileState import selectFileState
from modules.OriginatorImporter import originatorImporter

class importState:
    def getText(self, controller):
        if controller.Provider != '':
                print(' Поставщик: ' + controller.Provider)
        else:
            print(' Поставщик: ' + 'не выбран')
        if controller.FileName != '':
            print(' Файл: ' + controller.FileName)
        else:
            print(' Файл: ' + 'не выбран')
        print('\nВыберите пункт меню:')

    def getHelp(self):
        print('[p]provider')
        print('[f]file_name')
        print('[s]setting')
        print('[ok]start_import')

    def invokeCommand(self, controller):
        if   controller.Input in ('p','provider'):
            controller.setState(selectProviderState())
        elif controller.Input in ('f','file_name'):
            controller.setState(selectFileState())
        elif controller.Input in ('s', 'setting'):
            print('Вот настройки')
        elif controller.Input in ('ok','start_import'):
            if controller.Provider == '' or controller.FileName == '':
                print('Недостаточно данных для импорта!')
            else:
                originatorImporter(controller.Provider, controller.FileName)
        
        else:
            print('ошибка!')
            controller.getHelp()