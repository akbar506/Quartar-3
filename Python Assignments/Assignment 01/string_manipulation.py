"""
String Manipulation

- Task: Given the string s, use string methods to:
 - Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
 - Convert to uppercase: change all characters in the string to uppercase.
 - Convert to lowercase: change all characters in the string to lowercase.

 - s:str = "hElLo WoRlD"

- Expected Output:
 - Hello world
 - HELLO WORLD
 - hello world
"""

s:str = "hElLo WoRlD"

print(s.capitalize()) # Output: Hello World
print(s.upper()) # Output: HELLO WORLD
print(s.lower()) # Output: hello world