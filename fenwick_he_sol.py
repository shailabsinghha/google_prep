MAXN = 10**6 + 5
MAXV = 5*10**5

# MAXN = 5
# MAXV = 6
MOD = 10**9 + 7

a=[0]*MAXN
phi=[0]*(MAXV + 5)
p=[0]*(MAXV + 5)
BIT=[0]*MAXN


def compute_phi():

	x=1
	while x<= MAXV:
		phi[x]=x
		x+=1

	
	for i in range(2, MAXV):


		if (phi[i] == i) : # prime number

			for j in range(i, MAXV):

				phi[j] -= (phi[j] // i)
                phi[j] = phi[j] % MOD
                j+=i



compute_phi()
print(phi)
        


