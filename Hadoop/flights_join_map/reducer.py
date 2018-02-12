#!/usr/bin/python3

# 2: JOIN entre archivos:  airlines.csv  y  flights.csv

import sys
  
lines = sys.stdin.readlines()           
lines.sort()                

previous = None
name_prev = None
sum = 0

print( 'AEROLINEA\tCANT.CANCELACIONES') 

# Para cada aerolinea se cuenta cuantos vuelos canceladso tuvo 
for line in lines:

  code, name, cancel = line.split('\t') 
  if code != previous:
      if previous is not None:      	
      	print(name_prev + '\t' + str(sum))     
      previous = code    
      name_prev = name 
      sum = 0

  if cancel.strip() == "1":
  	sum += 1

# Retorna nombde de la aerolinea y cantidad de vuelos cancelados
print(name_prev + '\t' + str(sum))    	