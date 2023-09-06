#!/bin/bash

#elimina y permiso de CDR_stadistica
sudo find /var/log/asterisk/cdr-csv/. -name '64*.csv' -type f -exec rm {} \;
sudo chmod 777 /var/log/asterisk/cdr-csv/Master-Mes*.csv

cd /root/asterisk
sudo rm /var/spool/asterisk/outgoing/*.call
sudo rm /var/spool/asterisk2/outgoing/*.call  

cd /var/www/asterisk-voicebot/ && forever start src/seeder_http.js && forever start src/daemon_http.js 

echo "Node Up!"