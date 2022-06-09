class Heap:
  def __init__(self, L=[]):
    self.A = L
  def __str__(self):
    return str(self.A)

  def heapify_down(self, k, n):
    while 2*k+1 < n:
      L, R = 2*k+1, 2*k+2
      if self.A[L] > self.A[k]:
        m = L
      else:
        m = k
      if R < n and self.A[R] > self.A[m]:
        m = R
      if m != k:
        self.A[k], self.A[m] = self.A[m], self.A[k]
        k = m
      else:
        break
  def heapify_up(self, k):	# 올라가면서 A[k]를 재베치
    while k > 0 and self.A[(k-1)//2] < self.A[k] :
      self.A[k], self.A[(k-1)//2] = self.A[(k-1)//2], self.A[k]
      k = (k-1)//2

  def insert(self, key):
    self.A.append(key)
    self.heapify_up(len(self.A)-1)
    
  def delete_max(self):
    if len(self.A) == 0: return None
    key = self.A[0]
    self.A[0], self.A[len(self.A)-1] = self.A[len(self.A)-1], self.A[0]
    self.A.pop()	# 실제로 리스트에서 delete!
    self.heapify_down(0, len(self.A)) # len(self.A) = n-1
    return key

  def make_heap(self):
    n = len(self.A)
    for k in range(n-1, -1, -1):
      self.heapify_down(k, n)
      
  def heap_sort(self):
    n = len(self.A)
    for k in range(len(self.A)-1 , -1, -1):
      self.A[0],self.A[k] = self.A[k], self.A[0]
      n = n -1
      self.heapify_down(0, n)

S = [int(x) for x in input().split()]
H = Heap(S)
H.make_heap()
H.heap_sort()
print(H)