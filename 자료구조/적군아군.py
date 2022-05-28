#
# 4개의 연산 함수 코드 등
#
def union(v, w):
	if v == w:
		return w
	if v.rank > w.rank:
		v, w = w, v
	if v.rank <= w.rank:
		v.parent = w
	if v.rank == w.rank:
		w.rank += 1
	return w

def set_friends(x, y):
	if x == y:
		return
	v, w = T.find(x), T.find(y)
	k, j = None, None
	if v == w:
		return print(-1)
	if v.enermy != None:
		k, k.enermy, v.enermy = v.enermy, None, None
	if w.enermy != None:
		j, j.enermy, w.enermy = w.enermy, None, None
	a = union(v, w)
	if j and k: 
		b = union(j, k)
	elif j and k == None:
		b = j
	elif j == None and k:
		b = k
	else:
		return
	a.enermy = b
	b.enermy = a

def set_enemies(x, y):
	v, w = T.find(x), T.find(y)
	k, j = None, None
	if v.enermy == w and w.enermy == v:
		return
	if v.enermy != None:
		k, k.enermy, v.enermy = v.enermy, None, None
	if w.enermy != None:
		j, j.enermy, w.enermy = w.enermy, None, None
	if j:
		a = union(v, j)
	else:
		a = v
	if k:
		b = union(w, k)
	else:
		b = w
	a.enermy = b	
	b.enermy = a 
		
def are_friends(x, y):
	v, w = T.find(x), T.find(y)
	if v == w:
		return True
	else:
		return False
def are_enemies(x, y):
	v, w = T.find(x), T.find(y)
	if v.enermy == w and w.enermy == v:
		return True
	else:
		return False

n = int(input())
#
# 필요한 자료구조 정의
#
class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self
		self.rank = 0
		self.enermy = None
class FOE:
	def __init__(self):
		self.root = dict()  
	def make_set(self,x):  
		return Node(x)
	def find(self, x):
		v = self.root.get(x)
		while v.parent != v:
			v = v.parent
		return v
T=FOE()
for i in range(n):
	T.root[i] = T.make_set(i)

# 아래 코드는 가능하면 고치지 말 것!
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