num1=int(input("Enter number: "))
num2=int(input("Enter number: "))
op=(input("Eenter operation(+,-,*/): "))
def cal(num1,num2):
    if op=="+":
        result=num1+num2
        print(result)
    elif op=="-":
        result=num1-num2
        print(result)
    elif op=="*":
        result=num1*num2
        print(result)
    elif op=="/":
        result=num1/num2
        print(result)
    else:
        print("choose again ")
        
