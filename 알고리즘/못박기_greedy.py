def heap_sort(A): # T(n) = 2nlogn + 4n + 1 hour = O(nlogn)
	n = len(A) # 1hour
	for k in range(n-1, -1, -1):  # nlogn hour
		heapify_down(A, k, n) # O(logn)
	for k in range(len(A)-1, -1, -1): # n(4 + logn)hour
		A[0],A[k] = A[k],A[0] # 2hour
		n = n - 1 # 2hour
		heapify_down(A, 0, n) # O(logn)

def heapify_down(A, k, n): #O(logn)
	while 2*k+1 < n: #T(n) = 20logn hour
		L, R = 2*k + 1, 2*k + 2  # 6hour
		if L < n and A[L] > A[k]: # 3hour
			m = L # 1hour
		else:
			m = k # 1hour
		if R < n and A[R] > A[m]: # 3hour
			m = R # 1hour
		if m != k: # 2hour
			A[k], A[m] = A[m], A[k] # 2hour
			k = m # 1hour
		else: break
	
def count_pole(A, E, s, f): # T(n) = 18cn + 4 hour = O(n) =(n) hour
	count = 0 # 1hour
	maxq = 0 # 1hour
	k, j = 0, 0 # 2hour
	for i in range(s, f+1): # T(n) = 18n(logn) hour
		if i == A[k]: 
			while i == A[k]: # T(n) = 10c hour 
				count += 1 # 2hour
				k += 1 # 2hour
				if count > maxq: # 1hour
					maxq = count # 1hour
				if k > len(A)-1: # 2hour
					k -= 1 # 2hour
					break
		if i == E[j]: 
			while i == E[j]: # T(n) = 8c hour
				count -= 1 # 2hour
				j += 1 # 2hour
				if j > len(E)-1: # 2hour
					j -= 1 # 2hour
					break
	return maxq

n = int(input()) # 1hour
q = [] # 1hour
e = [] # 1hour
for i in range(n): # 3n hour
	a, b = map(int,input().split()) # 2hour
	q.append(a) # 1hour
	e.append(b) # 1hour
heap_sort(q) # O(nlogn)
heap_sort(e) # O(nlogn)
k = count_pole(q, e, q[0] ,e[n-1]) # O(n)
print(k)

# T(n) = 2nlogn + 4n + 3 hour = O(nlogn)

"""
막대의 오른쪽끝과 왼쪽 끝을 정렬하여 제일 작은 왼쪽끝부터 제일큰 오른쪽끝까지 한번 탐색을 진행하면서 왼쪽끝점에 닿으면 +1을 오른쪽 끝점에 닿으면 -1을 하는 방식으로 가장 많이 +가 된 부분을 찾아낸다.

이떄 정렬은 수행시간이 n(logn)이 나오는 heap정렬을 이용하였고 탐색을 진행하면서 걸치는 막대의 갯수를 카운팅하는 수행시간의 경우 처음부터 끝까지 한번만 탐색하는 작업을 진행하기 떄문에 O(n)의 수행시간이 소요된다. 
따라서 전체적인 수행시간의 경우 (n) = 2nlogn + 4n + 3 hour = O(nlogn)으로 nlogn시간에 모든 작업을 끝낼 수 있다.

"""