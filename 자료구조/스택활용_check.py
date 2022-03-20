import stack_queue
S = stack_queue.Stack()

def parChecker(p):
	for p in len(S):
		if p == "(":
			S.push(p)
		elif p == ")":
			S.pop()
		else:
			print("Not allowed Symbol")
	if len(S)>0:
		return False
	else:
		return True
p= input().strip().split()
print(parChecker(p))
# pseudo code
