"""
while True:
  try:
  #예외가 발생할 수 있는 가능성이 있는 코드
    print(float(input("숫자를 입력해"))**2)
    break
  except:
  #예외가 발생했을 때 실행할 코드
    print("숫자를입력해라")
"""
list_input_a=["52","273","32","스파이","103"]

list_number=[]
for item in list_input_a:
  try:
    float(item)
    list_number.append(item)
  except:
    pass

print("{}내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))
