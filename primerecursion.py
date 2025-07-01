# Define a recursive function to check if a number is prime
def prime(a, divisor=None):
    
    # If the number is less than or equal to 1, it's not prime
    if a <= 1:
       return False

    # On the first call, set the divisor to a - 1
    if divisor == None:
        divisor = a - 1

    # If we've reached 1 and found no divisors, the number is prime
    if divisor == 1:
        return True

    # If 'a' is divisible by the current divisor, it's not prime
    if a % divisor == 0:
        return False
    
    # Recursively check the next smaller divisor
    return prime(a, divisor - 1)


# Ask the user to enter a number
x = int(input("Enter an integer number : "))

# Call the prime function and print the result based on True/False
if prime(x):
    print(f"{x} is a prime number")  # If True, it's prime
else:
    print(f"{x} is not a prime number")  # If False, it's not prime
