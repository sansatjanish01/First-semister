import numpy as np
mat_1 = [[3,3,5,7],[4,6,8,3]]
mat_2 = [[54,43,65,76],[44,65,34,34]]
operation = input("(add/sub/mul/div) choose one of the operation : ")
if operation == "add":
    print(np.add(mat_2, mat_1))
elif operation == "sub":
    print(np.subtract(mat_1,mat_2))
elif operation == "mul":
    print(np.multiply(mat_1,mat_2))
elif operation == "div":
    print(np.divide(mat_1,mat_2))
else:
    print("invalid input")