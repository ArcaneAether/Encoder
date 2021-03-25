"""
VERSION 5

This update implements read/write functions to files. This version reformatted the termination process during the
encoding and decoding processes, allowing the user to exit the program immediately or return to the main menu to
continue browsing.

"""
# from terminaltables import *
from Code_Converter import *
from Binary_to_Text_Converter import *
from Octal_to_Text_Converter import *
from Conversion_Lists import *
from time import sleep
from os import system


def clear_screen():  # Used to clear the screen of prior text.
    system('cls')


# clear_screen()
encoded_message = []
decoded_message = []


def title():
    print('''                                       
                              #############################################################
                              #                                                           #
    --------------------------# This program is for encoding and decoding strings of text #----------------------------
                              #                                                           #
                              #############################################################
    ''')
    sleep(2)


def main():

    while True:
        print("\nWhat would you like to do?")
        print("(1) : Encode text\n(2) : Decode text\n(3) : See character conversion lists\n(4) : Quit program.")

        answer = input("\n>>> ")

        if answer == "1":
            print("\nPlease type the message you would like to be encoded.")
            message_encoding()
        elif answer == "2":
            print("\nPlease input the encoded message you would like decode to plain text.")
            message_decoding()
        elif answer == "3":
            conversion_lists()
        elif answer == "4":
            print("\nGoodbye!")
            sleep(0.5)
            exit()
        else:
            print("Invalid selection! Please choose a different option.\n")


def conversion_lists():
    print('''\nWhat character conversion tables would you like to see?
<Conversion Tables>\n1 : ASCII Table\n2 : Binary\n3 : Hexadecimal\n4 : Octal\n5 : Decimal/Ordinal\n6 : Morse Code
99 : Return to the main menu
\n*Note: The ASCII Table shows all code conversions; whereas, the other options show the specific conversion tables.
''')
    selection = input(">>> ")

    if selection == '1':
        ascii_table()
        print("\nPress ENTER to continue.\n")
        input(">>> ")
    elif selection == '2':
        bin_table()
        print("\nPress ENTER to continue.\n")
        input(">>> ")
    elif selection == '3':
        hex_table()
        print("\nPress ENTER to continue.\n")
        input(">>> ")
    elif selection == '4':
        oct_table()
        print("\nPress ENTER to continue.\n")
        input(">>> ")
    elif selection == '5':
        ord_table()
        print("\nPress ENTER to continue.\n")
        input(">>> ")
    elif selection == '6':
        morse_table()
        print("\nPress ENTER to continue.\n")
        input(">>> ")
    elif selection == '99':
        main()
    else:
        print("\n>>>Invalid selection | Select a valid option<<<\n")
        # clear_screen()
        conversion_lists()


def message_encoding():
    print('''\nHow would you like to encode your message?
(1) : Binary\n(2) : Hexadecimal\n(3) : Octal\n(4) : Ordinal\n(5) : Morse Code\n(99) : Return to main menu''')
    method_of_encoding = input(">>> ").lower()

    if method_of_encoding == '1':
        print("\nPlease type a message to encode into Binary code.")
        message = input("")
        encrypted_message = binary_encrypt(message)
        print(encrypted_message)
        with open("D:/user_binary_encrypted_message_data_file.rtf", "w") as f:
            f.writelines(encrypted_message)
            f.close()
        termination_decision()
    elif method_of_encoding == '2':
        print("\nPlease type your message you want to encode into hexadecimal.")
        encoded_text = input("")
        for i in encoded_text:
            # text_to_ord = ord(i)
            # print(text_to_ord, end='')
            # Used to encode text to hexadecimal
            text_to_hex = hex(ord(i))
            # end=' ' replaces the default value of end with a space (all conversions printed on same line)
            print(text_to_hex[2:], end=' ')

            encoded_message.append(text_to_hex)
        with open("D:/user_hexadecimal_encrypted_message_data_file.rtf", "w") as f:
            f.writelines(encoded_message)
            f.close()
        termination_decision()
    elif method_of_encoding == '3':
        print("\nPlease type a message to encode into Octal code.")
        message = input("")
        encrypted_message = octal_encrypt(message)
        print(encrypted_message)
        with open("D:/user_octal_encrypted_message_data_file.rtf", "w") as f:
            f.writelines(encrypted_message)
            f.close()
        termination_decision()
    elif method_of_encoding == '4':
        print("\nPlease type your message you want to encode into ordinal.")
        encoded_text = input("")
        # for i in encoded_text:
        # print(ord(i), end=' ')   # Used to encode text to ordinal
        ordinal_message = [int(ord(c)) for c in encoded_text]
        print(ordinal_message)
        with open("D:/user_ordinal_encrypted_message_data_file.rtf", "w") as f:
            f.writelines(encoded_message)
            f.close()
        termination_decision()
    elif method_of_encoding == "5":
        print("\nPlease type a message to encode into Morse code.")
        message = input(">>> ")
        encrypted_message = text2morse(message.upper())
        with open("D:/user_morse_encrypted_message_data_file.rtf", "w") as f:
            f.writelines(encrypted_message)
            f.close()
        termination_decision()
    elif method_of_encoding == "99":
        main()
    else:
        print("\nSelect a different method.")
        message_encoding()


