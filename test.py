import sys, csv
from openpyxl import load_workbook
from operator import itemgetter

sys.path.append('./class')

a = {1,2,3}
b = {1,2}

print(
    b.issubset(a)
)