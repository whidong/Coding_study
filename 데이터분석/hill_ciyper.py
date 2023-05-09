import numpy as np
from sympy import Matrix

def encyption(A, k):
  pass
def decryption(B, dk):
  pass
def make_dekey(key ,m):
  dk = key.copy()
  dk[0, 0], dk[1, 1] = dk[1, 1], dk[0, 0]
  print(dk)
  dk[0, 1] = -1*dk[0, 1]%26
  print(dk)
  dk[1, 0] = -1*dk[1, 0]%26
  print(dk)
  print(m*dk)

  dk = np.mod(m*dk, 26)
  print(dk)
  return dk

def make_key():
  key = np.random.randint(0, 26, size=(2, 2))
  if np.linalg.det(key) == 0:
    return make_key()
  k = key[0,0]*key[1,1] - key[0,1]*key[1, 0]
  k = k%26
  m = 0
  for i in range(26):
    if (k*i)%26 == 1:
      m = i
      return key, m
    else:
      m = -1
  if m == -1:
    return make_key()
  else:
    return key, m

key, m = make_key()
print(key, m)
dkey = make_dekey(key, m)

print(key)
print(dkey)
print(dkey*key)
sol = np.mod(dkey*key,26)
print("------------")
print(sol)
plain_text = input()
text = []
for i in plain_text:
  text.append(ord(i)%32-1)

if len(text)%2 == 0:
  plain_text_matrix = np.reshape(text, (-1, 2)).T
else:# if text length is obb number
  plain_text_matrix = np.reshape(text[:-1], (len(text)//2, 2)).T

print(text)
print(plain_text_matrix)

