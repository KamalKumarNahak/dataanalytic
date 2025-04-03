a = 0
b = 1
no = int(input("Enter a number: "))
for i in range(no):
    series = a + b
    a = b
    b = series
print("the", no,"th fiboacci series of the number is ", a)