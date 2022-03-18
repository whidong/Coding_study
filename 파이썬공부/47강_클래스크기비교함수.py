class Student:
  def __init__(self,이름,나이):
    print("객체가 생성되었습니다.")
    self.이름 = 이름
    self.나이 = 나이
  def __eq__(self,other):
    
    return (self.나이 == other.나이) and \
      (self.이름==other.이름)
  def __ne__(self,other):
    
    return (self.나이 != other.나이) and \
      (self.이름!=other.이름)
  def __gt__(self,other):
    
    return (self.나이 > other.나이) and \
      (self.이름>other.이름)
  def __ge__(self,other):
    
    return (self.나이 >= other.나이) and \
      (self.이름>=other.이름)
  def __lt__(self,other):
    
    return (self.나이 < other.나이) and \
      (self.이름<other.이름)
  def __le__(self,other):
    
    return (self.나이 <= other.나이) and \
      (self.이름<=other.이름)
student = Student("윤인성",3)
print(student == student)
print(student != student)
print(student > student)
print(student >= student)
print(student < student)
print(student <= student)

