#!/bin/bash

criar_pasta_copia () {

DATA=`date +%Y%m%d-%H%m%S`
dir_original="/home/s3b4h/teste-rsync/"
copia="/backup/regnet/original/"
diferencial="/backup/$DATA/APP/$HOSTNAME-dif-$DATA"
DATAIN=`date +%c`
VERI_DIR_BACKUP=`ls -l $copia`

if [ $? = 2 ]; then

mkdir -p $copia
chmod 0777 $copia
echo "Criado diretótio $copia"

else

echo " Diretório $copia existe"

fi

}

bkp_diff() {
for x in `rsync -ac --out-format="%n"  $dir_original $copia`
do
if [ -d "$dir_original/$x" ]; then
mkdir -p "$diferencial/$x"

else
cp -frv $dir_original/$x $diferencial/$x

fi
done

if [ $? -eq 0 ] ; then

echo "-------------------------------------"
echo "Backup Diferencial concluído com sucesso"

DATAFIN=`date +%c`

echo "Data de termino: $DATAFIN"
echo "Backup realizado com sucesso" >> /var/log/backup_diferencial.log
echo "Criado pelo usuário: $USER" >> /var/log/backup_diferencial.log
echo "INICIO: $DATAIN" >> /var/log/backup_diferencial.log
echo "FIM: $DATAFIN" >> /var/log/backup_diferencial.log
echo "------------------------------------------------" >> /var/log/backup_difer                                                                                        encial.log
echo " "
echo "Log gerado em /var/log/backup_diferencial.log"

else

echo "ERRO! Backup Diferencial $DATAIN" >> /var/log/backup_diferencial.log


fi

}
criar_pasta_copia
bkp_diff

