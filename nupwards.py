def x_upwards(a)->None:
    if a == 0:
        print(0)

    else:
        x_upwards( a - 1 )
        print(a)
          

x = int(input("Enter a number : "))
x_upwards(x)