#i=0

#while True:
#    print("{}번쨰 반복문입니다.".format(i))
#    i += 1

#    input_text = input("> 종료하시겠습니까?(y)")
#    if input_text in ("Y","y"):
#        print("반복을 종료합니다.")
#        break
#변수를 선업합니다.
numbers = [5, 15, 6, 20, 7, 25]
#반복을 돌립니다.
for number in numbers:
    #number 가 10보다 작으면 다음 반복으로 넘어갑니다.
    if number < 10:
        continue # 현재 반복을 중지하고, 다음 반복으로 넘어간다.
    print(number)#출력합니다.