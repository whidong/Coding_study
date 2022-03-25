class Stack:
    def __init__(self):
        self.items = []    
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:    
            return self.items.pop()
        except IndexError:    
            pass
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            pass
    def __len__(self):    
        return len(self.items)
    def isEmpty(self):
        return self.__len__() == 0



def parChecker(p):
		t = " ".join(p).split()
		S=Stack()
		for token in t:
			if token in "([{":
				S.push(token)
			elif token in ")" and S.top() == "(":
				S.pop()
			elif token in "}" and S.top() == "{":
				S.pop()
			elif token in "]" and S.top() == "[":
				S.pop() 
			elif token in "]})":
				if S.isEmpty():
					return False
		if S.isEmpty() != True:
			return False
		else:
			return True
p= input()
print(parChecker(p))
