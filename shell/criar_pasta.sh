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
