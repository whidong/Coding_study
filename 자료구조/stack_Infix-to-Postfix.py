'''
Infix to postfix
'''


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

def infix_to_postfix(infix):
		opstack = Stack()
		outstack = []
		token_list = infix.split()
		prec = {}# 연산자의 우선순위 설정
		prec['('] = 0
		prec['+'] = 1
		prec['-'] = 1
		prec['*'] = 2
		prec['/'] = 2
		prec['^'] = 3 # 연산자 우선순위 이중에 가장느림
		
		for token in token_list:
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

	
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)
	
infix_expr = input()
postfix_expr = infix_to_postfix(infix_expr)
print(postfix_expr)

"""

위에 연산자 우선순위부분에서 크게 막혔었음 
while반복문의 사용 그리고 반복문안에 break를 적절하게 사용해주기
^ 를 제곱이라고 생각하는 멍청이....
^ 는 비트논리연산자의 하나로 곱셈 나눗셈보다 더 우선순위가 낮다
이전 코드는 git에 있을테니 참고

"""
