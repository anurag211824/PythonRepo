#Upper and Lower Methods 
#strings in python are immutable they can't be changed
str1="anurag"
# name string is not changed
#upperStr is not changed
upperStr=str1.upper()
print(upperStr)
print()
lowerStr=upperStr.lower()
print(lowerStr)

print()

#Strip method
str2="Anurag!!!!!!!!!!!!!"
stripedStr=str2.rstrip("!")
print(stripedStr)

print()

#replace method
str3="aabbbbcccddd"
replaceStr=str3.replace("a","anu")
#find a and repace all its occurance with anu
print(replaceStr)

print()

#split methods
str4="apple mango oranges banana"
liststr4=str4.split(" ")
#This method converts the given string into a list after finding a space in string
print(liststr4)

print()

#captilize method
str5="my name is Anurag kumar"
captilizeStr5=str5.capitalize()
#This method make the first char of string in Uppercase and other char of string to lowercase 
print(captilizeStr5)

print()

#center method
str6="My name is anurag"
centerStr6=str6.center(34)
#center method align string to the center as per the parameter
print(centerStr6)

print()

#count method
str7="anu_anu_anu_rag"
countStr7=str7.count("anu")
#it counts the number of times the given string occurs in a particular string 
print(countStr7)

print()

#ends with function
str8="anuragkumar"
flag=str8.endswith("r")
#this method return true or False wheather a string is ending with given parmeter or not
print(flag)

print()

#find method
str9="I am learning python"
occuranceIndx=str9.find("python")
#this method return the index of string from where the given string is starts to appear, 
# and if the given string is not present it return -1
print(occuranceIndx)

print()

#isalnum method
string1 = "Hello123"
string2 = "Hello 123"
string3 = "Hello!"
string4 = ""
# Using isalnum() method
print(string1.isalnum())  # Output: True, because it contains only letters and digits
print(string2.isalnum())  # Output: False, because it contains a space
print(string3.isalnum())  # Output: False, because it contains a special character '!'
print(string4.isalnum())  # Output: False, because it's an empty string


print()

#isalpha method
# Example strings
a = "Hello"
b = "Hello123"
c = "Hello!"
d = ""
e = "Hello World"
# Using isalpha() method
print(a.isalpha())  # Output: True, because it contains only alphabetic characters
print(b.isalpha())  # Output: False, because it contains digits
print(c.isalpha())  # Output: False, because it contains a special character '!'
print(d.isalpha())  # Output: False, because it's an empty string
print(e.isalpha())  # Output: False, because it contains a space

print()

# Original string
original_string = "hello world"
# Applying title() method
title_string = original_string.title()
# Output the title-cased string
print(title_string)  # Output: 'Hello World'




# startswith(): Checks if a string starts with a specified substring.
str10 = "anuragkumar"
flag = str10.startswith("anu")
print(flag)  # Output: True


# join(): Joins the elements of an iterable (such as a list) into a single string.
list_str = ["apple", "banana", "cherry"]
joined_str = "-".join(list_str)
print(joined_str)  # Output: apple-banana-cherry











