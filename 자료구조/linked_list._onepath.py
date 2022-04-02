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
		# head 노드의 값 리턴. empty list이면 None 리턴

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
		# tail 노드의 값 리턴. empty list이면 None 리턴

	def search(self, key):
		v = self.head
		while v:
			if v.key == key:
				return v
			v = v.next
		return None
		# key 값을 저장된 노드 리턴. 없으면 None 리턴
		
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
	elif cmd[0] == "printList":
		L.printList()
	elif cmd[0] == "size":
		print("list has", len(L), "nodes.")
	elif cmd[0] == "exit":
		print("DONE!")
		break
	else:
		print("Not allowed operation! Enter a legal one!")