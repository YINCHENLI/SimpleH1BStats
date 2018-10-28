import sys
import re
total = 0

for line in sys.stdin:
	line = line.strip()
	visas = line.split(";")
	if visas[2] == 'CERTIFIED':
		total += 1
		result = re.sub('[^a-zA-Z]', "", visas[-3])
		print('%s\t%s' %(visas[-3], 1))

print('%s\t%s' %("!TOTAL", total))