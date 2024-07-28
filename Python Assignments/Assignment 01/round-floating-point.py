"""
Round floating-point numbers

- Task: Given a floating-point number value
 - Round value to the nearest integer.
 - Round value to two decimal places.

 - value:float = 12.34567

- Expected Output:
 - Rounded to nearest integer: 12
 - Rounded to two decimal places: 12.35
"""

num:int = 12.74

# Convert Integer to String
num_str: str = str(num)

# Get the index of "."
index_of_dot:int = num_str.find(".") + 1

# Get the characters after decimal point
float_value:str = num_str[index_of_dot:]

# Get only first character
first_float_value = float_value[:1]


# If first floating point value is greater than 5 then it will add 1 with num else subtract -1
if int(first_float_value) > 5:
    num = int(num) + 1
    print(num)
else:
    num = int(num)
    print(num)