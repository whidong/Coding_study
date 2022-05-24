class Node:
	def __init__(self, key):
		self.key = key
		self.parent = self.left = self.right = None
		self.height = 0

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
			self.update_height(v)
			self.size += 1
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
			else:
				self.root = None	
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
		self.size -= 1
		self.update_height(pt)
		return pt

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

class AVL(BST):
	def __init__(self):
		self.root = None
		self.size = 0

	def rebalance(self, x, y, z):
		if z.right == y and y.right == x or z.left == y and y.left == x:
			if z.right == y:
				return super(AVL, self).rotateLeft(z)
			else:
				return super(AVL, self).rotateRight(z)
		else:
			if z.right == y:
				k = super(AVL, self).rotateRight(y)
				return super(AVL, self).rotateLeft(k.parent)
			else:
				k = super(AVL, self).rotateLeft(y)
				return super(AVL, self).rotateRight(k.parent)
				
        # assure that x, y, z != None
        # return the new 'top' node after rotations
        # z - y - x의 경우(linear vs. triangle)에 따라 회전해서 균형잡음

	def insert(self, key):
		v = super(AVL, self).insert(key)
		if v.parent == None:
			return v
		z, y, x = v, None, None
		left, right = -1, -1
		bf = left-right
		while -1 <= bf <= 1:
			if z.parent == None:
				break
			left = right = -1
			x, y, z = y, z, z.parent
			if z.left:
				left = z.left.height
			if z.right:
				right = z.right.height
			bf = left - right
		if bf>1 or bf<-1:
			nz = self.rebalance(x, y, z)
			if nz.parent == None:
				self.root = nz
		return v
	# x, y, z를 찾아 rebalance(x, y, z)를 호출
	# BST에서도 같은 이름의 insert가 있으므로, BST의 insert 함수를 호출하려면 
	# super(class_name, instance_name).method()으로 호출
	# 새로 삽입된 노드가 리턴됨에 유의!
        
	def delete(self, u): 
		v = super(AVL, self).deleteByCopying(u)
		z, y, x = v, None, None
		left, right = -1, -1
		bf = left-right
		while v:
			if z.left:
				left = z.left.height
			if z.right:
				right = z.right.height
			bf = left - right
			if -1 > bf or 1 < bf:
				y = self.bf(z)
				if y != None:
					x = self.bf(y)
				v = self.rebalance(x, y, z)
			v = v.parent
			z, y, x = v, None, None
			left, right = -1, -1
		return u

	def bf(self, k):
		left, right = -1, -1
		if k.left:
			left = k.left.height
		if k.right:
			right = k.right.height
		if left == right:
			return k.left
		if left > right:
			return k.left
		else:
			return k.right
				# 또는 self.deleteByMerging을 호출가능하다. 그러나 이 과제에서는 deleteByCopying으로 호출한다
        # height가 변경될 수 있는 가장 깊이 있는 노드를 리턴받아 v에 저장
        # v가 AVL 높이조건을 만족하는지 보면서 루트 방향으로 이동
        # z - y - x를 정한 후, rebalance(x, y, z)을 호출



T = AVL()
while True:
    cmd = input().split()
    if cmd[0] == 'insert':
        v = T.insert(int(cmd[1]))
        print("+ {0} is inserted".format(v.key))
    elif cmd[0] == 'delete':
        v = T.search(int(cmd[1]))
        T.delete(v)
        print("- {0} is deleted".format(int(cmd[1])))
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