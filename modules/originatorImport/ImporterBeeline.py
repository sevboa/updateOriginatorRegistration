import re
import csv

from modules.originatorImport.Importer import importer
from modules.originatorImport.OriginatorBeeline import originatorBeeline

class importerBeeline(importer):
    
    def load(self, extension, providerCode, fileName):
        if extension == 'csv' and providerCode in ('Beeline'):
            with open('./originators/' + fileName, 'r', encoding='cp1251') as fileCsv:
                for string in csv.DictReader(fileCsv, delimiter=';'):
                    self.input(string)
        else:
            print('Неподдерживаемое расширение входящего файла!')
            quit()

    def input(self, string):
        self.outerOriginatorsAppend(originatorBeeline(string))
