class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0  # 높이 정보도 유지함에 유의!!

	def __str__(self):
		return str(self.key)

class BST:
	def __init__(self):
		self.root = None	
		self.size = 0
	def __len__(self):
		return self.size

	def preorder(self, v):
		if v != None:
			print(v.key, end =' ')
			self.preorder(v.left)
			self.preorder(v.right)

	def inorder(self, v):
		if v != None:
			self.inorder(v.left)
			print(v.key, end =' ')
			self.inorder(v.right)
	def postorder(self, v):
		if v != None:
			self.postorder(v.left)
			self.postorder(v.right)
			print(v.key, end =' ')
	def find_loc(self, key):
		if self.size == 0:
			return None
		p = None
		v = self.root
		while v != None:
			if v.key == key:
				return v
			elif v.key < key:
				p = v
				v = v.right
			else:
				p = v
				v = v.left
		return p
	def search(self, key):
		p = self.find_loc(key)
		if p and p.key == key:
			return p
	def insert(self, key):
		p = self.find_loc(key)
		if p == None or p.key != key:
			v = Node(key)
			if p == None:
				self.root = v
			else:
				v.parent = p
				if p.height == v.height:
					p.height = v.height + 1
				if p.key >= key:
					p.left = v
				else:
					p.right = v
			m, n = p, v
			while m:
				if m.height == n.height:
					m.height = n.height + 1
				m, n = m.parent, m
			self.size += 1
			return v
		else:
			return None
	def deleteByMerging(self, x):
		a, b, pt = x.left, x.right, x.parent
		if a != None:
			c = m = a
			while m.right:
				m = m.right
			if b != None:
				b.parent = m
			m.right = b
			s = m
			f, k = None, m.right
			while k != a:
				f, k = k, k.parent
				if f.height >= k.height:
					k.height = f.height + 1
		else:
			c, s = b, pt
		if pt == None:
			if c:
				c.parent = None
			self.root = c
		else:
			if pt.left == x:
				pt.left = c
			else:
				pt.right = c
			if c:
				c.parent = pt
			if c.parent:
				f, k = c, c.parent
				if f.height >= k.height:
					while k:
						if f.height >= k.height:
							k.height = f.heighint + 1 #이부분 C값 위치찾은뒤 부모노드존재할때 높이값 수정하는 부분 여기서부터
						f, k = k, f.parent
		self.size -= 1
	def deleteByCopying(self, x):
		a, b, pt = x.left, x.right, x.parent
		if a == None and b == None:
			if x.parent == None:
				self.root = None
			else:
				if pt.left == x:
					pt.left = None	
				else:
					pt.right = None
			del x
		elif a:
			y = a
			while y.right:
				y = y.right
			x.key = y.key
			yp, d = y.parent, y.left
			if y.left:
				d.parent = y.parent
			if yp.left == y:
				yp.left = d
			else:
				yp.right = d
			del y
		elif b:
			y = b
			while y.left:
				y = y.left
			x.key = y.key
			yp, d = y.parent, y.right
			if y.right:
				d.parent = y.parent
			if yp.left == y:
				yp.left = d
			else:
				yp.right = d
			del y
		self.size -= 1
        # 노드들의 height 정보 update 필요

	def height(self, x): # 노드 x의 height 값을 리턴
		if x == None: return -1
		else: return x.height

	def succ(self, x):
		pt = x.parent
		if x.right == None:
			if pt == None:
				return None
			if pt.left == x:
				return pt
			if pt.right == x:
				if pt.parent:
					ppt = pt.parent
					if pt == ppt.left:
						return ppt
				return None
		p = None
		v = x
		if x.right:
			p = v
			v = v.right
		while v != None:	
				p = v
				v = v.left
		return p

	def pred(self, x):
		pt = x.parent
		if x.left == None:
			if x.parent == None or pt.left == x:
				return None
			return x.parent
		p = None
		v = x
		if x.left:
			p = v
			v = v.left
		while v != None:	
				p = v
				v = v.right
		return p

	def rotateLeft(self, x): 
		if x == None: 
			return
		z = x.right
		if z == None: 
			return
		b = z.left
		z.parent = x.parent
		if x.parent:
			if x.parent.right == x:
				x.parent.right = z
			else:
				x.parent.left = z
		else:
				self.root = z
		z.left = x
		x.parent = z
		if b: 
			x.right = b
			b.parent = x
			if x.left and b.height< x.left.height:
				x.height = x.left.height + 1
			else:
				x.height = b.height + 1
		else:
			x.right = None
			if x.left:
				x.height = x.left.height + 1
			else:
				x.height = 0
		if z.right:
			if x.height <= z.right.height:
				z.height = z.right.height + 1
			else:
				z.height = x.height + 1
		else:
			z.height = x.height + 1
		m, n = z.parent, z
		while m:
			if m.height == n.height:
				m.height = n.height + 1
			n, m = m, m.parent
				# 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)

	def rotateRight(self, x):
		if x == None: 
			return
		z = x.left
		if z == None:
			return
		b = z.right
		z.parent = x.parent
		if x.parent:
			if x.parent.left == x:
				x.parent.left = z
			else:
				x.parent.right = z
		else:
			self.root = z
		z.right = x
		x.parent = z
		if b: 
			x.left = b
			b.parent = x
			if x.right and b.height< x.right.height:
				x.height = x.right.height + 1
			else:
				x.height = b.height + 1
		else:
			x.left = None
			if x.right:
				x.height = x.right.height + 1
			else:
				x.height = 0
		if z.left:
			if x.height <= z.left.height:
				z.height = z.left.height + 1
			else:
				z.height = x.height + 1
		else:
			z.height = x.height + 1
		m, n = z.parent, z
		while m:
			if m.height == n.height:
				m.height = n.height + 1
			n, m = m, m.parent
		
			# 균형이진탐색트리의 1차시 동영상 시청 필요 (height 정보 수정 필요)
	
