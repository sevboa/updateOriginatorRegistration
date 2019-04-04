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
    
    Data = dict()
    Part = dict()
    Cursor = list()
    
    def __init__(self, filePath='config.json'):
        with open(filePath, 'r', encoding='utf-8') as configFile: #открываем файл на чтение
            data = json.load(configFile) #загружаем из файла данные в словарь data
            self.Data = dict(data)
            for key in data.keys():
                self.__dict__[key] = data[key]
        self.setCursorPart()
                
    def setChildPart(self, key):
        self.Cursor.append(key)
        self.setCursorPart()
    
    def setParentPart(self):
        self.Cursor.pop(-1)
        self.setCursorPart()
        
    def setCursorPart(self):
        self.Part = self.Data
        if len(self.Cursor) > 0:
            for key in self.Cursor:
                self.Part = self.Part.get(key)
            print(self.Cursor)
    
    def setPartParam(self, key, value):
        if type(self.Part[key]) == type(value):
            self.Part[key] = value
        else:
            print('Тип параметра не совпадает с типом значения!')
    


## Тестирование (при импорте не отрабатывает)
if __name__ == "__main__":

    ConfigParserJson = configParserJson()
    print(ConfigParserJson.__dict__)