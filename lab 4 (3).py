# Use dictionary to store and retrieve student grades
dict={}
while True:
    ask1= input("Name of student: ")
    ask2= float(input("Marks of student: "))
    ask3= input("wanna enter more? (yes or no)")
    dict[ask1]=ask2
    if ask3=="yes":
        continue
    else:
        break
print("Your list: ",dict)

ask4= input("Enter the name of student, I'll tell you the marks: ")
for i in dict.keys():
    if i==ask4:
        print(dict[i])
    else:
        break