import heapq

def sumall_kth(A) : #T(n) = 6nlogn + 7n + 4
	mx ,mn= [], [] # 2hour
	result, count = 0, 0 # 2hour
	for i in A: # n hour
		k = count//3+1 # 3hour
		if not mx or -mx[0] >= i:
			heapq.heappush(mx, -i) # log(n)hour
		else:
			heapq.heappush(mn, i) # log(n)hour
		if len(mx) > k:
			heapq.heappush(mn, -heapq.heappop(mx)) # 2log(n)hour
		elif len(mx) < k and mn:
			heapq.heappush(mx, -heapq.heappop(mn)) # 2log(n)hour
		if len(mx) >= k:
			result += -mx[0] # 2hour
		count += 1 # 2hour
	return result
A = list(map(int,input().split()))
print(sumall_kth(A))
"""
문제를 해결하면서 주어진 리스트A에서 m[i]값을 구해야되는 범위가 하나씩늘어나면서 동시에 더해야되는 수가 몇번째 작은수인가와 각숫자가 몇번째로 작은수인가가
계속해서 바뀌는 문제임을 파악했다. 이에 따라 k번째 숫자를 빠른 수행시간에 찾아낼 수 있는 Median of Medians알고리즘에서 중앙값을 찾아내는 과정을 생략하고
i값이 증가함에 따라 추가되는 리스트A의 값을 넣는 동시에 maxheap과 minheap을 동시에 사용하여 추가되는 숫자가 maxheap의 루트노드 보다 크다면 minheap에 넣고 작다면 maxheap에 넣은 다음 구해야되는 k번째 숫자와 max힙의 길이를 비교해서 k가 max힙보다 길다면 maxheap의 값을 pop하여 minheap에 넣고 짧다면 minheap의 값을 pop하여 maxheap에 넣어 maxheap의 루트노드가 k번째 숫자가 되도록하여 k번째 숫자를 바로 반환하는 형태로 구현하였다.

각각의 heappush와 heappop연산자는 O(logn)의 시간복잡도를 가지고 for반복문은 리스트 A의 길이만큼 반복하기 때문에 O(n)의 시간복잡도를 가진다.
따라서 T(n) = 6nlog(n) + 7n + 4의 수행시간을 가지게 되며 이를 Big-O로 나타내면 O(nlogn)의 시간복잡도를 가질것이다.
"""