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

	def update_height(self, v):
		while v != None:
			left = -1
			right = -1
			if v.left:
				left = v.left.height
			if v.right:
				right = v.right.height
			if left>=right:
				v.height = left + 1
			else:
				v.height = right + 1
			v = v.parent

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
				if p.key >= key:
					p.left = v
				else:
					p.right = v
			self.size += 1
			self.update_height(v)
			return v
		else:
			return None

	def height(self, x): 
		if x == None: return -1
		else: return x.height

	def deleteByMerging(self, x):
		a, b, pt = x.left, x.right, x.parent
		if a == None:
			c = b
		else:
			c = m = a
			while m.right:
				m = m.right
			if b != None:
				b.parent = m
			m.right = b
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
		if c:
			if c.parent:
				k = c.parent
		self.size -= 1
		self.update_height(pt)
		return pt

	def deleteByCopying(self, x):	
		if x == None:
				return
		a, b, pt = x.left, x.right, x.parent
		y = None
		if a:
			y = a
			while y.right:
				y = y.right
			x.key = y.key
		elif b:
			y = b
			while y.left:
				y = y.left
		if y == None:
			if pt:
				if pt.left == x:
					pt.left = None
				else: 
					pt.right = None
				x.parent = None
			else:
				self.root = None
			apt = pt
		else:
			x.key = y.key
			ya, yb, yp = y.left, y.right, y.parent
			c = ya
			if yb:
				c = yb
			if c:
				c.parent = yp
			if yp.left == y:
				yp.left = c
			else:
				yp.right = c
			apt = yp
		self.size -= 1
		self.update_height(apt)
		return apt

	def succ(self, x):
		if x == None or self.size == 1:
			return None
		r, pt = x.right, x.parent
		while r and r.left:
			r = r.left
		if r:
			return r
		else:
			while pt and pt.right == x:
				x = pt
				pt = pt.parent
			return pt
				
	def pred(self, x):
		if x == None or self.size == 1:
			return None
		l, pt = x.left, x.parent
		while l and l.right:
			l = l.right
		if l:
			return l
		else:
			while pt and pt.left == x:
				x = pt
				pt = pt.parent
			return pt

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
		if z.parent == None:
			self.root = z
		if b: 
			x.right = b
			b.parent = x
		else:
			x.right = None
		self.update_height(x)
		return z
	
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
		if z.parent == None:
			self.root = z
		if b: 
			x.left = b
			b.parent = x
		else:
			x.left = None
		self.update_height(x)
		return z
		
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