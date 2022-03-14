max_value = 0
a= 0
b= 0
# 최대값을 구할때 이전의 수보다 작아질때 
# max_value에 이전 i*j 값이 들어가게함으로 끝남
for i in range(1, 100):
    j= 100 -i
    if max_value < i*j:
        max_value = i*j
        a= i
        b= j
print ("최대가 되는 경우: {} *{} ={}".format(a, b, max_value))