#!/usr/bin/python3

# 2: JOIN entre archivos:  airlines.csv  y  flights.csv

import sys
  
current_airline_code = ""
current_airline = ""

lines = sys.stdin.readlines()           
lines.sort()

output = list();

# Cabeceras:
header = ("CODE\tAIRLINE\tYEAR\tMONTH\tDAY\tDAY_OF_WEEK\tFLIGHT_NUMBER" +
"TAIL_NUMBER\tORIGIN_AIRPORT\tDESTINATION_AIRPORT\tSCHEDULED_DEPARTURE" +
"DEPARTURE_TIME\tDEPARTURE_DELAY\tTAXI_OUT\tWHEELS_OFF\tSCHEDULED_TIME" +
"ELAPSED_TIME\tAIR_TIME\tDISTANCE\tWHEELS_ON\tTAXI_IN\tSCHEDULED_ARRIVAL" +
"ARRIVAL_TIME\tARRIVAL_DELAY\tDIVERTED\tCANCELLED\tCANCELLATION_REASON" +
"AIR_SYSTEM_DELAY\tSECURITY_DELAY\tAIRLINE_DELAY\tLATE_AIRCRAFT_DELAY\tWEATHER_DELAY")
print(header)

# input comes from STDIN
for line in lines:

    # Elimino espacios
	line = line.strip()
     
    # Separo campos por TAB
	splits = line.split("\t")
	if len(splits) == 3:
		# Obtengo codigo de la aerolinea
		current_airline_code = splits[1]
		# Obtengo Nombre 
		current_airline = splits[2]
		
	else:
		# Asigno codigo de la aerolinea
		output.append(current_airline_code)
		# Obtengo Nombre 
		output.append(current_airline)
		# Agrego el resto de los campos para generar la salida
		output[2:len(splits)] = splits[2:len(splits)]   
		# Salida:
		print('\t'.join(output))

	output = []

