"""
Delete a number Consider a list named numbers with the elements [1, 2, 3, 4, 5]. Use list method to delete the number 3?
"""

lst:list[int] = [1, 2, 3, 4, 5]



# This remove method will remove first occurrence of value.
lst.remove(3)
print(lst) # Output: [1, 2, 4, 5]  

lst:list[int] = [1, 2, 3, 4, 5]

# List method to delete
lst.pop(2) # It will delete the element at 2nd index which is 3.

print(lst) # Output: [1, 2, 4, 5]  