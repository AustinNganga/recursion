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