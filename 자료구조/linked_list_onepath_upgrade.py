class Node:
	def __init__(self, key=None):
		self.key = key
		self.next = None
	def __str__(self):
		return str(self.key)

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	def __len__(self):
		return self.size
	
	def printList(self): # 변경없이 사용할 것!
		v = self.head
		while(v):
			print(v.key, "->", end=" ")
			v = v.next
		print("None")
	
	def pushFront(self, key):
		new_node = Node(key)
		new_node.next = self.head
		self.head = new_node
		self.size += 1
	def pushBack(self, key):
		new_node = Node(key)
		if self.size == 0:
			self.head = new_node
		else:
			tail = self.head
			while tail.next != None:
				tail = tail.next
			tail.next = new_node
		self.size += 1
	def popFront(self): 
		if len(self) == 0:
			return None
		else:
			s = self.head
			key = s.key
			self.head = s.next
			self.size -= 1
			del s
			return key
	def popBack(self):
		if self.size == 0:
			return None
		else:
			previous, tail = None, self.head
			while tail.next != None:
				previous, tail = tail, tail.next
			if len(self) == 1:
				self.head = None
			else:
				previous.next = tail.next
			key = tail
			del tail
			self.size -= 1
			return key
	def search(self, key):
		v = self.head
		while v:
			if v.key == key:
				return v
			v = v.next
		return None# key 값을 저장된 노드 리턴. 없으면 None 리턴
	
	def remove(self, x):
		if x== None:
			return False
		else:
			previous, k = None, self.head
			if k == x:
				self.head = k.next
				del k
				self.size -= 1
				return True
			while k != x:
				previous, k = k, k.next
				if k.next == None:
					break
				elif previous == None:
					return False
			previous.next = k.next
			del k
			self.size -= 1
			return True
		# 노드 x를 제거한 후 True리턴. 제거 실패면 False 리턴
		# x는 key 값이 아니라 노드임에 유의!
	def reverse(self, key):
		if len(self) == 0 or len(self) == 1 or self.search(key) == None:
			return
		if self.head == self.search(key):
			p, q = None, self.head
			k = self.search(key)
			t = self.head
			while t.next != None:
				t = t.next
			while k.next != None:
				while q.next != None:
					p, q = q, q.next
				q.next = p
				p.next = None
				p, q = None, self.head
			self.head = t
			return
		e , s = None, self.head
		while s.key != key:
			e , s = s , s.next
		previous, tail = None, self.search(key)
		m = self.head
		while m.next != None:
			m = m.next
		while s.next != None:
			while tail.next != None:
				previous, tail = tail, tail.next
			tail.next = previous
			previous.next = None
			previous, tail = None, self.search(key)
		e.next = m
	def findMax(self):
		p, k, t = None, self.head, None
		if len(self) == 0:
			return None
		else:
			if k.next == None:
				return k.key
			while k.next != None:
				p, k = k, k.next
				if t != None:
					if p.key <= k.key and t < k.key :
						t = k.key    
					elif p.key > k.key and t < p.key:
						t = p.key
				else:
					if p.key <= k.key:
						t = k.key
					else:
						t = p.key  
			return t
		# self가 empty이면 None, 아니면 max key 리턴
	def deleteMax(self):
		if len(self) == 0:
			return None
		else:
			k = self.findMax()
			self.remove(self.search(k))
			return k
	def insert(self, k, val):
		if self.size <= k:
			self.pushBack(val)
			return
		t, n = None, self.head
		count = 0
		while count != k:
			t, n = n , n.next
			count += 1
		new_node = Node(val)
		new_node.next = n
		t.next = new_node
		self.size += 1
			
	def size(self):
		return self.size
	
# 아래 코드는 수정하지 마세요!
L = SinglyLinkedList()
while True:
	cmd = input().split()
	if cmd[0] == "pushFront":
		L.pushFront(int(cmd[1]))
		print(int(cmd[1]), "is pushed at front.")
	elif cmd[0] == "pushBack":
		L.pushBack(int(cmd[1]))
		print(int(cmd[1]), "is pushed at back.")
	elif cmd[0] == "popFront":
		x = L.popFront()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from front.")
	elif cmd[0] == "popBack":
		x = L.popBack()
		if x == None:
			print("List is empty.")
		else:
			print(x, "is popped from back.")
	elif cmd[0] == "search":
		x = L.search(int(cmd[1]))
		if x == None:
			print(int(cmd[1]), "is not found!")
		else:
			print(int(cmd[1]), "is found!")
	elif cmd[0] == "remove":
		x = L.search(int(cmd[1]))
		if L.remove(x):
			print(x.key, "is removed.")
		else:
			print("Key is not removed for some reason.")
	elif cmd[0] == "reverse":
		L.reverse(int(cmd[1]))
	elif cmd[0] == "findMax":
		m = L.findMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key is", m)
	elif cmd[0] == "deleteMax":
		m = L.deleteMax()
		if m == None:
			print("Empty list!")
		else:
			print("Max key", m, "is deleted.")
	elif cmd[0] == "insert":
		L.insert(int(cmd[1]), int(cmd[2]))
		print(cmd[2], "is inserted at", cmd[1]+"-th position.")
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")