import heapq

A = list(map(int,input().split()))
H = []
j = []
m = 0

for i in range(0,len(A)):
    B = A[:i+1]
    heapq.heapify(B)
    t = i//3
    for k in range(t+1):
        j = heapq.heappop(B)
    m += j
print(m)

for i in range(0,len(A)):
    heapq.heappush(H, A[i])
    t = i//3
    for k in range(t+1):
        j.append(heapq.heappop(H))
    r = j[t]
    for _ in range(len(j)):
        heapq.heappush(H, j.pop())
    m += r

for i in range(0,len(A)):
		heapq.heappush(H, A[i])
		t = i//3
		if t >= 2:
			for i in range(2,t+1):
				j.append(heapq.heappop(H))
			if H[1] < H[2]:
				r = H[1]
			else:
				r = H[2]
			for _ in range(len(j)):
				heapq.heappush(H, j.pop())
		else:
			if t == 1:
				if H[1] < H[2]:
					r = H[1]
				else:
					r = H[2]
			else:
				r = H[0]
		m += r
		
print(m)

for i in range(0,len(A)):
	heapq.heappush(H, A[i])
	t = i//3
	if t == 0:
		r = H[0]
	elif t == 1:
		if H[1] < H[2]:
			r = H[1]
		else:
			r = H[2]
	else:
		D = H[0:]
		if i%3 == 0 or r > A[i]:
			z = None

		if z == None:
			for _ in range(t-1):
				heapq.heappop(D)
			if D[1] < D[2]:
				z = D[1]
			else:
				z = D[2]	
			r = z
		elif z < A[i] and i%3 != 0:
			r = z
	m += r
