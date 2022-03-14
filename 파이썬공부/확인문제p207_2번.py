output = []
for i in range(0,101,1):
    if "{:b}".format(i).count("0") == 1:
        output.append(i)
        print("{}:{}".format(i,"{:b}".format(i)))
#output = [i for i in range(0,101,1) if "{:b}".format(i).count("0") == 1]
#위와 같이 한줄로 리스트내포하여 표현가능
print("합계",":" ,sum(output))
pass
    



