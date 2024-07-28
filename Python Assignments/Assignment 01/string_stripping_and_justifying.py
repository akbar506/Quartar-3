"""
String Stripping and Justifying

- Task: Given the string "s", use string methods to:
 - Remove leading/trailing spaces: remove all leading and trailing whitespace characters from the string.
 - Left justify with '*': left justify the string within a field of width 20, using "*" as the fill character.
 - Right justify with '*': right justify the string within a field of width 20, using "*" as the fill character.

 - s:str ="   Python is fun!   "

- Expected Output:
 - Python is fun!
   Python is fun!*****
   *****Python is fun!
"""

s:str ="   Python is fun!   "

# Removes leading and trailing characters (whitespace by default).
s_remove_spaces:str = s.strip() # Output: Python is fun!
print(s_remove_spaces)

# Left justify with '*'
s_left_justified:str = s.lstrip().replace('   ', '*****') # Output: Python is fun!*****
print(s_left_justified)

# Right justify with '*'
s_right_justified:str = s.rstrip().replace('   ', '*****') # Output: *****Python is fun!
print(s_right_justified)