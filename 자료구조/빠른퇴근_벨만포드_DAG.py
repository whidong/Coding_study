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
dist = dict()
for i in range(n):
	dist[i] = INF
	if not parent[i]:
		dist[i] = 0
def relax(u,v):
	if dist[v] < dist[u] + D[u][v]:
		dist [v] = dist[u] + D[u][v]

def findgohome():
	for i in K:
		for j in G[i]:
			p = parent[j]
			if dist[j] < dist[i] + D[i][j]:
				relax(i, j)
	return


findgohome()
for j in sink:
	result.append(dist.get(j))

print(max(result))