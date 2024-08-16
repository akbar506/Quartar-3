def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Get the User's name from user.
user_name: str = str(input("Enter your name: "))

num_names: list[str] = ["first", "second", "third"]

# Create an empty list.
fav_nums: list[int] = []

# Iterate the users favourite numbers.
for num_name in num_names:

    # Get the favourite number from user and Store in "fav_nums" List
    user_fav_num1: int = int(input(f"Enter your {num_name} favorite number: "))

    # Append the favourite number in fav_nums
    fav_nums.append(user_fav_num1)

# Create an empty list
even_odd_num_list = []

# Iterate all number in "fav_nums" list.
for num in fav_nums:
    # Check if the remainder of number is zero or not
    if num % 2 == 0:
        even_odd_num_list.append((num, "even")) # Append the tuple in the list of that "num" and "even" if remainder is zero.
    else:
        even_odd_num_list.append((num, "odd")) # Append the tuple in the list of that "num" and "odd" if remainder is not zero.

print(f"Hello, {user_name} Let's explore your favorite numbers:")
for num, num_type in even_odd_num_list:
    print(f"The number {num} is {num_type}.")

for fav_num in fav_nums:
    print(f"The number {fav_num} and its square: ({fav_num}, {fav_num*fav_num})")

total_sum:int = sum(fav_nums)
print(f"Amazing! The sum of your favorite numbers is: {total_sum}")
if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number. But it's cool.")