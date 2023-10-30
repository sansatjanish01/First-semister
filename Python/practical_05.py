def fact(n):
    if n < 0:
        print("Factorial of negative numbers does not exist !")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
a = int(input("enter the number to get the factorial : "))
print(fact(a))

