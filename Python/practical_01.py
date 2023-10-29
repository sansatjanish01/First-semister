def calculation (a,b):
    if a != 0 and b !=0:
        print(f"The addition of {a} and {b} is",a+b)
        print(f"The Substraction of {a}and {b} is ",a-b)
        print(f"The Multiplication of {a} and {b} is ",a*b)
        print(f"The Divsion of {a} and {b} is ",a/b)
user_input_a = int(input("Please enter Yout First number :"))
user_input_b = int(input("Please enter Your Second number :"))
calculation(user_input_a,user_input_b)