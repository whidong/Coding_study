# stack_queue.py 에 저장
class Stack:
    def __init__(self):
        self.items = []	# 데이터 저장을 위한 리스트 준비
    def push(self, val):
        self.items.append(val)
    def pop(self):
        try:	# pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:	# indexError 발생
            print("Stack is empty")
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return self.__len__()==0

    
    
    
