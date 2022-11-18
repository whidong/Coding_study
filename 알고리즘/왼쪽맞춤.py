W = int(input())
words = input().split()
# code below
def calculate_penalty(A, W): # T(n) = 4k +1 
	penalty = 0 # 1hour
	for k in range(len(A)): #T(n) = 4k = O(k)
		penalty += (W - A[k])**3 # 4hour
	return penalty
wl = []
for i in range(len(words)):  #T(n) = 33n hour
	wl.append(len(words[i])) # 1hour
D = [[0 for i in range(0,len(wl))]for j in range(0,len(wl))]

for j in range(len(wl)):
  for k in range(j, len(wl)):
    if k==j:
      D[j][k] = (W - wl[k])**3
    elif k > j:
      a = 0
      for z in range(j, k+1):
        a += wl[z] + 1
      a -= 1
      if a > W:
        D[j][k] = None
      else:
        D[j][k] = (W-a)**3
point = [0 for _ in range(0,len(wl))]
penalty = [10000000 for q in range(0,len(wl))]
for m in range(len(wl)-1,-1,-1):
  for n in range(len(wl)-1,m,-1):
    if D[m][n] == None:
        pass
    else:
        penalty[m] = D[m][n]
        
a = 0
k = 0
while True:
  a += penalty[k]
  k = point[k]
  if k == len(point):
    break

