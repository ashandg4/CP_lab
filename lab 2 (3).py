#fibonacci series
n = int(input("Number of terms of the series: "))
a=0
b=1
final=0
count=1
while count<=n:
    print(final,end="  ")
    count+=1
    a=b
    b=final
    final=a+b