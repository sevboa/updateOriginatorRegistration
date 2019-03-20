import re
import csv

from modules.originatorImport.Importer import importer
from modules.originatorImport.OriginatorTele2 import originatorTele2

class importerTele2(importer):
    
    def load(self, extension, providerCode, fileName):
        if extension == 'csv' and providerCode in ('Tele2'):
            with open('./originators/' + fileName, 'r', encoding='cp1251') as fileCsv:
                for string in csv.reader(fileCsv, delimiter=';'):
                    self.input(string)
        else:
            print('Неподдерживаемое расширение входящего файла!')
            quit()

    def input(self, string):
        self.outerOriginatorsAppend(originatorTele2(string))