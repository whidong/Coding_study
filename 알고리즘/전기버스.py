"""
A 도시는 전기 버스를 운행하려고 한다. 전기 버스는 한번 충전으로 이동할 수 있는
정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는
정류장 수가 k가 정해져 있다. 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을
해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오. 만약 충전기 설치가 잘못되어 종점에 도착할 수
없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전 횟수에는 포함하지 않는다.

"""

# 0 -> N번 정류장까지 한번 충전으로 이동할 수 있는 정류장 수 = k
# 충전기가 설치된 M개의 정류장 번호
# ex) 3 10 5 인 경우 

def countbus(K, N, M, charge):
  now = 0
  count = 0
  if charge[0] > K:
    return 0
  while True:
    for m in range(M):
      if charge[m] <= now + K:
        if m == M - 1:
          if charge[m-1] <= now + K:
            now = charge[m-1]
            count += 1
          else:
            return 0
      else:
        if charge[m-1] <= now + K:
          now = charge[m-1]
          count += 1
        else:
          return 0
    if now + K >= N:
      return count
    else:
      return 0
  

T = int(input())

for i in range(T):
  K, N, M = map(int, input().split())
  charge = list(map(int, input().split()))
  result = countbus(K, N, M, charge)
  print(f"#{i+1} {result}")
