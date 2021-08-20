def factorial():
    number=int(input("Enter your desired number : "))
    m=1
    for i in range(1,number+1):
        m=m*i
        if m==number:
            print('F!',i,':',number)
            break
        if i==number and m != number :
            print("the number Not obtained from factorial")
factorial()
while True:
    yes_no=input("Do you want to check another number ?")
    if yes_no=='YES' or  yes_no=='yes' or yes_no=='Y' or yes_no=='y':
        factorial()
    else:
        break