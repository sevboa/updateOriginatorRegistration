

class selectProviderState:
    
    def getText(self, controller):
        if controller.Provider == '':
            print('Укажите провайдера:')
        else:
            print('Укажите провайдера(' + controller.Provider + '):')

    def getHelp(self):
        print('[b]beeline')
        print('[m]mts')
        print('[t]tele2')
        print('[m]motiv (не работает)')
        print('[s]smsc')
        print('[bt]bt')
        print('\n[c]cancel')

    def invokeCommand(self, controller):
        if   controller.Input in ('b','beeline'):
            controller.Provider = 'beeline'
            controller.backState()
        elif controller.Input in ('m','mts'):
            controller.Provider = 'mts'
            controller.backState()
        elif controller.Input in ('t','tele2'):
            controller.Provider = 'tele2'
            controller.backState()
        elif controller.Input in ('m','motiv'):
            print('motiv пока не работает!')
        elif controller.Input in ('s','smsc'):
            controller.Provider = 'smsc'
            controller.backState()
        elif controller.Input in ('bt','bt'):
            controller.Provider = 'bt'
            controller.backState()
        elif controller.Input in ('c', 'cancel'):
            controller.backState()
        else:
            print('ошибка!')
            controller.getHelp()