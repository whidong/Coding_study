def 함수():
  print("출력A")
  yield 100
  print("출력B")
  yield 200
  print("출력C")
  yield 300
  print("출력D")
  yield 400
제네레이터= 함수()
for i in 제네레이터:
  print(i)
  pass
#제네레이터 = 함수()
#print(next(제네레이터))