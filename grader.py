"""
Functions needed to evaluate hypothises
"""

from truth import truth
from itertools import imap

def build_hypothesis(records):
	return dict((r['review_id'], r['stars']) for r in records)

def rmse(hypothesis):
	"""Find Root Mean Squared Error for a hypothesis.  hypothese is a dict of
	(user_id, business_id) to star rating."""

	def sq_err((key, real)):
		if hypothesis.get(key):
			return (float(hypothesis[key])-real)**2
		else:
			return 4**2 # 4 is maximum error

	return (sum(imap(sq_err, truth.iteritems()))/float(len(truth)))**0.5
