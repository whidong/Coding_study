n, k = map(int, input().split())
B = [list(map(int, input().split())) for j in range(n)]

def getsearch(A, s1, s2, e1, e2, k):
	if s1 == e1 and s2 == e2:
		i, j = s1, s2
		return onlyget(A, i, j, k)
	else:
		i = (e1+s1)//2
		j = (e2+s2)//2
	q = None
	if A[i][j] == k:
		q = (i, j)    
		return q
	elif A[i+1][j+1] == k:
		q = (i+1, j+1)
		return q
	elif A[i][j] > k:
		q = getsearch(A, s1, s2, i, j, k)
		if q != None:
			return q
		q = getsearch(A, s1, j+1, i, e2, k)
		if q != None:
			return q
		q = getsearch(A, i+1, s2, e1, j, k)
		if q != None:
				return q
	elif A[i+1][j+1] < k:
		q = getsearch(A, i+1, j+1, e1, e2, k)
		if q != None:
			return q
		q = getsearch(A, s1, j+1, i, e2, k)
		if q != None:
			return q
		q = getsearch(A, i+1, s2, e1, j, k)
		if q != None:
			return q
	elif k < A[i+1][j+1] or A[i][j] < k:
		q = getsearch(A, s1, j+1, i, e2, k)
		if q != None:
			return q
		q = getsearch(A, i+1, s2, e1, j, k)
		if q != None:
			return q

def onlyget(A, i, j, k):
	if A[i][j] == k:
		q = (i, j)    
		return q
	else:
		return None

a = getsearch(B, 0, 0, n-1, n-1, k)
if a == None:
	print((-1, -1))
else:
	print(a)
