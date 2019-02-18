import re
import sys
import csv

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorBeeline import originatorBeeline

class importerBeeline(importer):
    
    def load(extension, providerCode, fileName):
        if extension == 'csv' and providerCode in ('Beeline', 'SMSC'):
            with open('./originators/' + fileName, 'r', encoding='cp1251') as fileCsv:
                for string in csv.DictReader(fileCsv, delimiter=';'):
                    self.input(string)

    def input(self, string):
        self.outerOriginatorsAppend(originatorBeeline(string))
