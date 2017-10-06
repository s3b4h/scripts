#!/usr/bin/env python

import os
import filecmp
import re
import shutil
import subprocess
import ConfigParser
import time
import socket

holderlist=[]
    
def sync_inicial():
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


def compareme(dir1, dir2):
    dircomp=filecmp.dircmp(dir1,dir2)
    only_in_one=dircomp.left_only
    diff_in_one=dircomp.diff_files
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in only_in_one]
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in diff_in_one]
    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1,item)), os.path.abspath(os.path.join(dir2,item)))
        return holderlist

    
def main():
    #pega dados do arquivo de confiuguracao
    hostname = socket.gethostname()
    date = (time.strftime("%Y%m%d"))
    config = ConfigParser.ConfigParser()
    config.read("./agent_duo.conf")
    dir1 = config.get("diretorios", "DIR_ORIGEM")
    dir2 = config.get("diretorios","DIR_COPIA") + "/" + hostname
    dir3 = config.get("diretorios", "DIR_DESTINO") + "/" + date + "/" + "APP/"  + hostname
    arquivo = '%s-diff.tar.gz' % (date)
      
    #compara os diretorios
    source_files=compareme(dir1,dir2)
    dir1=os.path.abspath(dir1)
    dir3=os.path.abspath(dir3)
    destination_files=[]
    new_dirs_create=[]
    for item in source_files:
        destination_files.append(re.sub(dir1, dir3, item) )
    for item in destination_files:
        new_dirs_create.append(os.path.split(item)[0])
    for mydir in set(new_dirs_create):
        if not os.path.exists(mydir): os.makedirs(mydir)
    #copy pair
    copy_pair=zip(source_files,destination_files)
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])
     
    #compactar pasta
    if os.path.exists(dir3):
        cria_tar = 'tar cvf %s %s' %(dir3 + arquivo,dir3)
        if not dir3.endswith('/'): dir3=dir3+'/'
        atualizar='rsync -acv %s %s' % (dir3,dir2)
        remove_dir='rm -rf %s' %(dir3)
        subprocess.call(cria_tar, shell=True)
        subprocess.call(atualizar, shell=True)
        subprocess.call(remove_dir, shell=True)
    else:
        print('Nao existe arquivo diferencial. Nao houve alteracao de arquivos')
   
    
sync_inicial()
main()