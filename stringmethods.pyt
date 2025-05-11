a = "$$$$$$$John F Kennedy$$$$$$$"#string are immutable 
print(len(a))
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())
print(a.count("o"))
print(a.rstrip("$")) # rstrip doesn't remove the first $ sign
print(a.lstrip("$")) # lstrip doesn't remove the last $ sign
print(a.strip("$")) # strip removes the first and last $ sign
print(a.replace("$", "")) # replace replaces all $ signs with empty string
print(a.split("$")) # split splits the string into a list of strings
print(a.split()) # split without any arguments splits the string into a list of words
print(a.endswith("O")) # endswith checks if the string ends with the given string 
print(a.startswith("$")) # startswith checks if the string starts with the given string 
print(a.find("Kennedy")) # find returns the index of the first occurrence of the given string 
print(a.index("Mark")) # index returns the index of the first occurrence of the given string if index is not found it raises an error but find returns -1 
