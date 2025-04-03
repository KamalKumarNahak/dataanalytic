n = int(input("enter a number: "))
flag =True
i = 2
while(i < n):
    if n % i == 0:
        flag = False
        break
    i += 1
if flag == False:
    print("It is not a prime number")
else:
    print("It is a prime number")
