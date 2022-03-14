import random
hanguls=list("아우에오민수가나다라마바사아자차카타파하김이최박")
with open("info.txt","w") as file:
  for i in range(1000):
    name= random.choice(hanguls)+ random.choice(hanguls)+random.choice(hanguls)
    weight = random.randrange(40, 100)
    high = random.randrange(150,200)
    file.write("{},{},{}\n".format(name,weight,high))

with open("info.txt","r")as file:
  for line in file:
    (name,weight,high)=line.strip().split(",")
    if (not name) or (not weight) or (not high):
      continue
    bmi = int(weight)/((int(high)/100)**2)
    result=""
    if 25 <= bmi:
      result='과체중'
    if 18.5<= bmi:
      result='정상체중'
    else:
      result='저체중'
  print('\n'.join([
    "이름 : {}",
    "몸무게: {}",
    "키: {}",
    "BMI: {}",
    "결과: {}"
  ]).format(name,weight,high,bmi,result))
  print()
