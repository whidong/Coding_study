class Stack:
	def __init__(self):
		self.items = []
	def push(self, val):
		self.items.append(val)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			print("Stack is empty!")
	def top(self):
		try:
			return self.items[-1]
		except IndexError:
			print("Stack is empty!")
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		return self.__len__() == 0
#=======================================< 구분선 >==========================================
def isNumber(string): # 숫자인지 확인
	try:
		float(string)
		return True
	except ValueError:
		return False
#=======================================< 구분선 >==========================================
def get_token_list(expr):
	temp_list = []
	temp_float = ''
	for element in expr:
		if isNumber(element) or element == '.':
			temp_float += element
		else:
			if temp_float:
				temp_list.append(temp_float)
				temp_float = ''
			if element.strip():
				temp_list.append(element)
	if temp_float:
		temp_list.append(temp_float)
	return temp_list
#=======================================< 구분선 >==========================================
def infix_to_postfix(token_list):
	opstack = Stack()
	outstack = []
	prec = {
		'(': 0,
		')': 0,
		'+': 1,
		'-': 1,
		'*': 2,
		'/': 2,
		'^': 3
	}
	for token in token_list:
		if token == '(':
					opstack.push(token)
		elif token == ')':
			while opstack.top() != '(':
				outstack.append(opstack.pop())
			opstack.pop()
		elif token in '+-/*^':
			if opstack.isEmpty():
				opstack.push(token)
			else:
				while prec[opstack.top()] >= prec[token]:
					outstack.append(opstack.pop())
					if opstack.isEmpty():
						break
				opstack.push(token)
		else:
			outstack.append(token)
	while len(opstack) > 0:
		if opstack.top() == '(' or opstack.top() == ')':
			opstack.pop()
		else:
			outstack.append(opstack.pop())
			
	return " ".join(outstack)
def compute_postfix(postfix):
	list_temp = postfix.split(" ")
	tempstack = Stack()
	calstack = Stack()
	for j in range(len(list_temp)):
		calstack.push(list_temp[-j-1])
	for i in range(len(calstack)):
		if isNumber(calstack.top()):
			tempstack.push(calstack.pop())
		else:
			calstack.pop()
		if calstack.top() == '+':
			calstack.pop()
			num1 = float(tempstack.pop())
			num2 = float(tempstack.pop())
			calstack.push(num1 + num2)
		elif calstack.top() == '-':
			calstack.pop()
			num1 = float(tempstack.pop())
			num2 = float(tempstack.pop())
			calstack.push(num2 - num1)
		elif calstack.top() == '*':
			calstack.pop()
			num1 = float(tempstack.pop())
			num2 = float(tempstack.pop())
			calstack.push(num2 * num1)
		elif calstack.top() == '/':
			calstack.pop()
			num1 = float(tempstack.pop())
			num2 = float(tempstack.pop())
			calstack.push(num2 / num1)
		elif calstack.top() == '^':
			calstack.pop()
			num1 = float(tempstack.pop())
			num2 = float(tempstack.pop())
			calstack.push(num2 ** num1)	
		if len(calstack) == 1 and len(tempstack) == 0:
			return calstack.pop()
#=======================================< 구분선 >==========================================
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)