def string_methods_examples():
    print("\n1. capitalize(): Capitalizes the first letter of the string.")
    s = "kamal kumar"
    print(s.capitalize())
    
    print("\n2. casefold(): Converts the string to lowercase (more aggressive than lower()).")
    s = "KaMaL KuMaR"
    print(s.casefold())
    
    print("\n3. count(): Returns the number of times a substring appears in the string.")
    s = "banana"
    print(s.count("a"))
    
    print("\n4. find(): Returns the index of the first occurrence of a substring.")
    s = "hello world"
    print(s.find("world"))
    
    print("\n5. index(): Returns the index of the first occurrence of a substring (raises an error if not found).")
    print(s.index("world"))
    
    print("\n6. isalnum(): Checks if the string consists only of alphanumeric characters.")
    s = "Hello123"
    print(s.isalnum())
    
    print("\n7. isalpha(): Checks if the string consists only of alphabetic characters.")
    s = "Hello"
    print(s.isalpha())
    
    print("\n8. isdigit(): Checks if the string consists only of digits.")
    s = "12345"
    print(s.isdigit())
    
    print("\n9. lower(): Converts the string to lowercase.")
    s = "HELLO"
    print(s.lower())
    
    print("\n10. upper(): Converts the string to uppercase.")
    s = "hello"
    print(s.upper())
    
    print("\n11. replace(): Replaces occurrences of a substring with another substring.")
    s = "Hello world"
    print(s.replace("world", "Python"))
    
    print("\n12. split(): Splits the string into a list based on a delimiter.")
    s = "apple,banana,orange"
    print(s.split(","))
    
    print("\n13. strip(): Removes leading and trailing whitespaces.")
    s = "   Hello World   "
    print(s.strip())
    
string_methods_examples()