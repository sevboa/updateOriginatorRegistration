import re
import sys

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorMts import originatorMts

class importerBt(importer):
    
    def outerOriginatorsAppend(self, stringObject):
        if type(stringObject[2].value) == type(int()):
            originator = originatorMts(stringObject, self.RejectMessageMts)
            if self.GlobalOriginators.isdisjoint({originator.Originator + ';' + str(originator.ProviderId)}):
                self.Originators.add(originator)

    def input(self, stringObject):
        self.outerOriginatorsAppend(stringObject)
