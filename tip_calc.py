bill = float(raw_input('Total bill amount?'))
service = raw_input('Level of service?(good, fair, bad )')


if service == 'good':
    tip = bill * 0.20

elif service == 'fair':
    tip = bill * 0.15

elif service == 'bad':
    tip = bill * 0.10

total = bill + tip

print 'The total price is %.2f  ' % total
split = int(raw_input('Split how many ways?'))

each_person = total / split


print 'Each person pays %.2f' % each_person
