def x_print(a) :
    if a == 0:
        print(0)
      
    else:
        print(a)
        x_print( a - 1 )



x = int(input("Enter a number : "))
x_print(x)