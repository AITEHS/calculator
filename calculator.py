operations = ["+","-","/","*"]
def number():
    while True:
        try:
            number = int(input("Number:"))
            return number
        except:
            continue
def operation():
     while True:

        operation = input("Operation:")
        if operation in operations:
            return operation
        else:
            continue
        
while True:
    print(eval(str(number()) + operation() + str(number())))
        