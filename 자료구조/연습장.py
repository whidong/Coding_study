def solve(n):
  c =0
  while n >0:
    n = n-(n and -n)
    c += 1
  return c
print(solve(8))
