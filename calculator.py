result = 0

val1 = float(input("Enter value 1 : "))
val2 = float(input("Enter value 2 : "))

opr = input("Enter operator [ + - * / ] : ")

if opr == '+':
    res = val1 + val2
elif opr == '-':
    if val1 > val2 :
        res = val1 - val2
    else :
        res = val2 - val
elif opr == '*':
    res = val1 * val2
elif opr == '/':
    if val1 == 0:
        print("Division by zero is not allowed, program terminated!")
    else :
        res = val1/val2
else :
    print("WRONG input program terminated!")
print("Result : ", res)
