
import re

def pprint(_type, mess ):
    if _type == 'mess':
        print '{From} ({Date}): {Subject}\n'.format(**mess)
    else:
        print '{From}: {Quantity}'.format(**mess)

f = open('mbox.txt', 'r')


print "="*40

# i = 19600;

mess = [{}]
from_quantity = {}

for line in f:
    # if i:
        # i= i - 1
        # print '-|- %s' % 
        # print line,
        # m = re.search(r"^From (\w+@[\w|\.]+)", line)
        # m = re.search(r"^From: ([\w|\.]+\@[\w|\.]+) (.+$)", line)
        # m = re.search(r"^(Date|From|Subject): ([\w|\.]+\@[\w|\.]+)", line)
    m = re.search(r"^(Date|From|Subject): (.+$)", line)
    if m:
        l = len(mess)
        if mess[-1].__contains__('From') and mess[-1].__contains__('Date') and mess[-1].__contains__('Subject'):
        # if len(mess[-1]) == 3:
            mess.append({m.groups()[0]: m.groups()[1]})
        else:
            mess[-1][m.groups()[0]] = m.groups()[1]

        if m.groups()[0] == 'From':
            if from_quantity.__contains__(m.groups()[1]):
                from_quantity[m.groups()[1]] += 1
            else:
                from_quantity[m.groups()[1]] = 1
    # else:
        # break

for m in mess:
    if len(m) == 3:
        pprint('mess', m)
    

print "="*40

for m in from_quantity:
    pprint('quantity', {
        'From': m, 
        'Quantity': from_quantity[m]
    })

print "="*40

print len(mess)
