#!/usr/bin/env python
  
# Exec: 
# cat /Volumes/sd_avallarino/tareas/MGE/flights/airlines.csv /Volumes/sd_avallarino/tareas/MGE/flights/flights_50.csv | python3 flights_map.py | sort | python3 flights_reduce.py  

import sys
  
current_airline_code = "-1"
current_airline = "-1"
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
     
    # parse the input we got from mapper.py
    airline_code, airline, flight_nro, origin_airport, destination_airport = line.split("\t")
     
    if flight_nro == "-1": #this is a new flight 
        current_airline_code = airline_code
        current_airline = airline
        
    else:
    	print( '%s\t%s\t%s\t%s\t%s' % (current_airline_code, current_airline, flight_nro, origin_airport, destination_airport)) 
