try:
    print(x)
except:
    print("Error")

    
try:
    print(x)
except NameError:
    print("x is not defined")
except:
    print("something else went wrong")

    
try:
    print("HI")
except:
    print("something went wrong")
else:
    print("nothing went wrong")


try:
    print(x)
except:
    print("something went wrong")
finally:
    print("the 'try except' is finished")    
