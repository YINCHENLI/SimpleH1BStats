import sys
current_occupation = None
current_count= None
total = 0

for line in sys.stdin:
	line = line.strip()
	occupation, count = line.split('\t', 1)
	if occupation == '!TOTAL':
		total = count
		continue
	try:
		count = int(count)
	except ValueError:
		continue
	if current_occupation == occupation:
		current_count += count
	else:
		if current_occupation:
			per = float(current_count/int(total))
			percentage = "{:.1%}".format(per)
			print('%s;%s;%s' % (current_occupation, current_count, percentage))
		current_occupation = occupation
		current_count = count

if current_occupation == occupation:
	per = float(current_count/int(total))
	percentage = "{:.1%}".format(per)
	print('%s;%s;%s' % (current_occupation, current_count, percentage))