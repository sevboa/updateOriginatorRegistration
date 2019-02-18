import re
import sys

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorBeeline import originatorBeeline

class importerBeeline(importer):
    
    def input(self, string):
        self.outerOriginatorsAppend(originatorBeeline(string))
