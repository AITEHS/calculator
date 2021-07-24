#list of avaliable operations
operations = ["+","-","/","*"]
#choose number and make sure it's number
def number():
    while True:
        try:
            number = int(input("Number:"))
            return number
        except:
            print("It wasn't number, try again")
            continue
#what to do with number
def operation():
     while True:

        operation = input("Operation:")
        if operation in operations:
            return operation
        else:
            print("Wrong operation, try again")
            continue
        
while True:
    print(eval(str(number()) + operation() + str(number())))
        