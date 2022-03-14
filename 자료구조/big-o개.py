import time, random

def evaluate_n2(A, x):
	output=0
	for k in range(0,n,1):
		output+=A[k]*(x**k)
	return output

def evaluate_n(A, x):
    T=[]
    output=0
    T.append(1)
    for k in range(0,n,1):
        if k==1:
            T.append(x)
        elif k>1:
            T.append(T[k-1]*x)
        output+=A[k]*(T[k])
    return output


random.seed()
A=[]
n=int(input())
i=1
while i<=n:
  import random as rd
  A.append(rd.randint(-1000,1000))
  i+=1

x=(rd.randint(-1000,1000))

s_1 = time.process_time()
evaluate_n2(A,x)
e_1 = time.process_time()

s_2 = time.process_time()
evaluate_n(A,x)
e_2 = time.process_time()

print('수행시간=', e_1-s_1)
print('수행시간=', e_2-s_2)