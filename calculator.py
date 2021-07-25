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


mid_result = eval(str(number()) + operation() + str(number()))
print(mid_result)
while True:
    result = eval(str(mid_result) + operation() + str(number()))
    print(result)
    mid_result = result
