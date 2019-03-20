import json
import sys

def singleton(configParserJson):
    instances = {}
    def getinstance(*args, **kwargs):
        if configParserJson not in instances:
            instances[configParserJson] = configParserJson(*args, **kwargs)
        return instances[configParserJson]
    return getinstance

@singleton
class configParserJson:
    def __init__(self, filePath='config.json'):
        with open(filePath, 'r', encoding='utf-8') as configFile: #открываем файл на чтение
            data = json.load(configFile) #загружаем из файла данные в словарь data
            for key in data.keys():
                self.__dict__[key] = data[key]
    


## Тестирование (при импорте не отрабатывает)
if __name__ == "__main__":

    ConfigParserJson = configParserJson()
    print(ConfigParserJson.__dict__)