import json

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