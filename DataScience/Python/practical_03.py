# Grade Distribution according to marks 
def marks(x):
    if x >= 90:
        print("Grade O")
    elif x < 90 and x > 80:
        print("Grade is A+")
    elif x < 80 and x > 70:
        print("Grade is A")
    elif x < 70 and x > 60:
        print("Grade is B")
    elif x < 60 and x > 50:
        print("Grade is C")
    elif x < 50 and x > 35:
        print("Grade is D")
    else :
        print("Grade is F")
user_marks = int(input("Enter Your Marks : "))
marks(user_marks)