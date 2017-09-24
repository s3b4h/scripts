#!/bin/bash
echo "Backup full"

# criação da pasta
criar_pasta () {
DATA=`date +%Y%m%d`
DIR_BACKUP=/backup
VERI_DIR_BACKUP=`ls -l $DIR_BACKUP/backup-full-$DATA`

if [ $? = 2 ]; then

mkdir -p $DIR_BACKUP/backup-full-$DATA
chmod 0777 $DIR_BACKUP/backup-full-$DATA
echo "Criado diretótio $DIR_BACKUP/backup-full-$DATA"

else

echo " Diretório $DIR_BACKUP/backup-full-$DATA existe"

fi

}

dadosfull() {

SRCDIR="/home/s3b4h/teste" #diretórios que serão feito backup
DSTDIR=$DIR_BACKUP/backup-full-$DATA #diretório de destino do backup
DATA=`date +%x-%k%M%S` #pega data atual

#criar o arquivo full-data.tar no diretório de destino
ARQ=$DSTDIR/$HOSTNAME-full-$DATA.tar.gz
#data de inicio backup
DATAIN=`date +%c`
echo "Data de inicio: $DATAIN"

}

backupfull() {
sync
tar -cvf $ARQ $SRCDIR

if [ $? -eq 0 ] ; then
echo "----------------------------------------"
echo "Backup Full concluído com Sucesso"
DATAFIN=`date +%c`
echo "Data de termino: $DATAFIN"
echo "Backup realizado com sucesso" >> /var/log/backup_full.log
echo "Criado pelo usuário: $USER" >> /var/log/backup_full.log
echo "INICIO: $DATAIN" >> /var/log/backup_full.log
echo "FIM: $DATAFIN" >> /var/log/backup_full.log
echo "-----------------------------------------" >> /var/log/backup_full.log
echo " "
echo "Log gerado em /var/log/backup_full.log"
else
echo "ERRO! Backup do dia $DATAIN" >> /var/log/backup_full.log
fi
}

criar_pasta
dadosfull
backupfull