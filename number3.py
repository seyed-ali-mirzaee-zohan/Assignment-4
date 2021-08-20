def Multiplication_table():
    rows = int(input("plz Enter number of rows : "))
    columns = int(input("plz Enter number of columns : "))
    for i in range(1,rows+1):
        for j in  range(1,columns+1):
            print(i*j,'\t',end='')
        print()
Multiplication_table()
while True:
    yes_no=input("Do you want to continue ? ")
    if yes_no=='YES' or  yes_no=='yes' or yes_no=='Y' or yes_no=='y':
        Multiplication_table()
    else:
        break