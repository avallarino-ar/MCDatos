#!/usr/bin/python3

# 2: JOIN entre archivos:  airlines.csv  y  flights.csv

import sys
  
lines = sys.stdin.readlines()          
lines.sort()                

previous = None
name_prev = None
sum = 0

print( 'CODE\tAEROLINEA\tCANT.CANCELACIONES') 

# Para cada aerolinea se cuenta cuantos vuelos canceladso tuvo 
for line in lines:

	code, name, cancel = line.split('\t') 
	if code != previous:
		if previous is not None:      	
			print(previous + '\t' + name_prev + '\t' + str(sum))     
		previous = code    
		name_prev = name 
		sum = 0

	valor = cancel.strip()
	if valor != "-":
		valor = int(valor)
	if valor == 1:
		sum += valor

# Retorna nombde de la aerolinea y cantidad de vuelos cancelados
print(code + '\t' + name_prev + '\t' + str(sum))   