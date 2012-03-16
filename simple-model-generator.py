import fileinput
from simplejson import loads
from itertools import imap, ifilter

busines_avg = {}
for record in ifilter(lambda r: r['type']=='business', imap(loads, fileinput.input())):
	busines_avg[record['business_id']] = record['stars']

print "model = %r" % busines_avg
