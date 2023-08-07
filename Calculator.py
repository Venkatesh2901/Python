first  = input("enter the value of 1st number: ")
second = input("enter the value of 2nd number: ")

operator =input("Enter the operator (+,-,*,/,%) : ")

first  =  int(first)                                   # string to integer conversion 
second = int(second)                                   # string to integer conversion     

if operator =='+' :
    print( " Additionn :" + str(first+second))           #operator '+' or "+" both correct

elif operator == "-" :
    print("Subtraction: " + str(first-second))

elif operator == '*' :
    print("Multiplication: " + str(first*second))

elif operator == "/" :
    print("Division: " + str(first/second))

elif operator == "%" :
    print("Modulus: " + str(first%second))

else :
    print("invalid opertor ")