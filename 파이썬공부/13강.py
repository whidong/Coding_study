# 비교 연산자
from http.client import OK


print(10 == 100) #같다
print(10 != 100) #다르다
print(10 > 100)
print(10 < 100)
print(10 >= 100)
print(10 <= 100)

x=20
10< x< 20 #파이썬에서는 논리적으로 문제없음
# 10< x and x< 20
#논리연산자
#단항연산자
not True #False
not False # True

#이항 연산자
True and True #그리고 +
or #둘중에 하나cle

사과 and 사과 : OK # ture and true = true
사과 and 똥 : x # true and false = false
똥 and 사과 : x #false and true = false
똥 and 똥 : x #false and false = false
 
사과 or 사과 :ok # true or true = true
사과 or 똥 : ok # true or false = true
똥 or 사과 : ok # flase or true = true
똥 or 똥 : x # flase or false = false