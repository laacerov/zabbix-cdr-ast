#!/bin/bash

#elimina y permiso de CDR_stadistica
sudo rm find . -name '/var/log/asterisk/cdr-csv/64*.csv' -type f -delete
sudo chmod 777 /var/log/asterisk/cdr-csv/Master-Mes*.csv

cd /root/asterisk
sudo rm /var/spool/asterisk/outgoing/*.call
sudo rm /var/spool/asterisk2/outgoing/*.call  

cd /var/www/asterisk-voicebot/ && forever start src/seeder_http.js && forever start src/daemon_http.js 

echo "Node Up!"