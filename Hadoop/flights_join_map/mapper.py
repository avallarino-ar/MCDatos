#!/usr/bin/python3

# 2: JOIN entre archivos:  airlines.csv  y  flights.csv

# airlines.csv: IATA_CODE	AIRLINE
# airports.csv: IATA_CODE	AIRPORT	CITY	STATE	COUNTRY	LATITUDE	LONGITUDE
# flights.csv: 	YEAR	MONTH	DAY	DAY_OF_WEEK	AIRLINE	FLIGHT_NUMBER	TAIL_NUMBER	ORIGIN_AIRPORT	
#				DESTINATION_AIRPORT	SCHEDULED_DEPARTURE	DEPARTURE_TIME	DEPARTURE_DELAY	TAXI_OUT	
#				WHEELS_OFF	SCHEDULED_TIME	ELAPSED_TIME	AIR_TIME	DISTANCE	WHEELS_ON	TAXI_IN	
# 				SCHEDULED_ARRIVAL	ARRIVAL_TIME	ARRIVAL_DELAY	DIVERTED	CANCELLED	CANCELLATION_REASON
# 				AIR_SYSTEM_DELAY	SECURITY_DELAY	AIRLINE_DELAY	LATE_AIRCRAFT_DELAY	WEATHER_DELAY

import sys

for line in sys.stdin:
	cancel = "-"
	name = "zz"
	
	line = line.strip()
	splits = line.split(",")
	if len(splits) == 2:
		# De airlines.csv se obtiene Codigo y nombre de la aerolinea:
		code = splits[0]	# IATA_CODE
		name = splits[1]	# AIRLINE
		
	else: 
		# De flights.csv se obtiene Codigo y si el vuelo fue cancelado o no: 
		code = splits[4]	# AIRLINE
		cancel = splits[24]	# CANCELLED

	print( '%s\t%s\t%s' % (code, name, cancel)) 