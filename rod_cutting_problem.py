
"""Rod Cutting Problem"""
def rod_cutting(p, n):
	def memorize_cut_rod_aux(p,n,r,s):
		if r[n]>=0:
			return r[n]
		if n==0:
			return 0
		else:
			q = float('-inf')
			for i in xrange(1,n):
				if q < p[i]+memorize_cut_rod_aux(p, n-1, r, s):
					q = p[i]+memorize_cut_rod_aux(p, n-1, r, s)
					s[n] = i
				q = max(q, p[i]+memorize_cut_rod_aux(p, n-1, r, s))
			r[n] = q
		return q				

	def memorize_cut_rod(p,n):
		r = [float('-inf')]*n
		s = [float('-inf')]*n
		max_rev, pices = memorize_cut_rod_aux(p,n-1,r,s)
		return max_rev, pices

	return memorize_cut_rod(p, n)

def test_case():
	p = [1,5,8,9,10,17,17,20,24,30]
	max_rev, pices = rod_cutting(p, len(p))
	print "Max rev:{}, pices: {}".format(max_rev, pices) 

if __name__=='__main__':
	test_case()



