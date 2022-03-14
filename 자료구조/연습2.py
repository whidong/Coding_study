import time, random

def prefixSum1(X, n):
	output =[]
	for k in range(0,n,1):
		output.append(0)
		for j in range(0,k+1,+1):
			output[k]+=X[j]
	return output

def prefixSum2(X,n):
	out_put=[]
	for k in range(0,n,1):
		out_put.append(0)
		if k<1:
			out_put[k]+=X[k]
		else:
			out_put[k]+=out_put[k-1]+X[k]
	return out_put


random.seed()
X=[]
n=int(input())
i=1
while i<=n:
  import random as rd
  X.append(rd.randint(-999,999))
  i+=1

before1= time.process_time()
c=prefixSum1(X,n)
after1= time.process_time()
a=(after1-before1)

before2= time.process_time()
d=prefixSum2(X,n)
after2= time.process_time()
b=(after2-before2)

print(a)
print(b)
