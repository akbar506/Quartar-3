"""
String Replacement
- Task: Given the string s, use string methods to:
 - Replace "Python" with "Java": substitute "Python" with "Java".

 - s:str ="I love programming in Python"

- Expected Output:
 - I love programming in Java
"""

s:str ="I love programming in Python"

# Replace "Python" with "Java"
s_replace: str = s.replace("Python", "Java") # Output: I love programming in Java

print(s_replace)