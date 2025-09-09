# Take input from user
user_input = input("Enter elements of the list separated by space: ")

# Convert input string to list of integers
my_list = list(map(int, user_input.split()))

# Reverse the list
reversed_list = my_list[::-1]

# Print the result
print("Original list:", my_list)
print("Reversed list:", reversed_list)
