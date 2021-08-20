print('a*x**2+b*x+c=0')
def Quadratic_equation():
    a=float(input('Please enter the value of a :'))
    b=float(input('Please enter the value of b :'))
    c=float(input('Please enter the value of c :'))
    x1=float(-b+(b**2-4*a*c)**0.5)/(2*a)
    x2=float(-b-(b**2-4*a*c)**0.5)/(2*a)
    print('x1:',x1,', x2:',x2)
Quadratic_equation()