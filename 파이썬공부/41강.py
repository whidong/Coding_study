while True:
  string_input=input("정수를 입력헤")
  if string_input.isdigit():
    number_input_a = int(string_input)
    print("원의 반지름:", number_input_a)
    print("원의 둘레:", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14*(number_input_a**2))
    break
  else:
    print("정수를 입력해주세요!")
    
  
  

  