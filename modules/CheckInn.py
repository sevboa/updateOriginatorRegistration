def checkInn(inn):
    inn = list(inn)
    if len(inn) not in (10, 12):
        return '1'
 
    def inn_csum(inn):
        k = (3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8)
        pairs = zip(k[11-len(inn):], [int(x) for x in inn])
        return str(sum([k * v for k, v in pairs]) % 11 % 10)
 
    if len(inn) == 10:
        if inn[-1] == inn_csum(inn[:-1]):
            result = '0'
        else:
            result = '1'
    else:
        if inn[-2:] == list(inn_csum(inn[:-2]) + inn_csum(inn[:-1])):
            result = '0'
        else:
            result = '1'
    return result