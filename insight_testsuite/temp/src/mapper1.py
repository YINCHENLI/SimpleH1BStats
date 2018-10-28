import sys
import re

total = 0
for line in sys.stdin:
	line = line.strip()
	visas = line.split(";")
	if visas[2] == 'CERTIFIED':
		total += 1
		result = re.sub('[^0-9a-zA-Z,_\\s-]', "", visas[24]) 
		print('%s\t%s' % (result,1))
print('%s\t%s' % ("!TOTAL", total))