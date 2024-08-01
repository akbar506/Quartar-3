"""
Get last element Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.
"""

def get_last_element(lst):
    lst.pop() # remove the last element in the list
    print(lst)

lst:list[int] = [2, 4, 5, 2, 10]

get_last_element(lst)