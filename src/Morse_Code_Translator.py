# Python program to implement Morse Code Translator

"""
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
"""

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-',      'B': '-...',   'C': '-.-.',
                   'D': '-..',     'E': '.',      'F': '..-.',
                   'G': '--.',     'H': '....',   'I': '..',
                   'J': '.---',    'K': '-.-',    'L': '.-..',
                   'M': '--',      'N': '-.',     'O': '---',
                   'P': '.--.',    'Q': '--.-',   'R': '.-.',
                   'S': '...',     'T': '-',      'U': '..-',
                   'V': '...-',    'W': '.--',    'X': '-..-',
                   'Y': '-.--',    'Z': '--..',   '1': '.----',
                   '2': '..---',   '3': '...--',  '4': '....-',
                   '5': '.....',   '6': '-....',  '7': '--...',
                   '8': '---..',   '9': '----.',  '0': '-----',
                   ', ': '--..--', '.': '.-.-.-', '?': '..--..',
                   '/': '-..-.',   '-': '-....-', '(': '-.--.',
                   ')': '-.--.-'}

# Function to encrypt the string
# according to the morse code chart


def morse_encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def morse_decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                 # adding space to separate words
                decipher += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher

'''
# Hard-coded driver function to run the program
def main():
    print("Type the message to be encrypted and press ENTER to continue.")
    message = input("")
    encrypted_message = encrypt(message.upper())
    print(encrypted_message)

    # message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
    result = decrypt(encrypted_message)
    print(result)


# Executes the main function
main()


print("Please type a message to encode into Morse code.")
        message = input("")
        encrypted_message = morse_encrypt(message.upper())
        print(encrypted_message)
        
        
print("Please type the message you want converted to Morse code.")
        morse_message = input("")
        decrypted_message = morse_decrypt(morse_message)
        print(decrypted_message)
        print("\nPress Enter to continue.")
        input()
'''


'''

**** OLD SEGMENT OF CODE | PRODUCES ERRORS ****

# Encodes a text string to Morse Code.
def text2morse(message):
    cipher = message
    for letter in message:
        if letter != ' ':
            # if letter in message is '[':
            # letter == '('

            if message_encoding.method_of_encoding == 5:
                # Looks up the dictionary and adds the
                # corresponding morse code
                # along with a space to separate
                # morse codes for different characters
                cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher
'''