T = BST()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'deleteC':
        v = T.search(int(cmd[1]))
        T.deleteByCopying(v)
        print("- {0} is deleted by copying".format(int(cmd[1])))
    elif cmd[0] == 'deleteM':
        v = T.search(int(cmd[1]))
        T.deleteByMerging(v)
        print("- {0} is deleted by merging".format(int(cmd[1])))
    elif cmd[0] == 'search':
        v = T.search(int(cmd[1]))
        if v == None:
            print("* {0} is not found!".format(cmd[1]))
        else:
            print("* {0} is found!".format(cmd[1]))
    elif cmd[0] == 'height':
        h = T.height(T.search(int(cmd[1])))
        if h == -1:
            print("= {0} is not found!".format(cmd[1]))
        else:
            print("= {0} has height of {1}".format(cmd[1], h))
    elif cmd[0] == 'succ':
        v = T.succ(T.search(int(cmd[1])))
        if v == None:
            print("> {0} is not found or has no successor".format(cmd[1]))
        else:
            print("> {0}'s successor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'pred':
        v = T.pred(T.search(int(cmd[1])))
        if v == None:
            print("< {0} is not found or has no predecssor".format(cmd[1]))
        else:
            print("< {0}'s predecssor is {1}".format(cmd[1], v.key))
    elif cmd[0] == 'Rleft':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateLeft(v)
            print("@ Rotated left at node {0}".format(cmd[1]))
    elif cmd[0] == 'Rright':
        v = T.search(int(cmd[1]))
        if v == None:
            print("@ {0} is not found!".format(cmd[1]))
        else:
            T.rotateRight(v)
            print("@ Rotated right at node {0}".format(cmd[1]))
    elif cmd[0] == 'preorder':
        T.preorder(T.root)
        print()
    elif cmd[0] == 'postorder':
        T.postorder(T.root)
        print()
    elif cmd[0] == 'inorder':
        T.inorder(T.root)
        print()
    elif cmd[0] == 'exit':
        break
    else:
        print("* not allowed command. enter a proper command!")