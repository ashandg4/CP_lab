# Perform various operations on list example sorting and slicing
a=[]
n = int(input("Enter number of elements (must be greater than 5) : "))
for i in range(0,n):
    if n>5:
        x=input("Enter element: ")
        a.append(x)
    else:
        break

# Slicing
print("Your list: ",a)

print("\n \n \t List slicing")
print("First 3 elements: ",a[0:3])

# Sorting
print("\ \n \t Sorting")

for i in range(len(a)): 
    min_idx = i 
    for j in range(i+1, len(a)): 
        if a[min_idx] > a[j]: 
            min_idx = j 

    a[i], a[min_idx] = a[min_idx], a[i]
print("Sorted list: ",a)
