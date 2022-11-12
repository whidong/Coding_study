
def solve(L, S):
  B = [[1 for i in range(0,S)]for j in range(0,L)]
  if len(B[0]) >= 9:
    B[0][9] = 0
  for k in range(0,L):
    if len(B[k]) >= 9*(k+1) and k >= 1:
      B[k][9*k] = 0
    for t in range(1, S): 
      if t <= 9 and k >=1:
        B[k][t] = B[k][t-1] + B[k-1][t]
      elif t > 9 and k >=1:
        B[k][t] = B[k][t-1] + B[k-1][t] - B[k-1][t-10]
      else:
        if t <= 8:
          B[k][t] = 1
        else:
          B[k][t] = 0
  return B[L-1][S-1]


L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)

