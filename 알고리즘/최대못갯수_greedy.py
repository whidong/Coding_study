def heap_sort(A): # T(n) = 2nlogn + 4n + 1 hour = O(nlogn)
	n = len(A) # 1hour
	for k in range(n-1, -1, -1):  # nlogn hour
		heapify_down(A, k, n) # O(logn)
	for k in range(len(A)-1, -1, -1): # n(4 + logn)hour
		A[0],A[k] = A[k],A[0] # 2hour
		n = n - 1 # 2hour
		heapify_down(A, 0, n) # O(logn)

def heapify_down(A, k, n): #O(logn)
	while 2*k+1 < n:  #T(n) = 20logn hour
		L, R = 2*k + 1, 2*k + 2  # 6hour
		if L < n and A[L] > A[k]: # 3hour
			m = L # 1hour
		else:
			m = k # 1hour
		if R < n and A[R] > A[m]: # 3hour
			m = R # 1hour
		if m != k:  # 2hour
			A[k], A[m] = A[m], A[k] # 2hour
			k = m # 1hour
		else: break

def count_pin(A):
	count = 1 # 1hour
	pin = 0 # 1hour
	for i in range(len(A)): # T(n) = 4n = O(n)
		if pin == 0:
			pin = A[0][0] # 1hour
		if pin < A[i][1]:
			pin = A[i][0] # 1hour
			count += 1 # 2hour
	return count


n = int(input()) # 1hour
e = [] # 1hour
for i in range(n): # 3n hour
	a, b = map(int,input().split()) # 2hour
	e.append([b, a])  # 1hour
heap_sort(e) # O(nlogn)

print(count_pin(e)) # O(n)

#T(n) = nlogn + 3n + 5 hour = O(nlogn)
"""
최소 갯수의 못으로 모든 막대기를 한번씩 꽂기 위해서는 막대기를 오른쪽끝이 먼저 끝나는 순서대로 정렬하고 순서대로 첫번째로 오른쪽끝이 끝나는 부분보다 왼쪽끝이 작은 막대기들은 첫번쨰 오른쪽 끝에 못을 꽂았을때 같이 꽂힌다고 생각하면 된다. 
만약 왼쪽끝이 오른쪽 끝보다 작은 부분이 발생할 경우에는 왼쪽끝이 첫번째 오른쪽끝보다 큰 막대의 오른쪽끝 즉 첫번쨰 오른쪽 끝에 못을 꽂았을때 못이 꽂히지 않는 막대의 오른쪽 끝부터 다시 못이 박히는 막대기를 골라내고 이때 못의 갯수를 하나씩 카운트 하는 방식으로 구현했다. 
막대기를 정렬할때는 시간복잡도가 nlogn인 heap정렬을 이용하였다.
전체적인 시간복잡도는 막대기 정보가 담겨있는 리스트에서 오른쪽 끝이 빨리 끝나는 순서대로 정렬을 하기위해 사용한 heap정렬이 nlogn시간 걸렸고 막대가 어느지점에서 더이상 못에 꽂히지 않는지 탐색하는 과정이 n시간 소요되어 전체시간은 T(n) = nlogn + 3n + 5 hour 소요되었고 big-O로 나타내면 O(nlogn)시간이 소요되었다.

"""