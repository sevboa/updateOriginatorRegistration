import re
import sys

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorMts import originatorMts

class importerMts(importer):
    
    def outerOriginatorsAppend(self, stringObject, rejected=False):
        if rejected == True:
            originator = originatorMts(stringObject, self.RejectMessageMts)
        else:
            originator = originatorMts(stringObject)
        if self.GlobalOriginators.isdisjoint({originator.Originator + ';' + str(originator.ProviderId)}):
            self.Originators.add(originator)

    def input(self, stringObject, rejected=False):
        if rejected == True:
            self.outerOriginatorsAppend(stringObject, True)
        else:
            self.outerOriginatorsAppend(stringObject)
        

