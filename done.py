
import re

    
def _pprint(_type, mess):
    if _type == 'mess':
        print '{From} ({Date}): {Subject}\n'.format(**mess)
    else:
        print '{From}: {Quantity}'.format(**mess)


def pprint(res):
    print "="*40
    for m in res['mess']:
        _pprint('mess', m)

    print "="*40
    for m in res['from_quantity']:
        _pprint('quantity', {
            'From': m, 
            'Quantity': res['from_quantity'][m]
        })

    print "="*40

    print 'Total: %s' % len(res['mess'])


def parseFile(filename):
    f = open(filename, 'r')

    mess = [{}]
    from_quantity = {}

    for line in f:

        m = re.search(r"^(Date|From|Subject): (.+$)", line)

        if m:
            l = len(mess)
            if mess[-1].__contains__('From') and mess[-1].__contains__('Date') and mess[-1].__contains__('Subject'):
                mess.append({m.groups()[0]: m.groups()[1]})
            else:
                mess[-1][m.groups()[0]] = m.groups()[1]

            if m.groups()[0] == 'From':
                if from_quantity.__contains__(m.groups()[1]):
                    from_quantity[m.groups()[1]] += 1
                else:
                    from_quantity[m.groups()[1]] = 1

    if len(mess[-1]) != 3:
        mess.__delitem__(len(mess)-1)

    return {
        'mess': mess,
        'from_quantity': from_quantity
    }


def run():
    res = parseFile('mbox.txt')
    pprint(res)

run()
