import time, random

def sum(A, n):
  B=[[0 for i in range(n)]for j in range(n)]
  for i in range(n):
    for j in range(i,n):
      if i==j:
        B[i][j] += A[i]
      elif i<j:
        B[i][j] += B[i][j-1]+A[j]
  return B
	# code here

random.seed()
A=[]

n=int(input())
while 1>n or n>5000:
  print("1이상 5000이하의 정수를 입력하세요.")
  n=int(input())

u=1
while u<=n:
  import random as rd
  A.append(rd.randint(0,100))
  u+=1


s = time.process_time()
sum(A,n)
e = time.process_time()

print('수행시간=', e-s)

# 리스트 A에 랜덤 정수 값 n개 채움
# sum 함수 호출 + 시간 측정
# 함수의 수행시간을 출력