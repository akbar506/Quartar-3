"""
String Splitting and Joining

- Task: Given the string "s", use string methods to:
 - Split into a list: break the string into a list of substrings based on the delimiter ",".
 - Join with spaces: combine the list of substrings back into a single string, with each element separated by a space.

 - s:str ="apple,banana,cherry,dates"

- Expected Output:
 - ["apple", "banana", "cherry", "dates"]
 - apple banana cherry dates
"""

s:str ="apple,banana,cherry,dates"

# Split the string into a list of substrings based on the delimiter ","
s_split: list[str] = s.split(",") # Output: ["apple", "banana", "cherry", "dates"]
print(s_split)

s_join: str = " ".join(s_split) # Output: apple banana cherry dates
print(s_join)