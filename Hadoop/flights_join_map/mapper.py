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

import sys
for line in sys.stdin:
	
	# Elimino espacios
	line = line.strip()	
	# Separo campos por ",":
	splits = line.split(",")
	if len(splits) == 2:		
		# Genero key con la cual se ordenarán los datos:
		output = [splits[0]  + "1"]
		# Agrego campos a continuación del Key:
		output[1:len(splits)] = splits		
		# Genero salida con campos separados por TAB:
		print('\t'.join(output))			

	else:						
		# Genero key con la cual se ordenarán los datos
		output = [splits[4] + "2"]			
		# Agrego código al inico:
		output.append(splits[4])			
		# Elimino codigo:
		del splits[4]						
		# Agrego campos a continuación del Key:
		output[2:len(splits)] = splits   	
		# Genero salida con campos separados por TAB:
		print('\t'.join(output))			

	output = []