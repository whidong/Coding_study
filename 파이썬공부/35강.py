
#n! = 1*2*3*4*...(n-2)*(n-1)*n
#def factorial_1(n):
#    변수 =1 
#    for i in range(1,n+1 ): 
#        변수 *=i

#    return 변수

#def factorial_2(n):
#    if n == 0:
#        return 1
#    else:    
#        return n*factorial_2(n-1)

#print(factorial_1(1))
#print(factorial_2(1))
#------------------------
#f(1)=1 f(2)=1
#f(n)=f(n-1)+f(n-2)
#counter=0
#def f(x):
#    global counter
#    counter +=1
#    if x == 1 or x== 2:
#        return 1
#    else:
#        return f(x-1)+f(x-2)

#print(f(40))
#print(counter)
#-------------------------------------
메모 = {1:1, 2:1}
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output=f(n-1)+f(n-2)
        메모[n]=output
        return output

print(f(500))









