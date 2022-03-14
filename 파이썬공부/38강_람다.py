#def call_10_times(func):
#  for i in range(10):
#    #콜백함수(callback)
#    func(i)


#call_10_times(lambda number: print("안녕하세요",number))
#-------------------
# 리스트의 요소를 함수에 넣고 리턴된 값이true인것으로
# 새로운 리스트를 구성해주는 함수
#a= list(range(100))
#b= filter(lambda number:number % 2 == 0 , a)

#print(list(b))
# 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트
# 구성해주는 함수
def 제곱(number):
  return number *number

a= list(range(100))
print(list(map(제곱,a)))
print(list(map(lambda number: number*number,a)))
print([i*i for i in a if i%2==0])
#리스트 내포와 람다는 매우 유사함
#리스트 내포는 같은 리스트를 하나더만드므로 용량을 차지함
#그러나 map과 filter은 메모리를 절약할수있음

