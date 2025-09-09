user_string = input("Enter a string: ")
user_string = user_string.lower()

# Initialize counters
vowel_count = 0
consonant_count = 0

# Define vowels
vowels = "aeiou"

# Loop through each character
for char in user_string:
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Print the result
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
