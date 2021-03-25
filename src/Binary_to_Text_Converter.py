BINARY_CODE_DICT = {'0': '00110000', '1': '00110001', '2': '00110010',
                    '3': '00110011', '4': '00110100', '5': '00110101',
                    '6': '00110110', '7': '00110111', '8': '00111000',
                    '9': '00111001', '`': '01100000', '~': '01111110',
                    '!': '00100001', '@': '01000000', '#': '00100011',
                    '$': '00100100', '%': '00100101', '^': '01011110',
                    '&': '00100110', '*': '00101010', '(': '00101000',
                    ')': '00101001', '-': '00101101', '_': '01011111',
                    '=': '00111101', '+': '00101011', '[': '01011011',
                    ']': '01011101', '{': '01111011', '}': '01111101',
                    '\\': '01011100', '|': '01111100', ';': '00111011',
                    ':': '00111010', '"': '00100010', "'": '00100111',
                    ',': '00101100', '.': '00101110', '/': '00101111',
                    '<': '00111100', '>': '00111110', '?': '00111111',
                    'a': '01100001', 'b': '01100010', 'c': '01100011',
                    'd': '01100100', 'e': '01100101', 'f': '01100110',
                    'g': '01100111', 'h': '01101000', 'i': '01101001',
                    'j': '01101010', 'k': '01101011', 'l': '01101100',
                    'm': '01101101', 'n': '01101110', 'o': '01101111',
                    'p': '01110000', 'q': '01110001', 'r': '01110010',
                    's': '01110011', 't': '01110100', 'u': '01110101',
                    'v': '01110110', 'w': '01110111', 'x': '01111000',
                    'y': '01111001', 'z': '01111010', 'A': '01000001',
                    'B': '01000010', 'C': '01000011', 'D': '01000100',
                    'E': '01000101', 'F': '01000110', 'G': '01000111',
                    'H': '01001000', 'I': '01001001', 'J': '01001010',
                    'K': '01001011', 'L': '01001100', 'M': '01001101',
                    'N': '01001110', 'O': '01001111', 'P': '01010000',
                    'Q': '01010001', 'R': '01010010', 'S': '01010011',
                    'T': '01010100', 'U': '01010101', 'V': '01010110',
                    'W': '01010111', 'X': '01011000', 'Y': '01011001',
                    'Z': '01011010', '00000000': '[NULL]'}


'''
print("Please type your message you want to encode.")
encode_text = input("")
for i in encode_text:
    text_to_binary = bin(ord(i))  # Used to encode text to binary
    print(text_to_binary[2:], end=' ')
print("\nPress Enter to continue.")
input()



def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += BINARY_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    i = int()
    for letter in message:

        # checks for space
        if letter != ' ':

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
                decipher += list(BINARY_CODE_DICT.keys())[list(BINARY_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


# Hard-coded driver function to run the program
def main():
    print("Type the message to be encrypted and press ENTER to continue.")
    message = input('''''')
    encrypted_message = encrypt(message)
    print(encrypted_message)
    file1 = open("myfile.txt", "w")
    file1.write(encrypted_message)

    # message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
    result = decrypt(encrypted_message)
    print(result)


# Executes the main function
main()
'''


def binary_encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += BINARY_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


def binary_decrypt(message):

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    i = int()
    for letter in message:

        # checks for space
        if letter != ' ':

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
                decipher += list(BINARY_CODE_DICT.keys())[list(BINARY_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


'''
print("Please type a message to encode into Binary code.")
        message = input("")
        encrypted_message = binary_encrypt(message)
        print(encrypted_message)
        print("\nPress Enter to continue.")
        input()
'''
