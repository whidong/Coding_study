class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

def get_token_list(expr):
  tokenlist = " ".join(expr).split()
  sumstack = Stack()
  out = []

  for token in tokenlist:
    if token in '()+-*/^':
      while True:
        if len(sumstack)>1:
          a = sumstack.pop()
          b = sumstack.pop()
          c = b + a
          sumstack.push(c)
        elif len(sumstack)==1:
          out.append(sumstack.pop())
          break
        else:
          break
      out.append(token)
    else:
      sumstack.push(token)
  while len(sumstack)!=0:
    if len(sumstack)>1:
      a = sumstack.pop()
      b = sumstack.pop()
      c = b + a
      sumstack.push(c)
    elif len(sumstack)==1:
      out.append(sumstack.pop())
  return " ".join(out)

def infix_to_postfix(token_list):
		opstack = Stack()
		outstack = []
		tokenlist = token_list.split()
		prec = {}# 연산자의 우선순위 설정
		prec['('] = 0
		prec['+'] = 1
		prec['-'] = 1
		prec['*'] = 2
		prec['/'] = 2
		prec['^'] = 3 # 연산자 우선순위 이중에 가장느림
		
		for token in tokenlist:
				if token == '(':
					opstack.push(token)
				elif token == ')':                           
					while prec[opstack.top()]!=0:
						outstack.append(opstack.pop())
					opstack.pop()#설명이랑 다른부분
				elif token in '+-/*^':
					while True: #이부분때문에 다른 식 넣었을때 연산자 순서가 크게틀어짐 반복이아닌 나열했었음
						if opstack.isEmpty()==True:
							opstack.push(token)
							break
						elif prec[token]>prec[opstack.top()]:
							opstack.push(token)
							break
						else:
							outstack.append(opstack.pop())
				else:# operand일 때
					outstack.append(token)
		while opstack.isEmpty() != True:# opstack 에 남은 모든 연산자를 pop 후 outstack에 append
			outstack.append(opstack.pop())
		return " ".join(outstack)

def compute_postfix(token_list):
		compustack = Stack()
		outstack = []
		tokenlist = token_list.split()
		
		for token in tokenlist:
				if token in '+-/*^':
					a = float(compustack.pop())
					b = float(compustack.pop())
					if token == '+':
						c = b + a
					elif token == '-':
						c = b - a
					elif token == '/':
						c = b / a
					elif token == '*':
						c = b * a
					elif token == '^':
						c = b ** a
					compustack.push(c)
				else:
					compustack.push(token)
		return compustack.pop()

expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)
