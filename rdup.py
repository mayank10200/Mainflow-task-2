# Take input from the user
user_input = input("Enter elements of the list: ")

# Convert input to list of integers
my_list = list(map(int, user_input.split()))

# Remove duplicates using set and preserve order
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)

# Print the result
print("List after removing duplicates:", unique_list)
