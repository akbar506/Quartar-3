"""
Pop method You have a list named items with the elements [10, 20, 30, 40]. If you use the pop method without any arguments, what will the list look like and what value will be removed?
"""

"""
Answer: If we use pop method without argument, It will remove the last element of the list.
"""

lst:list[int] = [10, 20, 30, 40]

lst.pop() # It will remove the last element of the list

print(lst) # Output: [10, 20, 30]