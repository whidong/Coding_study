def gcd_sub(a, b):
	while a!=0 and b!=0:
		if a>b :a=a-b 
		else :b>a ;b=b-a
	return gcd_sub(a+b)
x=gcd_sub()
def gcd_mod(a, b):
	while a!=0 and b!=0:
		if a>b: a=a/b 
		else :b>a ;b=b/a
	return a+b
y=gcd_mod()
def gcd_rec(a, b):
    while a!=0 and b!=0:
        if a>b: b=a/b
        else : b>a ;a=a/b
    return a+b
z=gcd_rec()
gcd_sub(15, 3)
gcd_mod(15, 3)
gcd_rec(15, 3)
# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
print(x, y, z)