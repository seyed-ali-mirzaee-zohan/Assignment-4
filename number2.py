from math import sqrt
def Quadratic_equation():
    print('a*x**2+b*x+c=0')
    a=int(input('Please enter the value of a :'))
    b=int(input('Please enter the value of b :'))
    c=int(input('Please enter the value of c :'))
    delta=(b**2-4*a*c)
    if delta>0 :    
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print('x1:',x1,', x2:',x2)
    if delta==0:
        x1=(-b)/(2*a)
        print('x1:',x1)
    if delta<0:
        print("The equation has no answer !! ")
Quadratic_equation()
