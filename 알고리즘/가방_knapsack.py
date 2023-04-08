def fractional_knapsack(n, size, profit, K):
		# n개의 아이템, 크기 size[], 가치 profit[], 배낭의 현재 빈 공간 K
		if K <= 0 or n<=0:
			return 0
		s = 0
		p = 0
		for i in range(n):
				if s + size[i] <= K: # 배낭에 쏙 들어가면 전체 선택
						p += profit[i]
						s += size[i]
				else: # 넘치면 잘라서 선택
						p += (K-s) * (profit[i]/size[i])
						s += K-s
						break
		return p

def knapsack(i, size): # x[i]=1/0 결정. 배낭의 남은 크기 = size
		global MP, p, s
		if i >= n or size <= 0: # 배낭에 들어 있는 (선택한) 물건을 출력
				return
		# x[i] = 1을 따라가야하는지 결정
		x[i] = 1
		if itemw[i] <= size: # 아이템 i가 크기 제한을 넘지 않아야
				p += itemv[i]
				s += itemw[i]
				B = fractional_knapsack(n-(i+1), itemw[i+1:], itemv[i+1:] ,size-itemw[i])
				MP = max(MP, p)
				if p + B > MP:
						# Update MP
						knapsack( i+1, size-itemw[i] )
# x[i] = 0을 따라가야하는지 결정
		if itemw[i] <= size:
				p -= itemv[i]
				s -= itemw[i]
		x[i] = 0
		C = fractional_knapsack(n-(i+1), itemw[i+1:], itemv[i+1:], size)
		if p + B > MP:
				knapsack( i+1, size )

bagw = int(input())
n = int(input())
itemw = list(map(int,input().split()))
itemv = list(map(int,input().split()))
item = [(i, j) for i, j in zip(itemw, itemv)]
item = [] + list(sorted(item, key = lambda x : x[1] // x[0], reverse= True))
itemw, itemv = zip(*item)
itemw, itemv = list(itemw), list(itemv)
MP = 0
p = 0
s = 0
x = list(0 for i in range(n))
knapsack(0, bagw)
print(MP)
