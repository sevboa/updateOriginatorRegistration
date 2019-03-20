import sys
import os
import pg8000
import configparser
import re

try:
    import configparser
except ImportError:
    import ConfigParser as configparse

'''
pg8000.connect(
	user=None, 
	host='localhost', 
	unix_sock=None, 
	port=5432, 
	database=None, 
	password=None, 
	ssl=False, 
	timeout=None, 
	**kwargs)
'''

def configRead(dbName):
    config = configparser.ConfigParser()
    config.read('cfg\\data_bases.cfg')
    print(' config load')
    return dict(config._sections[dbName])
    
def configWrite(dbName, params):
    config = configparser.ConfigParser()
    config.read('cfg\\data_bases.cfg')
    if dbName not in config.sections():
        config.add_section(dbName)
    config._sections[dbName] = params
    with open('cfg\\data_bases.cfg', "w") as config_file:
        config.write(config_file)
    print('config write complete')
        
class dbPostgre:
    def __init__(self, dbName):
        self.DbName = dbName
        self.connect()
    
    def connect(self):
        bdCfg = configRead(self.DbName)
        self.DbConn = pg8000.connect(
        	host=bdCfg['host'],
        	port=int(bdCfg['port']),
        	database=bdCfg['database'],
        	user=bdCfg['user'], 
        	password=bdCfg['password'])
        print(' ' + self.DbName + ' connected')
        self.Cursor = self.DbConn.cursor()
        
    def close(self):
        self.DbConn.close()
        print(' ' + self.DbName + ' close')
        
    def execute(self, query, fieldnames):
        self.Cursor.execute(re.sub("[\r\n\t\\s]+", " ", query))
        result = list()
        for r in self.Cursor.fetchall():
            rb = list()
            for ra in list(r):
                rb.append(str(ra))
            r = rb
            result.append(dict(zip(fieldnames, r)))
        return result
    
    def commit(self):
        self.DbConn.commit()
    

def dbSelect(bdName, query, fieldnames):
    dbConn = dbPostgre(bdName)
    data = dbConn.execute(query, fieldnames)
    dbConn.close()
    return data

def dbInsert(bdName, query, fieldnames):
    dbConn = dbPostgre(bdName)
    data = dbConn.execute(query, fieldnames)
    dbConn.commit()
    dbConn.close()
    return data


## Тестирование (при импорте не отрабатывает)
if __name__ == "__main__":

    configWrite('sms57test', dict(
         host='192.168.11.227',
         port=5432,
         database='easysms',
         user='easysms',
         password='895erfk967jsdfjhlwfdju83gfkkr'
         ))
    
    dbConn = dbPostgre('sms57test')
    
    fieldnames = [
        'full_name', 
        'login', 
        'user_id', 
        'country_id', 
        'operator_group_id', 
        'operator_id',
        'gate_id', 
        'priority']

    result = dbConn.execute('''
        WITH t2 as (
            WITH t1 as (
                SELECT 
                    users.full_name, 
                    users.login, 
                    users.id as user_id, 
                    routes.country_id, 
                    routes.operator_group_id, 
                    routes.operator_id, 
                    routes.gate_id, 
                    routes.priority 
                FROM users
                INNER JOIN routes on users.routing_group_id = routes.routing_group_id
                WHERE users.id = 22 AND routes.originator = '^.*' AND routes.user_id in (users.id, 0)
                ORDER BY 
                    users.id, 
                    routes.priority DESC, 
                    routes.country_id, 
                    routes.operator_group_id, 
                    routes.operator_id
            )

            SELECT DISTINCT ON (
                    t1.user_id, 
                    t1.country_id, 
                    t1.operator_group_id, 
                    t1.operator_id) *
            FROM t1)
        
        SELECT                   
            users.full_name as full_name, 
            users.login as login, 
            t2.user_id as user_id, 
            t2.country_id as country_id, 
            t2.operator_group_id as operator_group_id, 
            t2.operator_id as operator_id,
            t2.gate_id as gate_id,
            t2.priority as priority
        FROM t2
        INNER JOIN users ON users.id = t2.user_id
        ORDER BY 
            t2.user_id, 
            t2.priority DESC, 
            t2.country_id, 
            t2.operator_group_id, 
            t2.operator_id
    ''', fieldnames)

    #print(len(result))

    for s in result:
        print(s)

    dbConn.close()




