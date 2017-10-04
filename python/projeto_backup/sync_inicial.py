#!/usr/bin/env python
import subprocess
import ConfigParser
import socket
import os

def main():
    #pega dados do arquivo de confiuguracao
    hostname = socket.gethostname()
    config = ConfigParser.ConfigParser()
    config.read("./agent_duo.conf")
    dir1 = config.get("diretorios", "DIR_ORIGEM")
    dir2 = config.get("diretorios","DIR_COPIA") + "/" + hostname
    
    if os.path.exists(dir2) is True:
        print('Diretorio ja existe')
    else:
        os.makedirs(dir2)
    
    if not dir1.endswith('/'): dir1=dir1+'/'
    
    sync_inicial='rsync -acv %s %s' %(dir1,dir2)
    subprocess.call(sync_inicial,shell=True)
if __name__ == '__main__':
 main()