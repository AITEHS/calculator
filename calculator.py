import math
#list of avaliable operations
operations = ["+","-","/","*", "root"]
def number():
    while True:
        try:
            number = int(input("Number:"))
            return number
        except:
            print("It wasn't number, try again")
            continue
#what to do with number
def root(number, root):
    return pow(number, root)

def operation():
     while True:

        operation = input("Operation:")
        if operation in operations:
            if operation == "root":
                print( root(number(), number()))
            else:
                return operation
            
        else:
            print("Wrong operation, try again")
            continue

#midresult saves result for next operations
mid_result = eval(str(number()) + operation() + str(number()))
print(mid_result)
while True:
    result = eval(str(mid_result) + operation() + str(number()))
    print(result)
    #current value of midresult changes to last result
    mid_result = result
