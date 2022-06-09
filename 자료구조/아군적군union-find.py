def union(v, w): #T = 9 hour = O(1)
	if v == w: #1 hour	
		return v
	if v.rank > w.rank: #1 hour
		v, w = w, v #2 hour
	if v.rank <= w.rank: #1 hour
		v.parent = w #1 hour
	if v.rank == w.rank: #1 hour
		w.rank += 1 #2 hour
	return w

def set_friends(x, y): #T = 2h + 39 hour = O(1)
	v, w = T.find(x), T.find(y) #2h hour
	k, j = None, None #2 hour
	if v == w: #1 hour
		return 
	if v.enermy != None: #1 hour
		k, k.enermy, v.enermy = v.enermy, None, None #3 hour
	if w.enermy != None: #1 hour
		j, j.enermy, w.enermy = w.enermy, None, None #3 hour
	a = union(v, w) #10 hour
	if j and k: #2 hour
		b = union(j, k) #10 hour
	elif j and k == None: #2 hour
		b = j #1 hour
	elif j == None and k: #2 hour
		b = k #1 hour
	else:
		return
	a.enermy = b #1 hour
	b.enermy = a #1 hour

def set_enemies(x, y):#T = 2h + 38 hour = O(1)
	v, w = T.find(x), T.find(y) #2h hour
	k, j = None, None #2 hour
	if v.enermy == w and w.enermy == v: #2 hour
		return
	if v.enermy != None:#1 hour
		k, k.enermy, v.enermy = v.enermy, None, None #3 hour
	if w.enermy != None:#1 hour
		j, j.enermy, w.enermy = w.enermy, None, None #3 hour
	if j != None: #1 hour
		a = union(v, j) #10 hour
	else:
		a = v #1 hour
	if k != None: #1 hour
		b = union(w, k) #10 hour
	else:
		b = w #1 hour
	a.enermy = b #1 hour
	b.enermy = a #1 hour
		
def are_friends(x, y):#T = 2h + 5 hour = O(1)
	v, w = T.find(x), T.find(y)#2h hour
	if v == w:#1 hour
		return True
	else:
		return False
def are_enemies(x, y):#T = 2h + 2 hour = O(1)
	v, w = T.find(x), T.find(y)#2h hour
	if v.enermy == w and w.enermy == v:#2 hour
		return True
	else:
		return False

n = int(input())#1 hour

class Node:
	def __init__(self, key):#T = 4 hour = O(1)
		self.key = key#1 hour
		self.parent = self#1 hour
		self.rank = 0#1 hour
		self.enermy = None#1 hour
class FOE:
	def __init__(self):#O(1)
		self.root = dict()
	def make_set(self,x):#O(1)
		return Node(x)
	def find(self, x):#O(h)
		v = self.root.get(x)#1 hour
		while v.parent != v:#h hour
			v = v.parent#1 hour
		return v
T=FOE()#1 hour
for i in range(n):#T = n hour = O(n)
	T.root[i] = T.make_set(i)#1 hour
"""
처음에 입력받은 사람의 수 n명 각각에 숫자를 부여하기 위해 for반복문으로 n번 반복하여 노드를 생성하여 부여된 번호를 저장한다. 각각의 노드를 파이썬의 딕셔너리를 이용한 해시테이블에 n개의 노드를 각각 연결하여 각노드에 O(1)시간에 접근할수 있도록 한다. 위의 과정까지 n개의 노드를 만드는 과정은 O(n)시간이 각 집단의 root노드를 찾는 find함수는 각집단의 높이인 h값만큼 반복하므로 O(h)시간이 나머지 과정은 모두 O(1)시간이 필요하다.

다음으로 각노드의 아군과 적군을 구별하는 과정에서 아군끼리는 union함수를 사용하여 하나의 집합으로 묶었고 적군관계는 각 아군 집단의 root노드가 적군 집단의 root노드를 적으로 가리키도록하여 구연하였다. sf와 se함수는 아군이나 적을 지정하는 과정에서 입력받은 x와 y값의 각 집단의 루트를 찾아야하므로 find함수를 2번사용한다. 따라서 수행시간은 각각 2h+39시간과 2h+28시간이 걸리고 둘다 O(h)시간이 걸린다. 마찬가지로 af와 ae함수도 root노드를 찾는 find함수를 사용해야하므로 수행시간은 각각 2h+5와 2h+2가 걸리고 O(h)시간이 걸린다. union함수의 경우 미리 찾아놓은 root노드를 입력받기 때문에 O(1)시간에 수행가능하다.
"""

while True:
    query, x, y = input().split()
    x, y = int(x), int(y)
    if query == 'sf':
        if are_enemies(x, y): # conflict, then print -1
            print(-1)
        else:
            set_friends(x, y)
    elif query == 'se':
        if are_friends(x, y):
            print(-1)
        else:
            set_enemies(x, y)
    elif query == 'af':
        if are_friends(x, y):
            print(1)
        else:
            print(0)
    elif query == 'ae':
        if are_enemies(x, y):
            print(1)
        else:
            print(0)
    elif query == 'exit':
        break
    else:
        print('not allowed operation')
