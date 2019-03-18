import csv
import re
import sys

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorSmsc import originatorSmsc
import sys

class importerSmsc(importer):
    Statuses = list()
    StatusesCache = dict()
    Operators = list()
    OperatorsCache = dict()
    OriginatorsAB = dict()
    OriginatorsBC = dict()

    def loadConfig(self):
        self.Statuses.extend(self.Config['smsc']['statuses'])
        self.createStatusesCache()
        self.Operators.extend(self.Config['smsc']['operators'])
        self.createOperatorsCache()
    
    def load(self, extension, providerCode, fileName):
        if extension == 'csv' and providerCode in ('SMSC'):
            with open('./originators/' + fileName, 'r', encoding='cp1251') as fileCsv:
                for string in csv.DictReader(fileCsv, delimiter=';'):
                    self.input(string)
        else:
            print('Неподдерживаемое расширение входящего файла!')
            quit()
    
    def input(self, string):
        

        for operator_group_key in self.OperatorsCache.keys():
            operator_group_find, operator_group_regexp = self.OperatorsCache[operator_group_key]
            string['operator_group_id'], string['service_type_id'] = operator_group_key.split(';')

            for statusString in self.StatusesCache.keys():
                string['status'] = statusString
                string['status_id'] = self.StatusesCache[statusString]
                
                if string['Оператор'].find(operator_group_find + string['status']) != -1:
                    result = re.search(r'(?<=' + operator_group_regexp + string['status'] + r' \()[^\)]*', string['Оператор'])
                    if result != None:
                        result2 = re.search(operator_group_regexp + string['status'] + r' \(.{0,11}\)\s*', string['Оператор'])
                        #print('\'' + result2.group(0) + '\'')
                        string['Оператор'] = re.sub(operator_group_regexp + string['status'] + r' \(.{0,11}\)\s*', '', string['Оператор'])
                        string.update(originator_change=result.group(0))
                        self.appendSmscOriginator(string)
                    else:
                        result2 = re.search(operator_group_regexp + string['status'] + r'\s*', string['Оператор'])
                        #print('\'' + result2.group(0) + '\'')
                        string['Оператор'] = re.sub(operator_group_regexp + string['status'] + r'\s*', '', string['Оператор'])
                        string.update(originator_change=string['Имя'])
                        self.appendSmscOriginator(string)
        if string['Оператор'] != '' and string['Оператор'] != ' Теле2 (бесплатно): допущено оператором':
            if re.match(r'^\s*$', string['Оператор']) == None:
                print('\'' + string['Оператор'] + '\'')

    def OriginatorsABBCCheck(self, originator):
        ABArrayKey = originator.OriginatorChange + ";" + str(originator.OperatorGroupId) + ";" + str(originator.ServiceTypeId) + ";" + str(originator.StatusId)
        BCArrayKey = originator.Originator + ";" + str(originator.OperatorGroupId) + ";" + str(originator.ServiceTypeId) + ";" + str(originator.StatusId)
        
        OriginatorABList = self.OriginatorsAB.get(BCArrayKey)
        OriginatorBCList = self.OriginatorsBC.get(ABArrayKey)
        
        ## проверяем наличие
        if OriginatorABList != None:
            for originatorAB in OriginatorABList:
                if originatorAB.Originator != originator.OriginatorChange and originatorAB.OriginatorChange != originator.OriginatorChange:
                    #print('AB', str(originator.OperatorGroupId), originatorAB.OriginatorChange, originator.OriginatorChange)
                    originatorAB.OriginatorChange = originator.OriginatorChange
        elif OriginatorBCList != None:
            for originatorBC in OriginatorBCList:
                if originatorBC.OriginatorChange != originator.Originator and originator.OriginatorChange != originatorBC.OriginatorChange:
                    #print('BC', str(originator.OperatorGroupId), originatorBC.OriginatorChange, originator.OriginatorChange)
                    originator.OriginatorChange = originatorBC.OriginatorChange
        
        OriginatorABList = self.OriginatorsAB.get(ABArrayKey)
        OriginatorBCList = self.OriginatorsBC.get(BCArrayKey)
        
        ## добавляем
        if OriginatorABList == None:
            self.OriginatorsAB.update({ABArrayKey: {originator}})
        else:
            OriginatorABList.add(originator)
        if OriginatorBCList == None:
            self.OriginatorsBC.update({BCArrayKey: {originator}})
        else:
            OriginatorBCList.add(originator)

    def appendSmscOriginator(self, string):
        OriginatorSmsc = originatorSmsc(string)
        
        self.OriginatorsABBCCheck(OriginatorSmsc)
        
        self.outerOriginatorsAppend(OriginatorSmsc)
        self.appendSmscOriginatorChange(string)
        self.appendSmscYota(string)
    
    def appendSmscOriginatorChange(self, string):
        if string['Имя'] != string['originator_change']:
            stringOriginatorChange = string.copy()
            stringOriginatorChange.update(Имя=stringOriginatorChange['originator_change'])
            self.outerOriginatorsAppend(originatorSmsc(stringOriginatorChange))

    def appendSmscYota(self, string):
        if string['operator_group_id'] == '1':
            stringYota = string.copy()
            stringYota.update(service_type_id='4')
            stringYota.update(operator_group_id='15')
            
            OriginatorSmsc = originatorSmsc(stringYota)

            self.OriginatorsABBCCheck(OriginatorSmsc)
            
            self.outerOriginatorsAppend(OriginatorSmsc)
            self.appendSmscOriginatorChange(stringYota)

    def createStatusesCache(self):
        for status in self.Statuses:
            self.StatusesCache.update({status['text']: str(status['registration_status_id'])})

    def createOperatorsCache(self):
        for operator in self.Operators:
            self.OperatorsCache.update({str(operator['operator_group_id']) + ';' + str(operator['service_type_id']): [operator['text'], operator['regexp']]})