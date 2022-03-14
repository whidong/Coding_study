#def function():
#    변수 = 초깃값
    #여러 가지 처리
    #여러 가지 처리
    #여러 가지 처리

#    return 100
    
#print(function())

# start~end까지 있는 모든 정수를 더하는 함수
def sum_all(start, end):
    변수 = 0
    for i in range(start, end, +1):
        변수 += i
    return 변수

print(sum_all(1, 100))
print(sum_all(50,100))
