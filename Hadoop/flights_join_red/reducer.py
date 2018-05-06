#!/usr/bin/python3
# @author: 2018 (c) Ariel Vallarino, Jorge Altamirano
# @description: JOIN entre archivos:  airlines.csv  y  flights.csv
# @license: GPL v2
import sys

lines = sys.stdin.readlines()
lines.sort()

previous = None
name_prev = None
sum = 0

print('IATA_CODE,AIRLINE,CANCEL_COUNT')

for line in lines:
    line = line.strip()
    line2 = line.split('\u00AC')
    #print("%s (%d)"% (line, len(line2)))
    if len(line2) == 1:
        sum += 1
    elif len(line2) == 2 and line2[0] != "IATA_CODE":
        print("%s\u00AC%s\u00AC%d"% (line2[0], line2[1], sum))
        sum = 0

