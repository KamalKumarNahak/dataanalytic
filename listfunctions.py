
def list_methods_examples():
    print("\n1. append(): Adds an element to the end of the list.")
    lst = ["Kamal"]
    lst.append("Kumar")
    print(lst)
    
    print("\n2. clear(): Removes all elements from the list.")
    lst.clear()
    print(lst)
    
    print("\n3. copy(): Returns a shallow copy of the list.")
    lst = ["Kamal", "Kumar"]
    copy_lst = lst.copy()
    print(copy_lst)
    
    print("\n4. count(): Returns the number of times an element appears in the list.")
    lst = [1, 2, 3, 2, 1, 2]
    print(lst.count(2))
    
    print("\n5. extend(): Extends the list by appending all elements from an iterable.")
    lst = ["Kamal"]
    lst.extend(["Kumar", "Nahak"])
    print(lst)
    
    print("\n6. index(): Returns the index of the first occurrence of an element.")
    lst = [1, 2, 3, 4, 5]
    print(lst.index(3))
    
    print("\n7. insert(): Inserts an element at a specified index.")
    lst.insert(1, "New")
    print(lst)
    
    print("\n8. pop(): Removes and returns the element at a specified index (default is the last element).")
    popped = lst.pop()
    print(lst, "Popped element:", popped)
    
    print("\n9. remove(): Removes the first occurrence of a specified element.")
    lst.remove("New")
    print(lst)
    
    print("\n10. reverse(): Reverses the order of elements in the list.")
    lst.reverse()
    print(lst)
    
    print("\n11. sort(): Sorts the list in ascending order.")
    num_lst = [5, 2, 4, 1, 3]
    num_lst.sort()
    print(num_lst)
    
list_methods_examples()
