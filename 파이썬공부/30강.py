#array=[]
#for i in range(0,20,2):
#    array.append(i*i)
#위의 3줄은 아래의 한줄과 같음
#array[i*i for i in range(0, 20, 2)]

array_1=[i for i in range(10)] #뒤에 조건문을 추가해도됨
array_2=[i for i in range(0, 10, 2)]
array_3=[1 for i in range(10)]
print(array_1)
print(array_2)
print(array_3)
 