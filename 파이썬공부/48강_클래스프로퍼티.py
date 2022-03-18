class Rect:
  def __init__(self, width, height):
    if width <=0 or height <=0:
      raise Exception("너비와 높이가 음수가 나올 수 없습니다.")
    self.__width = width
    self.__height = height #속성앞에언더바2개 붙이면 외부에서 조작 불가능

  @property #클레스가 복잡해져서 등장하게됨
  def width(self):
    return self.__width
  @width.setter
  def width(self, width):
    if width <=0:
      raise Exception("너비는 음수가 나올 수 없습니다.")
    self.__width = width
  @property
  def height(self):
    return self.__height
  @height.setter
  def height(self, height):
    if height <=0:
      raise Exception("높이는 음수가 나올 수 없습니다.")
    self.__height = height
  def get_area(self):
    return self.__width*self.__height

rect = Rect(10,10)
#rect.set_width(rect.get_width()+10)
rect.width += 10
print(rect.get_area())