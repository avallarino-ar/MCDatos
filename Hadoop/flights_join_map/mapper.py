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
    # Setting some defaults
	airline_code = " "
	airline = "zz"
	flight_nro = "-1"
	origin_airport = "-1"
	destination_airport = "-1"

	line = line.strip()
	splits = line.split(",")
	if len(splits) == 2: # Transactions have more columns than users
		airline_code = splits[0]
		airline = splits[1]
	else: 
		airline_code = splits[4]
		flight_nro = splits[5]
		origin_airport = splits[7]
		destination_airport = splits[8]

	print( '%s\t%s\t%s\t%s\t%s' % (airline_code, airline, flight_nro, origin_airport, destination_airport)) 