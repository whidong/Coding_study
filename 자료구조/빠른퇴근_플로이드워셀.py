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

def findgohome():
	dist = D
	for i in range(n):
		for e in range(n):
			for r in range(n):
				dist[e][r] = max(dist[e][i]+dist[i][r], dist[e][r])
	return dist # 시간복잡도가 너무큼 all to all말고 다익스트라(minheap)사용해서 다시 짜보자.
		

A = findgohome()
for l in source:
	for o in sink:
		result.append(A[l][o])
print(K)
print(max(result))













