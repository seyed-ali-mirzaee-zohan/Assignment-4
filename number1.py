def Chess():
    h=int(input('Please specify the number of sections in the horizontal direction : '))
    v=int(input('Please specify the number of sections in the vertical direction : '))
    for i in range(v):
        for j in range(h):
            if (i+j) % 2==1:
                print('#',end='')
            else:
                print('*',end='')
        print()
Chess()