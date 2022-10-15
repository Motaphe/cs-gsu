x = int(input("Enter a positive integer: "))
binary = ""

while x > 0:
    binary += str(x % 2)
    x //= 2
    

print (f"The binary equivalent is: {binary}")


