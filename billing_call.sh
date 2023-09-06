#!/bin/sh
# Version 1.0

METRIC="$1"

if [ -z "$1" ]; then
    echo "Please specify a metric"
    exit 1
fi

case $METRIC in

        'm_mes')       python /var/log/asterisk/cdr-csv/consumo_cdr.py | grep minutos | cut -d ':' -f2 | awk '{print $1}' ;;
        'm_dia')       python /var/log/asterisk/cdr-csv/dia_cdr.py | grep minutos | cut -d ':' -f2 | awk '{print $1}';;


    *)  echo "Not selected metric"
        exit 0
        ;;
esac