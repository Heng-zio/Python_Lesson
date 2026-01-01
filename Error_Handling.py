#try and except
try :   #for test code error or not
    x = 10 / 2

except :  # for answer when error occur
    print("Error: Division by zero is not allowed.")
else :  # if no error occur
    print("Division successful:", x)
finally : # always execute
    print("Program continues...")