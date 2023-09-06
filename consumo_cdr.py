# -*- coding: utf-8 -*-
  
import csv
from datetime import datetime, timedelta
import os
import subprocess

# Ruta al archivo CSV principal (Master.csv)
archivo_csv_principal = '/var/log/asterisk/cdr-csv/Master.csv'

# Obtener el primer día del mes actual en el formato deseado (YYYY-MM-DD)
primer_dia_mes_actual = datetime.now().replace(day=1).strftime('%Y-%m-%d')

# Calcular el último día del mes actual
ultimo_dia_mes_actual = datetime.now().replace(day=1) + timedelta(days=32) - timedelta(days=1)
ultimo_dia_mes_actual = ultimo_dia_mes_actual.strftime('%Y-%m-%d')

# Ruta al archivo CSV de salida para el CDR del mes actual
archivo_csv_mes_actual = '/var/log/asterisk/cdr-csv/Master-Mes-{}.csv'.format(datetime.now().strftime('%Y-%m'))

# Crear una cadena que contiene la fila de encabezado
encabezado = "accountcode;src;dst;dcontext;clid;channel;dstchannel;lastapp;lastdata;start;answer;end;duration;billsec;disposition;amaflags;Uniqueid\n"

# Abrir el archivo CSV principal en modo lectura y el archivo de salida en modo escritura
with open(archivo_csv_principal, mode='r') as entrada, open(archivo_csv_mes_actual, mode='w') as salida:
    # Crear un lector CSV para el archivo de entrada
    reader = csv.reader(entrada, delimiter=',', quotechar='"')

    # Crear un escritor CSV para el archivo de salida
    writer = csv.writer(salida, delimiter=';', quoting=csv.QUOTE_MINIMAL)

    # Escribir la fila de encabezado en el archivo de salida
    writer.writerow(encabezado.strip().split(';'))

    # Inicializar el total de consumo en segundos
    consumo_total_mes = 0

    # Leer las filas del archivo principal, filtrar las del mes actual y escribirlas en el archivo de salida
    for fila in reader:
        fecha_inicio = fila[9]  # Obtener la fecha de inicio del registro

        # Verificar si la fecha de inicio está dentro del mes actual
        if primer_dia_mes_actual <= fecha_inicio <= ultimo_dia_mes_actual:
            # Escribir la fila en el archivo de salida
            writer.writerow(fila)

            # Sumar el billsec al total de consumo del mes en segundos
            consumo_total_mes += int(fila[13])

# Calcular el consumo total del mes en minutos y segundos
minutos, segundos = divmod(consumo_total_mes, 60)

print("Se ha creado el archivo {} con la fila de encabezado.".format(archivo_csv_mes_actual))
print("Consumo total del mes en curso ({} - {}): {} minutos y {} segundos".format(primer_dia_mes_actual, ultimo_dia_mes_actual, minutos, segundos))