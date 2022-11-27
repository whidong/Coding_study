
def solve(L, S):
  B = [[1 for i in range(0,S)]for j in range(0,L)] # O(SL)hour
  if len(B[0]) >= 9: # 1hour
    B[0][9] = 0 # 1hour
  for k in range(0,L): # T(n) = 5L(12(S-1))hour = O(L(S-1))hour
    if len(B[k]) >= 9*(k+1) and k >= 1: # 4hour
      B[k][9*k] = 0 # 1hour
    for t in range(1, S): # T(n) = 12(S-1)hour = O(S-1)hour
      if t <= 9 and k >=1: # 2hour
        B[k][t] = B[k][t-1] + B[k-1][t] # 2hour 
      elif t > 9 and k >=1: # 2hour
        B[k][t] = B[k][t-1] + B[k-1][t] - B[k-1][t-10] # 3hour
      else:
        if t <= 8: # 1hour
          B[k][t] = 1 # 1hour
        else:
          B[k][t] = 0 # 1hour
  return B[L-1][S-1] 


L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)