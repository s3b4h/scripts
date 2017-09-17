#criar pasta em python
import os.path
import time

# nao tenho bem a certeza se e isto que quer, nao sera: if username == 'USERNAME CORRETO' and password == 'PASSWORD CORRETA': ?
#if username != None and password != None:
data = time.strftime("%Y%m%d-%H%M")
#print data
caminho = 'C:\\bkp'+data
if os.path.isdir(caminho): # vemos de este diretorio ja existe
    print ('Ja existe uma pasta com esse nome!')
else:
    os.mkdir(caminho) # aqui criamos a pasta caso nao exista
    print ('Pasta criada com sucesso!')