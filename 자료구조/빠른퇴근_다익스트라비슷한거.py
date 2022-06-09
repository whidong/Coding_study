import sys
sys.setrecursionlimit(5000)

def DFS(G, v):
	global curr_time
	visited[v] = True
	curr_time += 1
	for i in G[v]:
		if visited[i] == False:
			DFS(G, i)
		parent[i].append(v)
	L.append(v)
	curr_time += 1
	
def DFSAll(G):
	for v in range(n-1, -1, -1):
		if visited[v] == False:
			DFS(G, v)
INF = -10000000
n = int(input())
m = int(input())
G = [[] for _ in range(n)]
D = [[INF]*n for _ in range(n)]
for _ in range(m):
	x, y, z= map(int, input().split())
	G[x].append(y)
	D[x][y] = z
for q in range(n):
	G[q].sort(reverse = True) 

visited = [False]*n
parent = [[] for _ in range(n)]
L = []
curr_time = 1

DFSAll(G)
K = list(reversed(L))

source = []
sink = []

for s in range(n):
	D[s][s] = 0 
	if not parent[s]:
		source.append(s)
	if not G[s]:
		sink.append(s)

result = []
dist = D
g = dict()
for i in range(n):
  g[i] = INF
gg = g
visit = [False]*n
def findgohome(x):
  if not parent[x]:
    gg[x] = 0
  for k in G[x]:
    if gg[k] == INF:
      gg[k] = dist[x][k] + gg.get(x)
    else:
      if gg.get(k) > dist[x][k] + gg.get(x):
        pass
      else:
        gg[k] = dist[x][k] + gg.get(x)
    if not G[k]:
      findgohome(k)
  return gg

  
for x in source:
  findgohome(x)
  for j in sink:
      result.append(gg.get(j))
  gg = g


print(K)
print(max(result))