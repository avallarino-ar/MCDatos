#!/usr/bin/python3

# 2: JOIN entre archivos:  airlines.csv  y  flights.csv

# airlines.csv: IATA_CODE	AIRLINE
# airports.csv: IATA_CODE	AIRPORT	CITY	STATE	COUNTRY	LATITUDE	LONGITUDE
# flights.csv: 	YEAR	MONTH	DAY	DAY_OF_WEEK	AIRLINE	FLIGHT_NUMBER	TAIL_NUMBER	ORIGIN_AIRPORT	
#				DESTINATION_AIRPORT	SCHEDULED_DEPARTURE	DEPARTURE_TIME	DEPARTURE_DELAY	TAXI_OUT	
#				WHEELS_OFF	SCHEDULED_TIME	ELAPSED_TIME	AIR_TIME	DISTANCE	WHEELS_ON	TAXI_IN	
# 				SCHEDULED_ARRIVAL	ARRIVAL_TIME	ARRIVAL_DELAY	DIVERTED	CANCELLED	CANCELLATION_REASON
# 				AIR_SYSTEM_DELAY	SECURITY_DELAY	AIRLINE_DELAY	LATE_AIRCRAFT_DELAY	WEATHER_DELAY

output = list();
airlines_csv = 'airlines.csv'

# Cargo archivo de aerolineas:
airlines = {}
list_file = open(airlines_csv)
list_dm = set(line.strip() for line in list_file)
list_file.close()

# Paso SET a DICT:
for item in list_dm:
    splits = item.split(",")
    code = splits[0]
    name = splits[1]
    airlines[code] = name

import sys
for line in sys.stdin:
	# Elimino espacios
	line = line.strip()	
	# Separo campos por ",":
	splits = line.split(",")

	# De flights.csv se obtiene Codigo y si el vuelo fue cancelado o no: 
	code = splits[4]			# AIRLINE
	name = airlines.get(code) 	# Nombre de la aerolinea
	cancel = splits[24]			# CANCELLED
	if cancel.strip() == "1":		
		print("{}\t{}\t{}".format(code, name, cancel))