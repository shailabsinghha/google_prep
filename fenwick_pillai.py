###############################PROBLEM############################################################################################# 
#https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/tutorial/
from ss_pillai import *

ARR_MAX_VAL = 5*10**5
ARR_MAX_VAL = 13
PILLAI= [0] * (ARR_MAX_VAL+1)


def update(bit_arr,  bit_arr_len,   val, index):

	i = index
	while i< bit_arr_len:
		bit_arr[i]+=val
		i+=i&(-i)

def query(bit_arr, bit_arr_len,  index):
	
	_sum_=0
	i=index
	while i > 0:
		_sum_+=bit_arr[i]
		i-=i&(-i)
		
	return _sum_

################################ PPILLAI INIT HERE ###############################
for x in range(1, ARR_MAX_VAL+1):
	PILLAI[x]=pillai(x)
################################ PILLAI CLOSED HERE ###############################


arr_len = int(input())

ARR = [ int(x) for x in input().split()]

BIT_ARR = [0] * (arr_len+1)

QUERIES = int(input())

for i in range(1, arr_len+1):
	update(BIT_ARR, arr_len+1, PILLAI[ARR[i-1]], i)


for i in range(QUERIES):

	# print(f"BIT_ARR: {BIT_ARR}")

	q = [x for x in input().split()]

	if q[0] == 'C':

		print( query(BIT_ARR, arr_len+1, int(q[2])) - query(BIT_ARR, arr_len+1, int(q[1])-1) )

	else:
		update(BIT_ARR, arr_len+1, PILLAI[int(q[2])]- BIT_ARR[int(q[1])], int(q[1]))



