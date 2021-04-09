n = int(input("Enter number:"))
while True :
    if str(n) == str(n)[::-1]:
        print(str(n)[::-1],"is a palindrome")
        break
    else:
        n += int(str(n)[::-1])

