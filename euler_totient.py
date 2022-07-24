def phi(x):	
	p=2
	res = x
	while (p*p <= x):

		if x%p==0:

			while x%p==0:
				x=x//p

			res = res* (1.0 - (1.0 / float(p)))

		p+=1

	if(x > 1):
		res = res *(1.0 - (1.0 / float(x)))

	# EULER_TOIENT[x]=int(res)
	return int(res)
