import sys, re

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorTele2 import originatorTele2

class importerTele2(importer):
    
    def input(self, string):
        self.outerOriginatorsAppend(string)