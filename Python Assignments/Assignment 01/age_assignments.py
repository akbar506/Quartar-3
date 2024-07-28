"""
Age Assignments Based on the Riddle

Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
- Anton is 21 years old.
- Beth is 6 years older than Anton.
- Chen is 20 years older than Beth.
- Drew is as old as Chen's age plus Anton's age.
- Ethan is the same age as Chen.
"""

# Define the names and ages of the friends
name1:str = "Anton"
age1:int = 21

name2:str = "Beth"
age2:int = age1 + 6

name3:str = "Chen"
age3:int = age2 + 20

name4:str = "Drew"
age4:int = age3 + age1

name5:str = "Ethan"
age5:int = age3

print(f"{name1} is {age1}")
print(f"{name2} is {age2}")
print(f"{name3} is {age3}")
print(f"{name4} is {age4}")
print(f"{name5} is {age5}")