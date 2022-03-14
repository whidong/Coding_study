import time, random

def evaluate_n2(A, x):
	output=0
	for k in range(0,n):
		for j in range(0,n):
			if j==k:
				output+=A[k]*(x**j)
	return output

def evaluate_n(A, x):
	output=0
	for k in range(0,n,1):
		output+=A[k]*(x**k)
	return output

random.seed()
A=[]
n=int(input())
i=1
while i<=n:
  import random as rd
  A.append(rd.randint(-1000,1000))
  i+=1

x=(rd.randint(-1000,1000))

s_1 = time.process_time()
evaluate_n2(A,x)
e_1 = time.process_time()

s_2 = time.process_time()
evaluate_n(A,x)
e_2 = time.process_time()

print('수행시간=', e_1-s_1)
print('수행시간=', e_2-s_2)


# random 함수 초기화
# n 입력받음
# 리스트 A를 randint를 호출하여 n개의 랜덤한 숫자로 채움
# evaluate_n2 호출
# evaluate_n 호출
# 두 함수의 수행시간 출력