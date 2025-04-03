# Strings

# a="this is kamal kumar nahak"
# print(a[1])
# print(a[3])
# print(a[-1])
# print(a[-5])
# print(a[1:4])
# print(a[::-1])

#List
 
""" a = ["kamal", 2, "visakhaptanam"]
print(a)
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])  """
#print(a[-4] index out of range

#tuple(immutable)
"""
tup1 = ()
tup2 = ('hello', 'world')
print("i am kamal", tup2)


tup3 = tuple([1,2,3,4,5])

print(tup3[0])
print(tup3[-1])
print(tup3[-2])
print(tup3[-3])  """

#boolean

"""valid = True
invalid = False
print(type(valid))
print(type(invalid)) """

#set (unordered collection, muttable, no duplicates)

""" s1 = set("HelloWelcomeHello")
print("Set with the use of String: ", s1)

s2 = set(["Hello", "For", "Hello"])
print("Set with the use of List: ", s2) """

#string operations

#task -> create a program to mention all the string function
""" name = "revature"
print(name[0])
print(name[1:4])
print(name.upper())
print(name.lower()) """

#List(list)

""" fruits = ["append", "bannana", "cherry"]
fruits.append("grape")
print(fruits)
print(fruits[3]) """

#range

""" numbers = range(1, 10 ,2) #(start, end - 1 , skips)
print(set(numbers))
print(list(numbers))
print(tuple(numbers))  """

"""sets = {1,2,3,4,5}
print(sets)
sets.add(6)
print(sets)

fs = frozenset({1,2,3})
fs.add(4) """


#dictonary

""" student  =  {"name" : "kamal", "age" : 21, "city" : "new york"}
print(student["name"])
print(student["age"])
print(student["city"]) """

#binary types
"""
b = [65, 66 , 67]
print(b)
c = bytes([65, 66, 67])           
# we give array bracket to repreent in noramal number
# or else it will printed in the binary format               
print(c)  #b'ABC' (output)  
"""

#none data type  
"""
x = None
print(type(x)) """


#Flow control statements
""" age = int(input("enter the age"))
if age > 18:
    print("age is greater than 18")
elif age == 18:
    print("age is equal to 18")
else:
    print("not greater than 18")  """
    
    
    #example 2
'''a = int(input("enter a number: "))
b = int(input("enter a number: "))
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are eqaul")
else:
    print("b is greater than a") '''
    
#nested if statement

'''i = int(input("enter a number"))
if i!= 0:
    if i > 0:
        print("positive")
    else:
        if i < 0:
            print("negative")
else:
    print("enter a valid number") '''
    

#while loop and break example
'''n = 10
while n > 0:
    if n == 2:
        break
    print(n)
    n -= 1  '''
    #continue example
'''
n1 = 10
while n1 > 0:
    
   
    if n1 == 2:
        continue
    print(n1)
    n1 -= 1'''
    
#for loop in pyhton


'''mylist = ("Apple", "Bannana", "Grape")
for x in mylist:
    print(x) '''


'''mylisti = (1, 2, 3, 4, 5)
for x in mylisti:
    print(x * x) '''

#nested for loop
'''
x = [1, 2]
y = [4, 5]
for i in x:
    for j in y:
        print (i , j) '''
        
# for loop in dictionary
'''
info = {
    'kamal' : 21,
    'kaushik' : 21,
    'thomas' : 23,
    'sid' : 21,
    'john' : 23,
    'vinay' : 21,
}

for k in info.keys():
    print(k) # keys
    print(info[k]) #values 
'''
    
#functions
'''
def add():
    print("printing")
add()
'''
#ex2
'''
def greating():
    print("hello, good morning..")
greating() '''

#functions(passing arguments)
'''
def info(name):
    print("hello my name is", name)

info("Kamal") '''
# task (by taking input we have to dispaly it)
'''def calling(i):
    print("my name is", i)
    
infor = str(input("Enter your name"))
calling(infor) '''


'''   
def add(a, b):
    return a + b
res = add(10 , 20)
print(res) '''


'''   
def add(a, b):
    return a + b

i = int(input("enter a number"))
j = int(input("enter a number"))
res = add(i , j)
print(res)  '''

#default output function


'''
def greet(name = "greet"):
    print("hello", name)
greet()
greet("yellow") '''

#returning with multiple values
'''
def details():
    name = "kamal"
    age = 21
    return name, age
n, a = details()
print("Name: ", n, " | Age:", a) '''

#function with multiple args(*) 
'''
def add_all(*numbers):
    return sum(numbers) #her sum is the predefined function

print(add_all(1,2,3,4,5)) '''

#function with **kwargs(keyword Arguments)

'''
def info(**details):
    for key, value in details.items():
        print(key, ":", value)
info(kamal=21, kaushik=22)

def info(**details):
    for key, value in details.items():
        print(key, ":", value)
a = {"kamal" : 21, "kaushik" : 22, "vinay" : 23}
info(**a) #The ** operator unpacks the dictionary, converting it into keyword arguments. 
'''

#arrays

'''import array
fruits = array.array('u',"custom", "bananan") #type error
for fruit in fruits:
    print(fruit) '''


'''import array
numbers = array.array('i',[1,2,3,4])
length = len(numbers)
print(length)'''

#sorted array
'''numbers = array.array('i', [6,1,4,7,7,8])
num_sort = sorted(numbers)
print(num_sort) '''