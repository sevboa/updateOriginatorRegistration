import sys
import json
import csv

RejectMessageMts = list()

filePath = './input/' + 'rejectMessageMts.csv'
with open(filePath, 'r', encoding='utf-8') as fileCsv:
    for string in csv.DictReader(fileCsv, delimiter=';'):
        if string['registration_status_id'] > '0':
            RejectMessageMts.append(string)

with open("statusesMts.json", "w", encoding="utf-8") as file:
    json.dump(RejectMessageMts, file,ensure_ascii=False,indent=4)