# Converting the decimal number into binary
def deciaml_to_dinary(x):
     bin_num =""
     while x > 0:
        remainder = x%2
        bin_num = str(remainder) + bin_num
        x = x //2
     print(bin_num)
deciaml_to_dinary(9)