import random

random.seed()
A=[]

n=int(input())
while 1>n or n>5000:
  print("1이상 5000이하의 정수를 입력하세요.")
  n=int(input())
i,j =map(int, input().split())
B=[i,j]
u=1
while u<=n:
  import random as rd
  A.append(rd.randint(0,100))
  u+=1
print(A[1],A[2])
print(B[1][2])

# n = 1 이상 5000 이하 정수 값 입력
# 리스트 A에 랜덤 정수 값 n개 채움
# sum 함수 호출 + 시간 측정
# 함수의 수행시간을 출력