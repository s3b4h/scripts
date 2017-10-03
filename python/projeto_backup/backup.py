#!/usr/bin/env python
import subprocess
import ConfigParser
import time
import os.path
import socket

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:29:18 2017

@author: s3b4h
"""


def parse_ambiente():
    config = ConfigParser.ConfigParser()
    config.read("./agent_duo.conf")
    modulo = config.get("def_ambiente", "MODULO")
    cliente = config.get("def_ambiente", "CLIENTE")
    ambiente = config.get("def_ambiente", "AMBIENTE")
    var_amb = modulo + ' ' + cliente + ' ' + ambiente
    return var_amb


def inicio(horaInicio):
    inicio = "BACKUP FULL DO FILESERVER INICIADO AS %s" % horaInicio
    return inicio


def termino(diaInicio, horaInicio, pathlog):
    hoje = (time.strftime("%d-%m-%Y"))
    horaFinal   = time.strftime('%H:%M:%S')
    final = '''
  ===========================================================================
                            BACKUP FULL FINALIZADO

                HORA INICIAL:    %s  -  %s
                HORA FINAL  :    %s  -  %s
                LOG FILE    :    %s
  ===========================================================================

    ''' % (diaInicio, horaInicio, hoje, horaFinal, pathlog)
    return final


def geralog():
    logfile     = 'backup-full.txt'
    pathlog     = '/var/log/%s' % logfile

    return pathlog



def executa_backup():
    #pega informacoes do arquivo para montar o tar
    hostname = socket.gethostname()
    date = (time.strftime("%Y%m%d"))
    arquivo = '%s-%s-full.tar.gz' % (hostname, date)
    config = ConfigParser.ConfigParser()
    config.read("./agent_duo.conf")
    dir_origem = config.get("diretorios", "DIR_ORIGEM")
    dir_destino = config.get("diretorios", "DIR_DESTINO") + "/" + date + "/" + "APP/"

    #verifica se pasta ja existe se nao existir cria
    if os.path.isdir(dir_destino):
        print ('Ja existe uma pasta com esse nome!')
    else:
        os.makedirs(dir_destino)
        print ('Pasta criada com sucesso!')

    #exclusao de pastas do tar
    exclude_dir = config.get("diretorios","EXCLUDE_DIR")
    if exclude_dir == '':
        backup = 'tar cvf %s %s' %(dir_destino + arquivo, dir_origem)
        print (backup)
    
    else:
        lista_exclusao = ""
        for item in exclude_dir.split(' '):
            lista_exclusao += "--exclude=" + str(item) + ' '
            backup = 'tar cvf %s %s %s' % (dir_destino + arquivo, dir_origem, lista_exclusao)   
    
        print (backup)
    return backup
    

def main():
    #inicio do log
    horaInicio  = time.strftime('%H:%M:%S')
    pathlog     = geralog()
    exec_backup = executa_backup()
    log         = ' >> %s' % pathlog
    start       = inicio(horaInicio)
    
    l = open(pathlog, 'w')
    l.write(start)
    l.close()
    
    
    #executa backup
    subprocess.call(exec_backup + log, shell=True)
    
    #fim do backup
    diaInicio   = (time.strftime("%d-%m-%Y"))
    final       = termino(diaInicio, horaInicio, pathlog)
    r           = open(pathlog, 'w')
    r.write(final)
    r.close()
    

main()