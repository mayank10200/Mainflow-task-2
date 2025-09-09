# Take input from the user
user_input = input("Enter elements of the list: ")

# Convert input to list of integers
arr = list(map(int, user_input.split()))

# Bubble Sort algorithm
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            # Swap the elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Print the sorted list
print("Sorted list:", arr)
