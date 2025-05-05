# question 1
t_cache = {}

def multiply(a: int,  b: int)->int:
    key = (a,b)
    if key in t_cache:
        return t_cache[key]
    if  b == 0:
        value = 0
    elif b == 1:
        value = a
    else:
        value =  a + multiply(a,b-1)
    t_cache[key]= value
    return value

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
result = (multiply(x, y))
print("the result is ", result)


# question 2

z_cache = {}

def exponent(a,b)->int:
    key = (a,b)
    if key in z_cache:
        value =  z_cache[key]
    if b == 0:
        value = 1
    elif b == 1:
        value =  a
    else:
        value =  a * exponent(a,b-1)
    z_cache[key] = value
    return value

x = int(input("Enter the base : "))
y = int(input("Enter the exponent : "))
result = exponent(x,y)
print("The result is ", result)

#question 3
def x_print(a):
    if a == 0:
        print(0)

    else:
        print(a)
        x_print(a - 1)


x = int(input("Enter a number : "))
x_print(x)


#question 4
def x_upwards(a) -> None:
    if a == 0:
        print(0)

    else:
        x_upwards(a - 1)
        print(a)


x = int(input("Enter a number : "))
x_upwards(x)


#question 5

def reverse(a):
    if len(a) == 1:
        return a
    else:
        return a[-1] + reverse(a[:-1])


x = input("enter the text that you want to be reversed : ")
reversed_text = reverse(x)
print(reversed_text)



#question 6
def prime(a, divisor=None):
    if a <= 1:
        return False

    if divisor == None:
        divisor = a - 1

    if divisor == 1:
        return True

    if a % divisor == 0:
        return False

    return prime(a, divisor - 1)


x = int(input("Enter an integer number : "))
if prime(x):
    print(f"{x} is a prime number")


else:
    print(f"{x} is not a prime number")


#question 7
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