def message_decoding():
    print('''\nSelect which format your message is encoded in. | (e.g.- If your message is encoded in hexadecimal,
select hexadecimal.)
(1) : Binary\n(2) : Hexadecimal\n(3) : Octal\n(4) : Ordinal\n(5) : Morse Code\n(99) : Return to main menu''')
    type_of_encoding = input(">>> ")

    if type_of_encoding == "1":
        print("\nPlease type the message you want converted from Binary code.")
        binary_message = input("")
        decrypted_message = binary_decrypt(binary_message)
        print(decrypted_message)
        with open("D:/user_binary_decoded_message_data_file.rtf", "w") as f:
            f.writelines(decoded_message)
            f.close()
        termination_decision()
    elif type_of_encoding == "2":
        print("\nPlease type the message you want to decode from hexadecimal to text.")
        message_to_decode = input("")
        hex_to_text = bytearray.fromhex(message_to_decode).decode()  # Used to decode text to hexadecimal
        print(hex_to_text, end=' ')
        decoded_message.append(hex_to_text)
        with open("D:/user_hexadecimal_decoded_message_data_file.rtf", "w") as f:
            f.writelines(decoded_message)
            f.close()
    elif type_of_encoding == "3":
        print("\nPlease type the message you want converted from Octal code.")
        octal_message = input("")
        decrypted_message = octal_decrypt(octal_message)
        print(decrypted_message)
        with open("D:/user_octal_decoded_message_data_file.rtf", "w") as f:
            f.writelines(decoded_message)
            f.close()
    elif type_of_encoding == "4":
        print("\nPlease type the message you want to decode from ordinal to text.")
        encoded_string = input("")
        encoded_string = encoded_string.strip('[]')
        message_to_decode = [int(s) for s in encoded_string.split(',')]
        char = [chr(x) for x in message_to_decode]
        ordinal_to_text = ''.join(char)
        print(ordinal_to_text)
        with open("D:/user_ordinal_decoded_message_data_file.rtf", "w") as f:
            f.writelines(decoded_message)
            f.close()
    elif type_of_encoding == "5":
        print("\nPlease type the message you want converted to Morse code.")
        morse_message = input("")
        decrypted_message = morse2text(morse_message)
        print(decrypted_message)
        with open("D:/user_morse_decoded_message_data_file.rtf", "w") as f:
            f.writelines(decoded_message)
            f.close()
    elif type_of_encoding == "99":
        main()

    else:
        print("\nInvalid option. Please select a valid option")


def termination_decision():
    print("\nWould you like exit this program or continue back to the main menu?")
    print("(1) Exit program \n(2) Continue to main menu")
    decision = input(">>> ").lower()
    for user_decision in decision:
        if user_decision == "1":
            print("\nGoodbye!")
            sleep(1)
            exit()
            return False
        elif user_decision == "2":
            # print("\nPress Enter to continue.")
            # input()
            main()
            return False
        else:
            print("Invalid selection! Please select a different option.")
            termination_decision()


'''
encoded_message = []
decoded_message = []
'''

title()
main()
input("Press ENTER to continue.")
