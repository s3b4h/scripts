# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:29:18 2017

@author: sjunior
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 09:58:47 2017

@author: sjunior
"""

import subprocess
import ConfigParser
import time
import os.path


def parse_ambiente():
    config = ConfigParser.ConfigParser()
    config.read("./agent_duo.conf")
    modulo = config.get("def_ambiente", "MODULO")
    cliente = config.get("def_ambiente", "CLIENTE")
    ambiente = config.get("def_ambiente", "AMBIENTE")
    var_amb = modulo + ' ' + cliente + ' ' + ambiente
    return var_amb

def executa_backup():
        date = (time.strftime("%Y%m%d"))
        arquivo = '%s-full.tar.gz' % date
        config = ConfigParser.ConfigParser()
        config.read("./agent_duo.conf")
        dir_origem = config.get("diretorios","DIR_ORIGEM")
        dir_destino = config.get("diretorios","DIR_DESTINO") + "/" + date + "/" + "APP/"
        #exclude_dir = config.get("diretorios","EXCLUDE_DIR")
        
        if os.path.isdir(dir_destino):
            print ('Ja existe uma pasta com esse nome!')
        else:
            os.makedirs(dir_destino)
            print ('Pasta criada com sucesso!')

        backup = 'tar cvf %s %s' % (dir_destino + arquivo, dir_origem )
        print backup
        return backup


def seleciona_ambiente():
    ambiente = parse_ambiente()
    if ambiente  == "ambulatorial cross prod":
        executa_backup()
           
    elif ambiente == "urgencia cross prod":
        print "Ambiente urgencia Cross"
    elif ambiente == "ambulatorial cross homologacao":
        print "Ambiente ambulatorial homologacao"
    else:
        print "Definir Ambiente"

def main():
    seleciona_ambiente()
    exec_backup = executa_backup()
    
    subprocess.call(exec_backup, shell=True)
main()
