#VARS AND LISTS
global operation 
global status
operations = ["+","plus","-","minus", "/", "divide","*","multiply"]
problem = []

#FUNCS
def ch_op():
    while True:
        operation = input("Choose operation:")
        if operation == "=":
            return 1
            
        elif operation in operations:
            problem.append(operation)
            print(problem)
            return 0
            
        else:
            continue
#input numbers and choose operation

while True:
    
    try:
        number = int(input("Number:"))
        problem.append(str(number))
        print(problem)
        if(ch_op()):
            break
            
       
            
        
    except:
        continue
#calculations themselves

print(problem + "ok")