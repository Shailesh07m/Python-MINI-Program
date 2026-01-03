import random          # Used to shuffle characters randomly
import string          # Provides predefined character sets

# Step 1: Create a string of all allowed characters
# Includes space, punctuation, digits, and letters (A–Z, a–z)
chars = " " + string.punctuation + string.digits + string.ascii_letters

# Step 2: Convert the string into a list so it can be shuffled
chars = list(chars)

# Step 3: Create a copy of chars to act as the encryption key
# chars  -> original characters
# key    -> shuffled characters (encrypted mapping)
key = chars.copy()

# Step 4: Randomly shuffle the key list
# This creates a secret mapping between chars and key

random.shuffle(key)

# -------------------- ENCRYPTION --------------------

# Taking normal message as input
plain_text = input('Enter the message to be encrypted: ')

# Empty string to store encrypted text
cipher_text = ""

# Loop through each character in the normal message
for letter in plain_text:
    # Find the index of the character in chars
    index = chars.index(letter)

    # Replace it with the character at same index in key
    cipher_text += key[index]

# Output encrypted message
print(f'Encrypted message: {cipher_text}')



# -------------------- DECRYPTION --------------------

# Taking encrypted message as input
cipher_text = input('Enter the message to be decrypted: ')

# Empty string to store decrypted text
plain_text = ""

# Loop through each character in the encrypted message
for letter in cipher_text:
    # Find the position of the encrypted character in key
    index = key.index(letter)

    # Use the same index to get the original character from chars
    plain_text += chars[index]

# Output decrypted message
print(f'Decrypted message: {plain_text}')
print(f'Encrypted message: {cipher_text}')


