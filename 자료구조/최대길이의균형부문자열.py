class Node:
    def __init__(self, key=None, value = None):
        self.key = key
        self.value = value
        self.prev = self
        self.next = self
    def __str__(self):
        return str(self.key)
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
    def __iter__(self):
        v = self.head.next
        while v != self.head:
            yield v
            v = v.next
    def __str__(self):
        return " -> ".join(str(v.key) for v in self)
    def splice(self, a, b, x):
        if a == None or b == None or x == None:
            return
        a.prev.next = b.next
        b.next.prev = a.prev
        x.next.prev = b
        b.next = x.next
        a.prev = x
        x.next = a
    def moveBefore(self, a, x):
        self.splice(a, a, x.prev)
    def insertBefore(self, x, key, value):
        self.moveBefore(Node(key, value), x)
    def pushBack(self, key, value):
        self.insertBefore(self.head, key, value)
    def search(self, key):
        v=self.head.next
        while v.key != None:
            if v.key == key:
                return v
            v = v.next
        return None
    def Lsearch(self, key):
        v=self.head.next
        m = 0
        while v.key != None:
            if v.key == key:
                return m
            m += 1
            v = v.next
        return None
    def deleteNode(self, key):
        if key == None or key == self.head:
            return
        key.prev.next = key.next
        key.next.prev = key.prev

    def Rsearch(self, key):
        v = self.head.prev
        n = 0
        while v.key != None:
            if v.key == key:
                return n
            n += 1
            v = v.prev
        return None

def solve(A):
    l = DoublyLinkedList()
    a, b = 0, 0
    m, f=[], []
    for i in range(len(A)):
        if A[i] == '0':
            a += 1  
        else:
            b += 1
        if a-b not in m:
            l.pushBack(a-b,i)
            m.append(a-b)
            if a-b == 0:
                f.append(0)
            else:
                f.append(i+1)
        else:
            l.deleteNode(l.search(a-b))
            l.pushBack(a-b, i)
    output = 0
    for i in range(len(m)):
        first = f[i]
        last = l.search(m[i]).value+1
        if last-first > output:
            output = last-first
    return output


A = input().strip()
print(solve(A))