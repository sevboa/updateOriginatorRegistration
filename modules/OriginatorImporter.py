import csv
import re
from copy import copy
from operator import attrgetter

import openpyxl

from modules.Counter import counter

from modules.originatorImport.ImporterBeeline import importerBeeline
from modules.originatorImport.ImporterMts import importerMts
from modules.originatorImport.ImporterSmsc import importerSmsc
from modules.originatorImport.ImporterTele2 import importerTele2


class originatorImporter:
    Originators = list()
    OriginatorsByOperatorsGropupId = dict()
    
    def __init__(self, provider, fileName):
        if   provider == 'beeline':
            self.importOriginators(importerBeeline(fileName))
        elif provider == 'mts':
            self.importOriginators(importerMts(fileName))
        elif provider == 'tele2':
            self.importOriginators(importerTele2(fileName))
        elif provider == 'smsc':
            self.importOriginators(importerSmsc(fileName))
        else:
            print(provider + ' пока не работает!')
            pause()
            exit()

    def importOriginators(self, ProviderImporter):
        self.Originators.extend(
            self.deduplicate(
                list(
                    ProviderImporter.Originators
                )
            )
        )
        self.sortOriginators([
            'ProviderId', 
            'OriginatorChange',
            'OperatorGroupId',
            'ServiceTypeId',
            'Originator', 
            'StatusId',
            'ContractorLegalEntity',
            'ContractorInn'
        ])
        for originator in self.Originators:
            self.OriginatorsByOperatorsGropupIdAppend(originator)

    def deduplicate(self, originatorsList):
        originatorsDict = dict()
        Counter = counter(len(originatorsList), 0.5)
        for originator in originatorsList:
            Counter.step('deduplicate...')
            key = ';'.join([
                str(originator.Originator), 
                str(originator.ServiceTypeId), 
                str(originator.OperatorGroupId)
                ])
            Originator = originatorsDict.get(key)
            if Originator != None:
                if Originator.getStatusPriority() >= originator.getStatusPriority():
                    continue
            originatorsDict.update({key: originator})
        Counter.lastTell('deduplicated')
        return list(originatorsDict.values())

    def sqlGenerate(self, originators, count):
        queryString = str()
        queryBegin = 'CREATE TABLE originators_smsc(operator_group_id integer, service_type_id integer, originator varchar, originator_change varchar, account_id text, status_id integer, contractor_legal_entity text, contractor_inn text, is_incorrect_inn integer, originator_id integer, originator_change_id integer);'
        queryBegin2 = '\n\nINSERT INTO originators_smsc(operator_group_id, service_type_id, originator, originator_change, account_id, status_id, contractor_legal_entity, contractor_inn, is_incorrect_inn, originator_id, originator_change_id) \nVALUES \n'
        queryMiddleList = list()
        queryMiddleString = str()
        stringCount = int()
        for Originator in originators:
            stringCount += 1
            originator = Originator.output()
            queryMiddleString =  '('
            queryMiddleString += str(originator['operator_group_id'])
            queryMiddleString += ', '
            queryMiddleString += str(originator['service_type_id'])
            queryMiddleString += ', \''
            queryMiddleString += originator['originator'].replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', \''
            queryMiddleString += originator['originator_change'].replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', \''
            queryMiddleString += originator['account_id']
            queryMiddleString += '\', '
            queryMiddleString += str(originator['status_id'])
            queryMiddleString += ', \''
            queryMiddleString += originator['contractor_legal_entity'].replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', \''
            queryMiddleString += originator['contractor_inn']
            queryMiddleString += '\', '
            queryMiddleString += str(originator['is_incorrect_inn'])
            queryMiddleString += ', (SELECT id AS originator_id FROM originator WHERE originator = \''
            queryMiddleString += originator['originator'].replace('\'', '\'\'')
            queryMiddleString += '\' AND case_sensitive = 1)'
            queryMiddleString += ', (SELECT id AS originator_change_id FROM originator WHERE originator = \''
            queryMiddleString += originator['originator_change'].replace('\'', '\'\'')
            queryMiddleString += '\' AND case_sensitive = 1))'
            queryMiddleList.append(queryMiddleString)
            if stringCount > count:
                queryString += str(queryBegin2 + ',\n'.join(queryMiddleList) + ';')
                queryMiddleList = list()
                stringCount = 0
        queryString += str(queryBegin2 + ',\n'.join(queryMiddleList) + ';')
        queryString = queryBegin + queryString
        print('sql generated')
        return queryString
    
    def sqlGenerateByOperators(self, originators, count):
        queryList = list()
        queryBegin = 'CREATE TABLE originators_smsc(operator_group_id integer, service_type_id integer, originator varchar, originator_change varchar, account_id text, status_id integer, contractor_legal_entity text, contractor_inn text, is_incorrect_inn integer, originator_id integer, originator_change_id integer);'
        queryBegin += '\nINSERT INTO originators_smsc(operator_group_id, service_type_id, originator, originator_change, account_id, status_id, contractor_legal_entity, contractor_inn, is_incorrect_inn, originator_id, originator_change_id) \nVALUES \n'
        queryMiddleList = list()
        queryMiddleString = str()
        stringCount = int()
        for Originator in originators:
            stringCount += 1
            originator = Originator.output()
            queryMiddleString =  '('
            queryMiddleString += str(originator['operator_group_id'])
            queryMiddleString += ', '
            queryMiddleString += str(originator['service_type_id'])
            queryMiddleString += ', \''
            queryMiddleString += originator['originator'].replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', \''
            queryMiddleString += originator['originator_change'].replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', \''
            queryMiddleString += originator['account_id']
            queryMiddleString += '\', '
            queryMiddleString += str(originator['status_id'])
            queryMiddleString += ', \''
            queryMiddleString += originator['contractor_legal_entity'].replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', \''
            queryMiddleString += originator['contractor_inn']
            queryMiddleString += '\', '
            queryMiddleString += str(originator['is_incorrect_inn'])
            queryMiddleString += ', (SELECT id AS originator_id FROM originator WHERE originator = \''
            queryMiddleString += originator['originator'].replace('\'', '\'\'')
            queryMiddleString += '\' AND case_sensitive = 1)'
            queryMiddleString += ', (SELECT id AS originator_change_id FROM originator WHERE originator = \''
            queryMiddleString += originator['originator_change'].replace('\'', '\'\'')
            queryMiddleString += '\' AND case_sensitive = 1))'
            queryMiddleList.append(queryMiddleString)
            if stringCount > count:
                query = str(queryBegin + ',\n'.join(queryMiddleList) + ';')
                queryList.append(query)
                queryMiddleList = list()
                stringCount = 0
        query = str(queryBegin + ',\n'.join(queryMiddleList) + ';')
        queryList.append(query)
        print('sql generated')
        return queryList

    def OriginatorsByOperatorsGropupIdAppend(self, originator):
        self.OriginatorsByOperatorsGropupId.setdefault(str(originator.operatorGroup()), list())
        self.OriginatorsByOperatorsGropupId[str(originator.operatorGroup())].append(originator)

    def sortOriginators(self, params):
        Counter = counter(len(params), 5.0)
        for param in params:
            Counter.step('sorting...')
            self.Originators.sort(key=attrgetter(param))
        Counter.lastTell('sorted')

    def outputListDict(self):
        originators = list()
        for originator in self.Originators:
            originators.append(originator.output())
        return originators

    def getAllSpellingOriginators(self):
        spellingOriginators = set()
        for originator in self.Originators:
            spellingOriginators.add(originator.Originator)
            spellingOriginators.add(originator.OriginatorChange)
        return sorted(list(spellingOriginators))
            

    def spellingOriginatorsSqlGenerate(self):
        queryList = list()
        queryBegin = 'CREATE TABLE originators_spelling_smsc(originator text, case_sensitive int);'
        queryBegin += '\nINSERT INTO originators_spelling_smsc(originator, case_sensitive) \nVALUES \n'
        queryMiddleList = list()
        queryMiddleString = str()
        for spellingOriginator in self.getAllSpellingOriginators():
            queryMiddleString =  '(\''
            queryMiddleString += spellingOriginator.replace('\'', '\'\'').replace('\\', r'\\\\')
            queryMiddleString += '\', 1)'
            queryMiddleList.append(queryMiddleString)
        query = str(queryBegin + ',\n'.join(queryMiddleList) + ';')
        queryList.append(query)
        print('sql generated')
        return query