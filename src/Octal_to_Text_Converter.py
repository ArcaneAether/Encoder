OCTAL_CODE_DICT = {' ': '040', '!': '041', '"': '042',
                   '#': '043', '$': '044', '%': '045',
                   "&": '046', "'": '047', '(': '050',
                   ')': '051', '*': '052', '+': '053',
                   ',': '054', '-': '055', '.': '056',
                   '/': '057', '0': '060', '1': '061',
                   '2': '062', '3': '063', '4': '064',
                   '5': '065', '6': '066', '7': '067',
                   '8': '070', '9': '071', ':': '072',
                   ';': '073', '<': '074', '=': '075',
                   '>': '076', '?': '077', '@': '100',
                   'A': '101', 'B': '102', 'C': '103',
                   'D': '104', 'E': '105', 'F': '106',
                   'G': '107', 'H': '110', 'I': '111',
                   'J': '112', 'K': '113', 'L': '114',
                   'M': '115', 'N': '116', 'O': '117',
                   'P': '120', 'Q': '121', 'R': '122',
                   'S': '123', 'T': '124', 'U': '125',
                   'V': '126', 'W': '127', 'X': '130',
                   'Y': '131', 'Z': '132', '[': '133',
                   '\\': '134', ']': '135', '^': '136',
                   '_': '137', '`': '140', 'a': '141',
                   'b': '142', 'c': '143', 'd': '144',
                   'e': '145', 'f': '146', 'g': '147',
                   'h': '150', 'i': '151', 'j': '152',
                   'k': '153', 'l': '154', 'm': '155',
                   'n': '156', 'o': '157', 'p': '160',
                   'q': '161', 'r': '162', 's': '163',
                   't': '164', 'u': '165', 'v': '166',
                   'w': '167', 'x': '170', 'y': '171',
                   'z': '173', '{': '174', '|': '175',
                   '}': '176', '~': '177'}

'''
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += OCTAL_CODE_DICT[letter] + ' '
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
                decipher += list(OCTAL_CODE_DICT.keys())[list(OCTAL_CODE_DICT.values()).index(citext)]
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


def octal_encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += OCTAL_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '

    return cipher


def octal_decrypt(message):

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
                decipher += list(OCTAL_CODE_DICT.keys())[list(OCTAL_CODE_DICT.values()).index(citext)]
                citext = ''

    return decipher


'''
print("Please type a message to encode into Octal code.")
        message = input("")
        encrypted_message = octal_encrypt(message)
        print(encrypted_message)
        print("\nPress Enter to continue.")
        input()
        
        
print("Please type the message you want converted from Octal code.")
        octal_message = input("")
        decrypted_message = octal_decrypt(octal_message)
        print(decrypted_message)
        print("\nPress Enter to continue.")
        input()
'''
