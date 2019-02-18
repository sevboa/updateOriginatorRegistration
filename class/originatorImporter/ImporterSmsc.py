import csv
import re
import sys

sys.path.append('./class/originatorImporter')
from Importer import importer
from OriginatorSmsc import originatorSmsc

class importerSmsc(importer):
    SmscStatuses = {
        '3' : 'допущено оператором',
        '4' : 'не принято оператором',
        '7' : 'необходимы подтверждающие документы',
        '2' : 'отправлено на регистрацию',
        '2' : 'ожидает регистрации'
    }
    OperatorsGroups = {
        '1;5' : ['Мегафон (платно): ', r'Мегафон \(платно\): '],
        '1;4' : ['Мегафон (бесплатно): ', r'Мегафон \(бесплатно\): '],
        '3;4' : ['МТС: ', r'МТС: '],
        '4;5' : ['Теле2 (платно): ', r'Теле2 \(платно\): '],
        '2;5' : ['Билайн (платно): ', r'Билайн \(платно\): '],
        '2;4' : ['Билайн (бесплатно): ', r'Билайн \(бесплатно\): ']
    }
    OriginatorsAB = dict()
    OriginatorsBC = dict()

    def input(self, string):
        for status_id in self.SmscStatuses.keys():
            string['status'] = self.SmscStatuses[status_id]
            string['status_id'] = status_id

            for operator_group_key in self.OperatorsGroups.keys():
                operator_group_find, operator_group_regexp = self.OperatorsGroups[operator_group_key]
                string['operator_group_id'], string['service_type_id'] = operator_group_key.split(';')
                
                if string['Оператор'].find(operator_group_find + string['status']) != -1:
                    result = re.search(r'(?<=' + operator_group_regexp + string['status'] + r' \()[^\)]*', string['Оператор'])
                    if result != None:
                        string.update(originator_change=result.group(0))
                        self.appendSmscOriginator(string)
                    else:
                        string.update(originator_change=string['Имя'])
                        self.appendSmscOriginator(string)

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
