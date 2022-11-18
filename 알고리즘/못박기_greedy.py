def heap_sort(A):
	n = len(A)
	for k in range(n-1, -1, -1): 
		heapify_down(A, k, n)
	for k in range(len(A)-1, -1, -1):
		A[0],A[k] = A[k],A[0]
		n = n - 1 
		heapify_down(A, 0, n)

def heapify_down(A, k, n):
	while 2*k+1 < n: 
		L, R = 2*k + 1, 2*k + 2 
		if L < n and A[L] > A[k]:
			m = L
		else:
			m = k
		if R < n and A[R] > A[m]:
			m = R
		if m != k: 
			A[k], A[m] = A[m], A[k]
			k = m
		else: break
	
def count_pole(A, E, s, f):
	count = 0
	maxq = 0
	k, j = 0, 0
	for i in range(s, f+1):
		if i == A[k]:
			while i == A[k]:
				count += 1
				k += 1
				if count > maxq:
					maxq = count
				if k > len(A)-1:
					k -= 1
					break
		if i == E[j]:
			while i == E[j]:
				count -= 1
				j += 1
				if j > len(E)-1:
					j -= 1
					break
	return maxq

n = int(input())
q = []
e = []
for i in range(n):
	a, b = map(int,input().split())
	q.append(a)
	e.append(b)
heap_sort(q)
heap_sort(e)
k = count_pole(q, e, q[0] ,e[n-1])
print(k)