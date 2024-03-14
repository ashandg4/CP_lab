# function to check for palindrome
def palin(n):
    if n==n[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

n=input("Enter a string: ")
palin(n)