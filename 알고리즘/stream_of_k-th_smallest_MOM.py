import heapq

A = list(map(int,input().split()))
H = []
j = []
m = 0
z = None

def find_median_five(A):
	for i in range(len(A)//2):
		heapq.heappop(A)
	return A[0]

def MoM(A, k):
	if len(A) == 1: 
		return A[0]
	i = 0
	S, M, L, medians = [], [], [], []
	while i+4 < len(A):
		medians.append(find_median_five(A[i: i+5]))
		i += 5
	if i < len(A) and i+4 >= len(A):
		medians.append(find_median_five(A[i:]))
	mom = MoM(medians, len(medians)//2)
	for v in A:
		if v < mom:
			S.append(v)
		elif v > mom:
			L.append(v)
		else:
			M.append(v)
	if len(S) >= k : return MoM(S, k)
	elif len(S)+len(M) < k: return MoM(L, k-len(S)-len(M))
	else: return mom

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
    if i > 400:
      r = MoM(D,t)
    else:
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

print(m)