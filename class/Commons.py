import codecs
import csv
import io
import sys
from time import sleep

sys.path.append('./class')
from Counter import Counter
from dbPostgre import dbPostgre

def sortingByFieldNames(innerList, fieldNames):
    params = fieldNames.copy()
    counter = Counter(len(params), 5.0)
    params.reverse()
    innerList = dedublicateListDict(innerList)
    for param in params:
        counter.step('sorting...')
        innerList.sort(key=lambda k: k[param])
    counter.lastTell('sorted')
    return innerList

def sortingObjects(innerList, fieldNames):
    params = fieldNames.copy()
    counter = Counter(len(params), 5.0)
    params.reverse()
    innerList = dedublicateListDict(innerList)
    for param in params:
        counter.step('sorting...')
        innerList.sort(key=lambda k: param)
    counter.lastTell('sorted')
    return innerList

def csvLoad(fileName, fieldNames):
    while True:
        try:
            with io.open(fileName, 'r', encoding='utf-8-sig') as fileCsv:
                print('\r load ' + fileName + '                        ')
                counter = Counter(len(io.open(fileName, 'r', encoding='utf-8-sig').readlines()) - 1, 0.2)
                innerData = csv.DictReader(fileCsv, delimiter=';')
                outStrings = list()
                for string in innerData:
                    counter.step('data load...')
                    outString = dict()
                    for stringKey in string.keys():
                        if stringKey in fieldNames:
                            if string[stringKey] == 'NULL':
                                string[stringKey] = ''
                            outString.update({stringKey: str(string[stringKey])})
                    outStrings.append(outString)
            counter.lastTell(' data loaded')
            outStrings = sortingByFieldNames(outStrings, fieldNames)
            return outStrings
        except PermissionError:
            print('\r!!!Please, close the file ' + fileName, end='')
            sleep(1)
    
def csvUnload(innerStrings, fileNameOut, fieldNames):
    while True:
        try:
            with open('./output/' + fileNameOut, 'w', newline='', encoding='utf-8-sig') as outFile:
                print('\r unload to ' + fileNameOut + '                        ')
                counter = Counter(len(innerStrings), 0.2)
                writer = csv.DictWriter(outFile, delimiter=';', fieldnames=fieldNames)
                writer.writeheader()
                for string in innerStrings:
                    counter.step('data unload...')
                    inner_dict = string
                    writer.writerow(inner_dict)
            counter.lastTell('data unloaded')
            outFile.close()
            print(' complete')
            break
        except PermissionError:
            print('\r!!!Please, close the file ' + fileNameOut, end='')
            sleep(1)
    
def generateKey(params):
    return ';'.join(params)

def stringToRegexp(string):
    for simb in ['\\', '^', '$', '.', '*', '+', '?', '(', ')', '[', ']', '{', '}', '|']:
        string = string.replace(simb, '\\' + simb)
    return string

def generateInsertSql(table, suffix, innerData, maxStrings):
    print('generate insert SQL ' + table + ' ' + suffix)
    data = innerData.copy()
    try:
        keys = list(data[0].keys())
        query = str()
        counter = Counter(len(innerData), 0.2)
        while len(data):
            queryList = list([
                'INSERT INTO ' + table,
                ' (' + ', '.join(keys) + ') ',
                'VALUES '
            ])
            strings = list()
            i = int()
            while i < maxStrings and len(data):
                counter.step('generate...')
                dataString = data.pop(0)
                params = list()
                for key in keys:
                    try:
                        if type(dataString[key]) == type(str()):
                            dataString[key] = dataString[key].replace('\'', '\'\'')
                            params.append('\'' + dataString[key] + '\'')
                        else:
                            params.append(str(dataString[key]))
                    except KeyError:
                        print(dataString)
                        None
                strings.append('(' + ', '.join(params) + ')')
                i += 1
            queryList.append(', '.join(strings))
            query = '\n'.join([query, ''.join(queryList) + ';'])
        counter.lastTell('generated')
        f = open('./sql_queries/' + table + '_' + suffix + '.sql', 'w')
        f.write(query)
        print('   complete')
        return query
    except IndexError:
        print('  fail!')

def singleSelect(bdName, query, fieldNames):
    dbConn = dbPostgre(bdName)
    result = dbConn.execute(query, fieldNames)
    dbConn.close()
    return result

def dedublicateListDict(innerStrings):
    dedublicadeDict = dict()
    for innerString in innerStrings:
        params = list()
        for param in innerString.values():
            params.append(str(param))
        dedublicadeDict.update({';'.join(params): innerString})
    return list(dedublicadeDict.values())


## Тестирование (при импорте не отрабатывает)
if __name__ == "__main__":

    string = str('\'SD|E\'')
    print(string)
    string = stringToRegexp(string)
    print(string)

    testListDict = list([
        dict(asd = 123, fds = 321),
        dict(asd = 234, fds = 432),
        dict(asd = 345, fds = 543),
        dict(asd = 123, fds = 321),
        dict(asd = 456, fds = 654)
    ])
    
    print(dedublicateListDict(testListDict))
