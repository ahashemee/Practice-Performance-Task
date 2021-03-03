import math
"""The encryption of the code will go as the following: 
Step 1. Assort each letter of the encrypted message to the pertaining letter in the alphabet using ord
Step 2. Multiply the number by the length of the key
Step 3. Put together each numbeer so that they become a long string, for example, if the message is apple and the key is orange the key at this stage would become: 096967230
Step 4. Convert the string into an integer and create a for loop that is the length of the key. Each time, it will multiply by the number of the letter in the key. For example: 096967230 times o = 14, it will become 1454508450
Step 5. Convert the integer back to a alphabetical string. I will convert every other number to its alphabetical parrallel. 
Step 6. This is the encrypted message. Reverse the steps in order to decrypt the message """
#Testing the commit
#I'm forcing this commit so that I will be able to show my selection in Git
#The following function will be used to encrypt the message the user has provided.
KEY_CONSTANT = "banana"
def encryption_process(unencrypted_message, key):
    if len(unencrypted_message) > 10:
        print("Please keep the message under 10 characters.")
    else:
        for char in key:
            key_number = ord(char)
            numbered_key.append(key_number)
        for num in message:
            message_number = ord(num)
            numbered_message.append(message_number)
        # So far so good, there are no mistakes until here. This covers until step 3. The following is step 4 and on.\
        for num in numbered_message:
            n_e = num * (len(numbered_key) * num)
            numbered_encryption.append(n_e)
        print("The Encrypted Message is: " + str(numbered_encryption))
def introduction():
    print('\n' * 10)
    print("Hello! Welcome to Amaan's message cipher!")
    print("If you would like to encrypt, when prompted, type 'Encrypt' or '1'. If you would like to decrypt a message, type 'Decrypt' or '2'.")
    print("If you would like to exit this terminal, please type 'Break' or '3'")
    print("Thank you :)")
#Decryption Process
"""For the next part you will do the following: Write a decryption function, make sure too add conditionals so no errors can occur in the input section.
Make sure that the if the user just hits enter, make sure to tell them to try again and not to show them the error. Make it so that the user can submit 
as many messages as they like. Try to find the best method to showing the user the key as well as the encrypted message. How would it look best to the judges?
"""
def decrypt_to_list():
    input_string = input('Enter elements of a list separated by space: ')
    user_list = input_string.split()
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
    return user_list

def decryption_process(encrypted_message, key):
    decrypted_list = []
    for num in encrypted_message:
        decrypted_numbers = int(math.sqrt((num / len(key))))
        decrypted_letters = chr(decrypted_numbers)
        decrypted_list.append(decrypted_letters)
    decrypted_tuple = tuple(decrypted_list)
    decrypted_message = ''.join(decrypted_tuple)
    print("The decrypted message is '" + decrypted_message + "'")
introduction()
while True:
    numbered_message = []
    numbered_key = []
    numbered_encryption = []
    key = KEY_CONSTANT
    encrypt_or_decrypt = input("What would you like to do? ")
    if encrypt_or_decrypt == "Encrypt" or encrypt_or_decrypt == "encrypt" or encrypt_or_decrypt == "1":
        message = input("Please enter a message to encrypt: ")
        encryption_process(message, key)
    elif encrypt_or_decrypt == "Decrypt" or encrypt_or_decrypt == "decrypt" or encrypt_or_decrypt == '2':
        decrypt_as_list = decrypt_to_list()
        decryption_process(decrypt_as_list, key)
    elif encrypt_or_decrypt == 'Break' or encrypt_or_decrypt == "break" or encrypt_or_decrypt == '3':
        break
    else:
        print("Please either choose to encrypt, decrypt, or exit the program.")

print("Thank you for using Amaan's Cipher!")