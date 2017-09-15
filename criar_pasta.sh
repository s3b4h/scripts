#!/bin/bash

echo " Digite o nome do arquivo a ser criado
read file
echo "Digite aonde o arquivo será criado, caminho completo"
read dir

if [ -d "$dir" ];then
  # se o diretório existir
  touch "$dir"/"$file"
else
  # se não existir, vai ser criado o diretório
  mkdir "$dir"; touch "$dir"/"$file"
fi


#!/bin/bash

if [ $# -lt 2 ] ; then
echo echo -e "\nExemplo de uso: $0 /home/fabio/DIR-NOVO arq_novo"
exit 1;
else
mkdir -p $1 && touch $1/$2 || echo -e "\nUse $0 /caminho/completo/de/diretorio nomedoarquivo"
fi

em python

import os.path

# nao tenho bem a certeza se e isto que quer, nao sera: if username == 'USERNAME CORRETO' and password == 'PASSWORD CORRETA': ?
if username != None and password != None:
    pasta = 'C:\Backup'
    if os.path.isdir(pasta): # vemos de este diretorio ja existe
        print ('Ja existe uma pasta com esse nome!')
    else:
        os.mkdir(pasta) # aqui criamos a pasta caso nao exista
        print ('Pasta criada com sucesso!')

    # prosseguir com o codigo aqui, nesta linha onde esta o cardinal (hash)

else:
    print 'nao foi possivel logar'
	
	
*******************************************************************
	
#!/bin/bash

criar_pasta () {
DATA=`date +%Y%m%d-%k%M`
DIR_BACKUP=/backup/
VERI_DIR_BACKUP=`ls -l $DIR_BACKUP/backup-$DATA`

if [ $? = 2 ]; then

mkdir -p $DIR_BACKUP/backup-$DATA
chmod 0777 $DIR_BACKUP/backup-$DATA
echo "Criado diretótio $DIR_BACKUP/backup-$DATA"

else

echo " Diretório $DIR_BACKUP/backup-$DATA existe"

fi

}

criar_pasta
