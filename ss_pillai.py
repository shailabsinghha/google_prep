from euler_totient import *
def pillai(n):
	# since divsors can exists within the range of sqrt of the number

	res = 0

	x=1

	while x*x <= n:

		if n % x ==0: # this is a divisor

			d1 = x
			d2 = n//x

			# we can calcuate for the both of the side for this function

			res +=d1*phi(n//d1)

			if d1!=d2:
				res +=d2*phi(n//d2)
	

		x+=1

	return res		

	# leaving the edge case for now