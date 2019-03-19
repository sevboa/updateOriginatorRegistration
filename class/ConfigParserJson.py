import json

def singleton(configParserJson):
    instances = {}
    def getinstance(*args, **kwargs):
        if configParserJson not in instances:
            instances[configParserJson] = configParserJson(*args, **kwargs)
        return instances[configParserJson]
    return getinstance

@singleton
class configParserJson:
    Text = '1'
    def __init__(self, filePath='config.json'):
        with open(filePath, 'r', encoding='utf-8') as configFile: #открываем файл на чтение
            data = json.load(configFile) #загружаем из файла данные в словарь data
            for key in data.keys():
                self.__dict__[key] = data[key]
    


## Тестирование (при импорте не отрабатывает)
if __name__ == "__main__":

    object_1 = configParserJson()
    object_1.Text = '2'
    object_2 = configParserJson()
    print(object_2.Text)
    
    #ConfigParserJson = configParserJson.call()
    #print(ConfigParserJson.__dict__)