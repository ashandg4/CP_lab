#wap using if else for a simple calculator
a="Addition"
b="Substraction"
c="Multiplication"
d="Division"
e="Quotient"
f="Reminder"
g="Exponent"
print(a,"\n",b,"\n",c,"\n",d,"\n",e,"\n",f,"\n",g)

ask= input("What operation do you want to do? ")
no1= float(input("Enter number 1: "))
no2= float(input("Enter number 2: "))

if ask == "Addition":
    print(no1," + ",no2," = ",no1+no2)

elif ask == "Substraction":
    print(no1," - ",no2," = ",no1-no2)


elif ask == "Multiplication":
    print(no1," x ",no2," = ",no1*no2)

elif ask == "Division":
    if no2==0:
        print("Division by zero not possible")
    else:
        print(no1," / ",no2," = ",no1/no2)
    
elif ask == "Quotient":
    print("Quotient when",no1," is divided by ",no2," = ",no1//no2)

elif ask == "Reminder":
    print("Reminder when",no1," is divided by ",no2," = ",no1%no2)

elif ask == "Exponent":
    print("Exponential when",no1," is base and ",no2," is its power = ",no1**no2)