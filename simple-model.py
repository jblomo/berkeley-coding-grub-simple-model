import fileinput
from itertools import imap
from simplejson import loads, dumps

from hypothesis import model

for record in imap(loads, fileinput.input()):
	hyp = {'review_id': record['review_id'], 'stars': model[record['business_id']]}
	print dumps(hyp)
