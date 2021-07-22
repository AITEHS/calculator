while True:
    try:
        a = int(input("First number:"))
        b = input("Choose operation:")
        c = int(input("Second number:"))
        break
    except:
        continue
###operations

if b == "+" or b == "plus":
    res = a+c        
elif b == "-" or b == "minus":
    res = a-c
elif b == "*" or b == "multiply":
    res = a*c
elif b == "/" or b == "divide":
    res = a/c
else:
    print("wrong operation")
try:
    print("result is:%s" % res)
except:
    pass