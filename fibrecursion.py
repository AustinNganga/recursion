c_cache = {}
def fibonacci(a):
    if a in c_cache:
        return c_cache[a]

    if a==0:
        value =  0
    elif a==1:
        value =  1
    else:
        value =  fibonacci(a - 1)+fibonacci(a - 2)

    c_cache[a] = value
    return value    


x = int(input("Enter the position term of the fibonacci number that you wish to see(Starting from 1) : "))
print(f"The {x}th fibonacci number is {fibonacci(x-1)}")