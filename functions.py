#Create a program to get the user, next write a function to display the value whatever we got got from the user



def details(lis):
    for x in lis:
        print(x)
    
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
address = str(input("Enter your address: "))
domain = str(input("Enter your domain: "))
mylist = [name, age, address, domain]
details(mylist)


'''
def details(*deta):
    print(deta)
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
address = str(input("Enter your address: "))
domain = str(input("Enter your domain: "))
details(name, age, address, domain) '''


