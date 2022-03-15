import time, random

def sum(A, n):
	pass
	# code here

random.seed()
A=[]

n=int(input())
while 1>n or n>5000:
  print("1이상 5000이하의 정수를 입력하세요.")
  n=int(input())

B=[A,A]
i=1
while i<=n:
  import random as rd
  A.append(rd.randint(0,100))
  i+=1
print(A[1],A[2])
print(B[1][2])

# 리스트 A에 랜덤 정수 값 n개 채움
# sum 함수 호출 + 시간 측정
# 함수의 수행시간을 출력