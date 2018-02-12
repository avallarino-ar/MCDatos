#!/usr/bin/python3

# 2: JOIN entre archivos:  airlines.csv  y  flights.csv

import sys
  
lines = sys.stdin.readlines()           
lines.sort()                

current_airline_code = "-1"
current_airline = "-1"

print( 'COD.\tAEROLINEA\tNRO.VUELO\tORIGEN\tDESTINO') 

# input comes from STDIN
for line in lines:
    # remove leading and trailing whitespace
    line = line.strip()
     
    # parse the input we got from mapper.py
    airline_code, airline, flight_nro, origin_airport, destination_airport = line.split("\t")
     
    if flight_nro == "-1": #this is a new flight 
        current_airline_code = airline_code
        current_airline = airline
        
    else:
    	print( '%s\t%s\t%s\t%s\t%s' % (current_airline_code, current_airline, flight_nro, origin_airport, destination_airport)) 
