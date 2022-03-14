with open("test.txt", "a") as file:
  file.write("say hello.")

file = open("test.txt", "a")
file.write("say hello.")
file.close()

with open("test.txt","r") as file:
  print(file.read())

file=open("test.txt", "r")
print(file.read())
file.close()


"""
어떤대상(!)
- 텍스트 파일: 텍스트에디터 열수 있다
- 바이너리 파일: 텍스트에디터 열수 없다(이미지 동영상 워드 엑셀 pdf 등)


어떻게 다룰 것인가(!)
-쓰기
  -새로(write):w
  -있는 파일 뒤에(append):A
-읽기(read): r
"""