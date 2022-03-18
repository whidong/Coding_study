"""
스네이크 케이스
i_love_you : 기본적으로 사용

캐멀 케이스
ILoveYou : 클레스 이름

"""
class Student:
  def __str__(self):
    return "{} {}살".format(self.이름,self.나이)
  def __init__(self,이름,나이):
    print("객체가 생성되었습니다.")
    self.이름 = 이름
    self.나이 = 나이
  def __del__(self):
    print("객체가 소멸되었습니다.")
  def 출력(self):
    print(self.이름, self.나이)

student = Student("윤인성",3)
student.출력()
print(str(student))
# 클래스(틀) : 학생은 이름이라는 속성을 갖고 있다
# 객체(실체화 된 것) : 학생의 이름은 "윤인성"이야!
# 실체화 한 객체 = "인스턴스"