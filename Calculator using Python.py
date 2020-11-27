# Calculator App using Python 3
print ("Caluculator")
value1 = int(input("Enter your First Value : "))
value2 = int(input("Enter your Second Value : "))
operator = input ("Enter Operator Here : ")

if operator == 'Addition':
    val = value1 + value2
    print("Answer = ", val)
    
elif operator == 'Subtraction':
    val = value1 - value2
    print("Answer = ", val)
    
elif operator == 'Multiplication':
    val = value1 * value2
    print("Answer = ", val)
    
elif operator == 'Division':
    val = value1 / value2
    print("Answer = ", val)
    
elif operator == 'Square Root':
    val = value1 ** value2
    print("Answer = ", val)
    
elif operator == 'Modulus':
    val = value1 % value2
    print("Answer = ", val)
else :
    print("Please Enter Correct Operator")
