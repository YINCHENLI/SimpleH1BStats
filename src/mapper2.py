import sys
import re

total = 0

for line in sys.stdin:
	line = line.strip()
	visas = line.split(";")
	#only count certified visa
	if visas[2] == 'CERTIFIED':
		total += 1
		#remove irrelavant character using pattern
		result = re.sub('[^a-zA-Z]', "", visas[-3])
		print('%s\t%s' %(visas[-3], 1))

#print !TOTAL, ! will make sure !TOTAL will comes first after sorting
print('%s\t%s' %("!TOTAL", total))