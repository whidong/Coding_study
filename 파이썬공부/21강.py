# for <요소 변수 이름> in <리스트>:
#   코드

numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number -1)%3].append(number)

print(output)
