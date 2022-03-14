"""
try:
  a=[273,103,52,57,100]
  number=int(input("정수입력(0~4까지 입력)>"))
  print(a[number])


except ValueError as exception:
  print("값에 문제가 있습니다.")
except IndexError as exception:
  print("0~4까지를 입력해라")
except Exception as exception:
  print("알수없는 예외가 발생했습니다.")  
"""
#  if type(exception) == ValueError:
#    print("값에 문제가 있습니다.")
#  elif type(exception) == IndexError:
#    print("0~4까지를 입력해라"

# raise 예외객체
raise Exception("안녕하세요")
