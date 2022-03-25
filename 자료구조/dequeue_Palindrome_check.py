from collections import deque

class deque:
  def __init__(self):
    self.items = []
    
  def append(self, c):
    self.items.append(c)
    
  def appendleft(self, c):
    self.items.appendleft(c)

  def pop(self):
    try:
      return self.items.pop()
    except IndexError:
      print("deque is empty")

  def popleft(self):
    try:
      return self.items.pop(0)
    except IndexError:
      print("deque is empty")

  def __len__(self):
    return len(self.items)

  def right(self):
    try:
      return self.items[-1]
    except IndexError:
      print("deque is empty")

  def left(self):
    try:
      return self.items[0]
    except IndexError:
      print("deque is empty")
            
def check_palindrome(s):
    dq = deque()
    for i in range(len(s)):
        dq.append(s[i])
    palindrome = True
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            palindrome = False
            break

    return palindrome

s = input()
output = check_palindrome(s)
print(output)
    

	
	