"""
Convert an integer to its binary representation

- Task: Given an integer num
 - Obtain the binary representation of num

 - num:int = 45

- Expected Output:
 - Binary representation : 0b101101
"""

num:int = 45

num_bin = bin(num) # Output: Binary representation : 0b101101

print(f"Binary representation: {num_bin}")