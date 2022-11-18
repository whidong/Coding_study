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

def count_pin(A):
	count = 1
	pin = 0
	for i in range(len(A)):
		if pin == 0:
			pin = A[0][0]
		if pin < A[i][1]:
			pin = A[i][0]
			count += 1
	return count


n = int(input())
e = []
for i in range(n):
	a, b = map(int,input().split())
	e.append([b, a])
heap_sort(e)

print(count_pin(e))
