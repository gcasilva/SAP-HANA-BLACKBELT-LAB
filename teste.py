import sys
import datetime

from hdbcli import dbapi

connA = dbapi.connect('172.31.34.187', 30015, 'SYSTEM', 'Password1234')
connB = dbapi.connect('172.31.41.6', 30015, 'SYSTEM', 'Password1234')

def isConnected(connection):
    return connection.isconnected();

def select(connection):
    cursor = connection.cursor()
    stmnt = 'Select * from Demo_HANA'
    cursor.execute(stmnt)
    return cursor.fetchall();

def insert(connection, value):
    cursor = connection.cursor()
    stmnt = 'insert into Demo_HANA values (?)'
    cursor.execute(stmnt, value)
    return 0;


print ("##### TESTE DE CONEXAO ####")
print ("")
print ("Site A: "+ str(isConnected(connA)))
print ("Site B: "+ str(isConnected(connB)))
datetime.datetime.now().time()
print(datetime.datetime.now().time())

print ("")
print ("")

print ("##### TESTE DE SELECT ####")
resultA=select(connA)
resultB=select(connB)
print ("Maior registro SiteA: " + str(resultA[-1][0]))
print ("Maior registro SiteB: " + str(resultB[-1][0]))
datetime.datetime.now().time()
print(datetime.datetime.now().time())

print ("")
print ("")

print ("##### TESTE DE INSERT ####")
a=int(resultA[-1][0])+1
b=int(resultB[-1][0])+1
print ("Inserindo valor "+ str(a)+ " no SiteA")
try:
    insert (connA, a)
    print ("done")
except:
        print ("Erro inserindo")

print ("Inserindo valor "+ str(b)+ " no SiteB")
try:
    insert (connB, b)
    print ("done")
except:
    print ("Erro inserindo")
print ("")
print ("")
datetime.datetime.now().time()
print(datetime.datetime.now().time())
print ("##### TESTE DE SELECT ####")
resultA=select(connA)
resultB=select(connB)
print ("Maior registro SiteA: " + str(resultA[-1][0]))
print ("Maior registro SiteB: " + str(resultB[-1][0]))
print ("")
print ("")
datetime.datetime.now().time()
print(datetime.datetime.now().time())
print ("##### TESTE DE SELECT ####")
resultA=select(connA)
resultB=select(connB)
print ("Maior registro SiteA: " + str(resultA[-1][0]))
print ("Maior registro SiteB: " + str(resultB[-1][0]))
datetime.datetime.now().time()
print(datetime.datetime.now().time())
