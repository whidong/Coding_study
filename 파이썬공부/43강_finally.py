# 함수내부 : return
# 반복문 내부 :break

try:
  #예외가 발생할 수 있는 가능성이 있는 코드
  number = int(input("정수입력"))
  print("이력값은 {}입니다.".format(number))
except:
  #예외가 발생했을 때 실행할 코드
  print("예외가 발생")
finally:
  #무조건 적으로 실행할 코드
  print("무조건적으로 실행합니다.")
