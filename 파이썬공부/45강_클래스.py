class Student:
  def __init__(self, name, korean, math, english, science):
    self.name = name
    self.korean = korean
    self.math = math
    self.english = english
    self.science = science
  def 총점(self):
    return self.korean + self.math+\
    self.english + self.science
  def 평균(self):
    return self.총점()/4
  def 출력(self):
    print(self.name,self.총점(),self.평균(),sep="\t")

students = [
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95),
  Student("윤인성",87,98,88,95)
]
print("이름","총점","평균",sep="\t")
for student in students:
  student.출력()


#객체지향프로그래밍 언어
""" 
동사 + 목적어: 명령어
  -출력(학생)
  -평균(학생)
  -총합(학생)
  
주어 + 동사 + 목적어 : 주어가 행위를 한다
  -학생.출력()
  -학생.평균()
  -학생.총합()



"""
