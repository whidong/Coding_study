memo ={}
앉힐수있는최소사람수 = 2
앉힐수있는최대사람수 =10
전체사람의수 = 100
def 문제(남은사람수, 앉힌사람수):
    key =str([남은사람수, 앉힌사람수])
    if key in memo:
        return memo[key]
    if 남은사람수<0:
        return 0
    if 남은사람수 ==0:
        return 1
    count=0
    for i in range(앉힌사람수, 앉힐수있는최대사람수 +1):
        count +=문제(남은사람수-i, i)
    memo[key]=count
    return count

print(문제(전체사람의수, 앉힐수있는최소사람수))
