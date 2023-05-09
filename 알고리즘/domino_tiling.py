def solution(n):
  dp=[0 for i in range(n)]
  B = [0 for j in range(n+2)]
  dp[0], dp[1] = 1, 2
  B[0],B[1] = 0, 1
  for x in range(2,n):
    B[x] = B[x-1] + dp[x-2]
    dp[x] = dp[x-1]+dp[x-2]+2*B[x-1]
  print(dp)
  return dp[n-1]
n=int(input())
dp = solution(n)
print(dp)