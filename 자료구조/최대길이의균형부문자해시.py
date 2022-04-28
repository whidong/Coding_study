class HashOpenAddr:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None]*self.size
        self.values = [None]*self.size
    def __str__(self):
        s = ""
        for k in self:
            if k == None:
                t = "{0:5s}|".format("")
            else:
                t = "{0:-5d}|".format(k)
            s = s + t
        return s
    def __iter__(self):
        for i in range(self.size):
            yield self.keys[i]

    def find_slot(self, key):
        i = self.hash_function(key)
        start = i
        while (self.keys[i] != None) and (self.keys[i] != key):
            i = (i+1) % self.size
            if i == start:
                return None
        return i

    def set(self, key, value=None):
        i = self.find_slot(key)
        if i == None:
            return None
        if self.keys[i] != None:
            self.values[i] = value
            return key
        else:
            self.keys[i] = key
            self.values[i] = value 
        return key

    def hash_function(self, key):
        return key % self.size

    def remove(self, key):
        i = self.find_slot(key)
        if self.keys[i] == None:
            return None
        j = i
        while True:
            self.keys[i] = None
            while True:
                j = (j+1)% self.size
                if self.keys[j] == None:
                    return key
                k = self.hash_function(self.keys[j])
                if (i < j < k or j < k <= i or k <= i < j):
                    break
            self.keys[i] = self.keys[j]
            i = j

    def search(self, key):
        i = self.find_slot(key)
        if self.keys[i] != None:
            return self.values[i]
        else: 
            return None
    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.set(key, value)
def solve(A):
    l = HashOpenAddr()
    a, b = 0, 0
    m, f=[], []
    for i in range(len(A)):
        if A[i] == '0':
            a += 1  
        else:
            b += 1
        if a-b not in m:
            l.set(a-b,i)
            m.append(a-b)
            if a-b == 0:
                f.append(0)
            else:
                f.append(i)
        else:
            l.remove(a-b)
            l.set(a-b, i)  
    output = 0
    for i in range(len(m)):
        first = f[i]
        last = l.search(m[i])
        if m[i] == 0:
          if(last+1)-first > output:
            output = (last)-first
        elif (last+1)-first > output:
            output = (last+1)-first
    return output
A = input().strip()
print(solve(A))