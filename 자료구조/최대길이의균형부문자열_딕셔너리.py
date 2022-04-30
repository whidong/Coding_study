def solve(A):
	H = dict()
	a, b , d = 0, 0, 0
	for i in range(len(A)):
		if A[i] == '0':
			a += 1
		else:
			b += 1
		m = a-b
		if m not in H:
			H[m] =[i+1,None]
		else:
			H[m][1] = i
	for loop in H.keys():	
		if loop == 0:
			k = H.get(loop)[1]+1
		if H.get(loop)[1]==None:
			continue
		if loop != 0:
			k = H.get(loop)[1]+1-H.get(loop)[0]
		if d < k:
			d = k
	return d
A = input().strip()
print(solve(A))