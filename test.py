import sys
import json
import csv
import os

a = dict({'asd':dict({'dfg':5})})
b = a['asd']
b['dfg']=6
print(len(str(a)[:5]))

exit()

class a:
    def __init__(
        self, 
        ident: int, 
        max_num: int, 
        name: str
    ):
        self._ident = ident
        self._max_num = max_num
        self._name = name
    
    def __getitem__(self, qwe):
        return self._ident + 1
    
    def __setitem__(self, qwe, ident):
        self._ident = ident
    
    def __call__(self):
        return self._ident, self._max_num, self._name
     
b = a(1,3,'ewr')

b['qwe'] = 5

print(b['qwe'])

exit()

RejectMessageMts = list()

filePath = './input/' + 'rejectMessageMts.csv'
with open(filePath, 'r', encoding='utf-8') as fileCsv:
    for string in csv.DictReader(fileCsv, delimiter=';'):
        if string['registration_status_id'] > '0':
            RejectMessageMts.append(string)

with open("statusesMts.json", "w", encoding="utf-8") as file:
    json.dump(RejectMessageMts, file,ensure_ascii=False,indent=4)