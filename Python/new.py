# finding the greatest of three numbers 
num_1 = int(input("enter the first number : "))
num_2 = int(input("enter the second number :"))
num_3 = int(input("enter the third number : "))
if num_1 > num_2 and num_1 > num_3:
    largest = num_1
elif num_2 > num_1 and num_2 > num_3:
    largest = num_2
else:
    largest = num_3
print("The largest of all three numbers is ",largest)

password = "Satish123"
attempt = 0
while attempt < 4:
    user_enter = input("enter the password : ")
    if user_enter == password:
        print("You just logged in ...")
        break
    elif user_enter != password:
        print("Login Faild , try again !")
    elif attempt > 3:
        print("You have reached the maximum limit")
    attempt += 1    


a = int(input("enter the number: "))
for i in range(1,a+1):
    for j in range(1,i+1):
        print("*", end = " ")
    print()

def armstrong(nun):
    n_str = str(x)
    n_len = len(n_str)
    for i in n_len:
        print(i)
armstrong(153)