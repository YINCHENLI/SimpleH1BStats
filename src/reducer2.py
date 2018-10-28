import sys

current_state = None
current_count= None
total = 0

for line in sys.stdin:
	line = line.strip()
	state, count = line.split('\t', 1)
	if state == '!TOTAL':
		total = count
		continue
	try:
		count = int(count)
	except ValueError:
		continue
	if current_state == state:
		current_count += count
	else:
		if current_state:
			per = float(current_count/int(total))
			percentage = "{:.1%}".format(per)
			print('%s;%s;%s' % (current_state, current_count, percentage))
		current_state = state
		current_count = count

if current_state == state:
	per = float(current_count/int(total))
	percentage = "{:.1%}".format(per)
	print('%s;%s;%s' % (current_state, current_count, percentage))