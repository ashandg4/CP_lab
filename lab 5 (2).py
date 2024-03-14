# Write a generator to generate the fibonacci series.

def fibo():
    n = int(input("Number of terms of the series: "))
    final=0
    count=1
    a,b=0,1
    while count<=n:
        a,b=b,a+b
        print(b,end="   ")
        count+=1
fibo()