print("Finding the armstrong number ")
# first we are gonna take the input from the user that it the entered number is armstrong or nope
user_input = int(input("enter the number to get the armstrong of that: "))
temp = user_input # Now making a temp variable gonna store the user_input as a temparory variable 
sum = 0  # Initilizeing a variable which will gonna track the sum of the input digit
while user_input > 0: # This is the condition till the below task will be performed untill this condition get false 
    r = user_input % 10 # Here we store the last digit of the user_input 
    sum = sum + (r**3) # this is the step where we are storing the last digit cube in a sum variable 
    user_input = user_input // 10 # In this step we removed the last digit of the user_input i.e if user_input was 153 now after this step it will be 15 
    # as we have set above codition the loop will be continue till the user_input is greater than 0
if sum == temp:
    print("yes")
else :
    print("Nope")