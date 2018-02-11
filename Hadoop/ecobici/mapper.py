#!/usr/bin/python

import sys
import re
 
for line in sys.stdin:
	words = re.split(',', line)
	print(words[13] + "\t1")
