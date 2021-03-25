from terminaltables import *


def ascii_table():
    print('''                           
               _     ____    ____  ___  ___    _____       _      _        
              / \   / ___|  / ___||_ _||_ _|  |_   _|__ _ | |__  | |  ___ 
             / _ \  \___ \ | |     | |  | |     | | / _` || '_ \ | | / _ \ 
            / ___ \  ___) || |___  | |  | |     | || (_| || |_) || ||  __/
           /_/   \_\|____/  \____||___||___|    |_| \__,_||_.__/ |_| \___|''')

    ascii_data = (
        (['Decimal/Ordinal', 'Binary', 'Hexadecimal', 'Octal', 'Morse Code', 'Character']),
        ([0, '00000000', '00', '000', '', '[NULL]']),
        ([1, '00000001', '01', '001', '', '[START OF HEADING]']),
        ([2, '00000010', '02', '002', '', '[START OF TEXT]']),
        ([3, '00000011', '03', '003', '', '[END OF TEXT]']),
        ([4, '00000100', '04', '004', '', '[END OF TRANSMISSION]']),
        ([5, '00000101', '05', '005', '', '[ENQUIRY]']),
        ([6, '00000110', '06', '006', '', '[ACKNOWLEDGE]']),
        ([7, '00000111', '07', '007', '', '[BELL]']),
        ([8, '00001000', '08', '010', '', '[BACKSPACE]']),
        ([9, '00001001', '09', '011', '', '[HORIZONTAL TAB]']),
        ([10, '00001010', '0A', '012', '', '[LINE FEED]']),
        ([11, '00001011', '0B', '013', '', '[VERTICAL TAB]']),
        ([12, '00001100', '0C', '014', '', '[FROM FEED]']),
        ([13, '00001101', '0D', '015', '', '[CARRIAGE RETURN]']),
        ([14, '00001110', '0E', '016', '', '[SHIFT OUT]']),
        ([15, '00001111', '0F', '017', '', '[SHIFT IN]']),
        ([16, '00010000', '10', '020', '', '[DATA LINK ESCAPE]']),
        ([17, '00010001', '11', '021', '', '[DEVICE CONTROL 1]']),
        ([18, '00010010', '12', '022', '', '[DEVICE CONTROL 2]']),
        ([19, '00010011', '13', '023', '', '[DEVICE CONTROL 3]']),
        ([20, '00010100', '14', '024', '', '[DEVICE CONTROL 4]']),
        ([21, '00010101', '15', '025', '', '[NEGATIVE ACKNOWLEDGE]']),
        ([22, '00010110', '16', '026', '', '[SYNCHRONOUS IDLE]']),
        ([23, '00010111', '17', '027', '', '[END OF TRANS. BLOCK]']),
        ([24, '00011000', '18', '030', '', '[CANCEL]']),
        ([25, '00011001', '19', '031', '', '[END OF MEDIUM]']),
        ([26, '00011010', '1A', '032', '', '[SUBSTITUTE]']),
        ([27, '00011011', '1B', '033', '', '[ESCAPE]']),
        ([28, '00011100', '1C', '034', '', '[FILE SEPARATOR]']),
        ([29, '00011101', '1D', '035', '', '[GROUP SEPARATOR]']),
        ([30, '00011110', '1E', '036', '', '[RECORD SEPARATOR]']),
        ([31, '00011111', '1F', '037', '', '[UNIT SEPARATION]']),
        ([32, '00100000', '20', '040', '', '[SPACE]']),
        ([33, '00100001', '21', '041', '-.-.--', '!']),
        ([34, '00100010', '22', '042', '.-..-.', '\"']),
        ([35, '00100011', '23', '043', '', '#']),
        ([36, '00100100', '24', '044', '...-..-', '$']),
        ([37, '00100101', '25', '045', '', '%']),
        ([38, '00100110', '26', '046', '.-...', '&']),
        ([39, '00100111', '27', '047', '.----.', '\'']),
        ([40, '00101000', '28', '050', '-.--.', '(']),
        ([41, '00101001', '29', '051', '-.--.-', ')']),
        ([42, '00101010', '2A', '052', '-..-', '*']),
        ([43, '00101011', '2B', '053', '.-.-.', '+']),
        ([44, '00101100', '2C', '054', '--..--', ',']),
        ([45, '00101101', '2D', '055', '-....-', '-']),
        ([46, '00101110', '2E', '056', '.-.-.-', '.']),
        ([47, '00101111', '2F', '057', '-..-.', '/']),
        ([48, '00110000', '30', '060', '-----', 0]),
        ([49, '00110001', '31', '061', '.----', 1]),
        ([50, '00110010', '32', '062', '..---', 2]),
        ([51, '00110011', '33', '063', '...--', 3]),
        ([52, '00110100', '34', '064', '....-', 4]),
        ([53, '00110101', '35', '065', '.....', 5]),
        ([54, '00110110', '36', '066', '-....', 6]),
        ([55, '00110111', '37', '067', '--...', 7]),
        ([56, '00111000', '38', '070', '---..', 8]),
        ([57, '00111001', '39', '071', '----.', 9]),
        ([58, '00111010', '3A', '072', '---...', ':']),
        ([59, '00111011', '3B', '073', '-.-.-.', ';']),
        ([60, '00111100', '3C', '074', '', '<']),
        ([61, '00111101', '3D', '075', '-...-', '=']),
        ([62, '00111110', '3E', '076', '', '>']),
        ([63, '00111111', '3F', '077', '..--..', '?']),
        ([64, '01000000', '40', '100', '.--.-.', '@']),
        ([65, '01000001', '41', '101', '.-', 'A']),
        ([66, '01000010', '42', '102', '-...', 'B']),
        ([67, '01000011', '43', '103', '-.-.', 'C']),
        ([68, '01000100', '44', '104', '-..', 'D']),
        ([69, '01000101', '45', '105', '.', 'E']),
        ([70, '01000110', '46', '106', '..-.', 'F']),
        ([71, '01000111', '47', '107', '--.', 'G']),
        ([72, '01001000', '48', '110', '....', 'H']),
        ([73, '01001001', '49', '111', '..', 'I']),
        ([74, '01001010', '4A', '112', '.---', 'J']),
        ([75, '01001011', '4B', '113', '-.-', 'K']),
        ([76, '01001100', '4C', '114', '.-..', 'L']),
        ([77, '01001101', '4D', '115', '--', 'M']),
        ([78, '01001110', '4E', '116', '-.', 'N']),
        ([79, '01001111', '4F', '117', '---', 'O']),
        ([80, '01010000', '50', '120', '.--.', 'P']),
        ([81, '01010001', '51', '121', '--.-', 'Q']),
        ([82, '01010010', '52', '122', '.-.', 'R']),
        ([83, '01010011', '53', '123', '...', 'S']),
        ([84, '01010100', '54', '124', '-', 'T']),
        ([85, '01010101', '55', '125', '..-', 'U']),
        ([86, '01010110', '56', '126', '...-', 'V']),
        ([87, '01010111', '57', '127', '.--', 'W']),
        ([88, '01011000', '58', '130', '-..-', 'X']),
        ([89, '01011001', '59', '131', '-.--', 'Y']),
        ([90, '01011010', '5A', '132', '--..', 'Z']),
        ([91, '01011011', '5B', '133', '-.--.', '[']),
        ([92, '01011100', '5C', '134', '', '\\']),
        ([93, '01011101', '5D', '135', '-.--.-', ']']),
        ([94, '01011110', '5E', '136', '', '^']),
        ([95, '01011111', '5F', '137', '..--.-', '_']),
        ([96, '01100000', '60', '140', '', '`']),
        ([97, '01100001', '61', '141', '*(2)*', 'a']),
        ([98, '01100010', '62', '142', '*(2)*', 'b']),
        ([99, '01100011', '63', '143', '*(2)*', 'c']),
        ([100, '01100100', '64', '144', '*(2)*', 'd']),
        ([101, '01100101', '65', '145', '*(2)*', 'e']),
        ([102, '01100110', '66', '146', '*(2)*', 'f']),
        ([103, '01100111', '67', '147', '*(2)*', 'g']),
        ([104, '01101000', '68', '150', '*(2)*', 'h']),
        ([105, '01101001', '69', '151', '*(2)*', 'i']),
        ([106, '01101010', '6A', '152', '*(2)*', 'j']),
        ([107, '01101011', '6B', '153', '*(2)*', 'k']),
        ([108, '01101100', '6C', '154', '*(2)*', 'l']),
        ([109, '01101101', '6D', '155', '*(2)*', 'm']),
        ([110, '01101110', '6E', '156', '*(2)*', 'n']),
        ([111, '01101111', '6F', '157', '*(2)*', 'o']),
        ([112, '01110000', '70', '160', '*(2)*', 'p']),
        ([113, '01110001', '71', '161', '*(2)*', 'q']),
        ([114, '01110010', '72', '162', '*(2)*', 'r']),
        ([115, '01110011', '73', '163', '*(2)*', 's']),
        ([116, '01110100', '74', '164', '*(2)*', 't']),
        ([117, '01110101', '75', '165', '*(2)*', 'u']),
        ([118, '01110110', '76', '166', '*(2)*', 'v']),
        ([119, '01110111', '77', '167', '*(2)*', 'w']),
        ([120, '01111000', '78', '170', '*(2)*', 'x']),
        ([121, '01111001', '79', '171', '*(2)*', 'y']),
        ([122, '01111010', '7A', '172', '*(2)*', 'z']),
        ([123, '01111011', '7B', '173', '*(2)*', '{']),
        ([124, '01111100', '7C', '174', '*(2)*', '|']),
        ([125, '01111101', '7D', '175', '*(2)*', '}']),
        ([126, '01111110', '7E', '176', '*(2)*', '~']),
        ([127, '01111111', '7F', '177', '*(2)*', '[DEL]']),
    )

    code_instance = SingleTable(ascii_data)  # Generates the table
    # code_instance.title = 'ASCII Table' -- Gives the table a title

    code_instance.inner_column_border = True  # When set to True, there are dividing lines for every column.
    # When set to False, there are no dividing lines.

    code_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
    # This centers the text in the columns
    # Column Key:
    # 0: Decimal/Ordinal
    # 1: Binary
    # 2: Hexadecimal
    # 3: Octal
    # 4: Morse Code
    # 5: Characters

    code_instance.padding_left = 1  # Number of spaces to pad on the right side of every cell. Padding adds spacing
    # between the cell text and the column border.
    print(code_instance.table)
    print("Notes:\n")
    print('''(1): Morse Code is not part of the standard ASCII table. International Morse Code is used here. ''')
    print('''(2): Morse Code is traditionally used in all caps or all lower case letter. The morse code values are
       the same for both capital and lower case levels.''')
    print('''(3): There are no Morse Code conversions for Character Controls.''')


def ord_table():
    print('''
                 ___            _  _                _    _____       _      _        
                / _ \  _ __  __| |(_) _ __    __ _ | |  |_   _|__ _ | |__  | |  ___ 
               | | | || '__|/ _` || || '_ \  / _` || |    | | / _` || '_ \ | | / _ \ 
               | |_| || |  | (_| || || | | || (_| || |    | || (_| || |_) || ||  __/
                \___/ |_|   \__,_||_||_| |_| \__,_||_|    |_| \__,_||_.__/ |_| \___|                                                           
    ''')
    ord_data = (
        (['Decimal/Ordinal', 'Character', 'Decimal/Ordinal', 'Character', 'Decimal/Ordinal', 'Character']),
        ([0, '[NULL]', 43, '+', 86, 'V']),
        ([1, '[START OF HEADING]', 44, ',', 87, 'W']),
        ([2, '[START OF TEXT]', 45, '-', 88, 'X']),
        ([3, '[END OF TEXT]', 46, '.', 89, 'Y']),
        ([4, '[END OF TRANSMISSION]', 47, '/', 90, 'Z']),
        ([5, '[ENQUIRY]', 48, 0, 91, '[']),
        ([6, '[ACKNOWLEDGE]', 49, 1, 92, '\\']),
        ([7, '[BELL]', 50, 2, 93, ']']),
        ([8, '[BACKSPACE]', 51, 3, 94, '^']),
        ([9, '[HORIZONTAL TAB]', 52, 4, 95, '_']),
        ([10, '[LINE FEED]', 53, 5, 96, '`']),
        ([11, '[VERTICAL TAB]', 54, 6, 97, 'a']),
        ([12, '[FROM FEED]', 55, 7, 98, 'b']),
        ([13, '[CARRIAGE RETURN]', 56, 8, 99, 'c']),
        ([14, '[SHIFT OUT]', 57, 9, 100, 'd']),
        ([15, '[SHIFT IN]', 58, ':', 101, 'e']),
        ([16, '[DATA LINK ESCAPE]', 59, ';', 102, 'f']),
        ([17, '[DEVICE CONTROL 1]', 60, '<', 103, 'g']),
        ([18, '[DEVICE CONTROL 2]', 61, '=', 104, 'h']),
        ([19, '[DEVICE CONTROL 3]', 62, '>', 105, 'i']),
        ([20, '[DEVICE CONTROL 4]', 63, '?', 106, 'j']),
        ([21, '[NEGATIVE ACKNOWLEDGE]', 64, '@', 107, 'k']),
        ([22, '[SYNCHRONOUS IDLE]', 65, 'A', 108, 'l']),
        ([23, '[END OF TRANS. BLOCK ]', 66, 'B', 109, 'm']),
        ([24, '[CANCEL]', 67, 'C', 110, 'n']),
        ([25, '[END OF MEDIUM]', 68, 'D', 111, 'o']),
        ([26, '[SUBSTITUTE]', 69, 'E', 112, 'p']),
        ([27, '[ESCAPE]', 70, 'F', 113, 'q']),
        ([28, '[FILE SEPARATOR]', 71, 'G', 114, 'r']),
        ([29, '[GROUP SEPARATOR]', 72, 'H', 115, 's']),
        ([30, '[RECORD SEPARATOR]', 73, 'I', 116, 't']),
        ([31, '[UNIT SEPARATION]', 74, 'J', 117, 'u']),
        ([32, '[SPACE]', 75, 'K', 118, 'v']),
        ([33, '!', 76, 'L', 119, 'w']),
        ([34, '\"', 77, 'M', 120, 'x']),
        ([35, '#', 78, 'N', 121, 'y']),
        ([36, '$', 79, 'O', 122, 'z']),
        ([37, '%', 80, 'P', 123, '{']),
        ([38, '&', 81, 'Q', 124, '|']),
        ([39, '\'', 82, 'R', 125, '}']),
        ([40, '(', 83, 'S', 126, '~']),
        ([41, ')', 84, 'T', 127, '[DEL]']),
        ([42, '*', 85, 'U']),
    )

    code_instance = SingleTable(ord_data)  # Generates the table
    # code_instance.title = 'ASCII Table' -- Gives the table a title

    code_instance.inner_column_border = True  # When set to True, there are dividing lines for every column.
    # When set to False, there are no dividing lines.

    code_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center'}
    # This centers the text in the columns
    # Column Key:
    # 0: Decimal/Ordinal
    # 1: Characters

    code_instance.padding_left = 1  # Number of spaces to pad on the right side of every cell. Padding adds spacing
    # between the cell text and the column border.
    print(code_instance.table)


def bin_table():
    print('''
       ____   _                               _____       _      _        
      | __ ) (_) _ __    __ _  _ __  _   _   |_   _|__ _ | |__  | |  ___ 
      |  _ \ | || '_ \  / _` || '__|| | | |    | | / _` || '_ \ | | / _ \ 
      | |_) || || | | || (_| || |   | |_| |    | || (_| || |_) || ||  __/
      |____/ |_||_| |_| \__,_||_|    \__, |    |_| \__,_||_.__/ |_| \___|
                                     |___/                                 ''')
    bin_data = (
        (['Binary', 'Character', 'Binary', 'Character', 'Binary', 'Character']),
        (['00000000', '[NULL]', '00101011', '+', '01010110', 'V']),
        (['00000001', '[START OF HEADING]', '00101100', ',', '01010111', 'W']),
        (['00000010', '[START OF TEXT]', '00101101', '-', '01011000', 'X']),
        (['00000011', '[END OF TEXT]', '00101110', '.', '01011001', 'Y']),
        (['00000100', '[END OF TRANSMISSION]', '00101111', '/', '01011010', 'Z']),
        (['00000101', '[ENQUIRY]', '00110000', 0, '01011011', '[']),
        (['00000110', '[ACKNOWLEDGE]', '00110001', 1, '01011100', '\\']),
        (['00000111', '[BELL]', '00110010', 2, '01011101', ']']),
        (['00001000', '[BACKSPACE]', '00110011', 3, '01011110', '^']),
        (['00001001', '[HORIZONTAL TAB]', '00110100', 4, '01011111', '_']),
        (['00001010', '[LINE FEED]', '00110101', 5, '01100000', '`']),
        (['00001011', '[VERTICAL TAB]', '00110110', 6, '01100001', 'a']),
        (['00001100', '[FROM FEED]', '00110111', 7, '01100010', 'b']),
        (['00001101', '[CARRIAGE RETURN]', '00111000', 8, '01100011', 'c']),
        (['00001110', '[SHIFT OUT]', '00111001', 9, '01100100', 'd']),
        (['00001111', '[SHIFT IN]', '00111010', ':', '01100101', 'e']),
        (['00010000', '[DATA LINK ESCAPE]', '00111011', ';', '01100110', 'f']),
        (['00010001', '[DEVICE CONTROL 1]', '00111100', '<', '01100111', 'g']),
        (['00010010', '[DEVICE CONTROL 2]', '00111101', '=', '01101000', 'h']),
        (['00010011', '[DEVICE CONTROL 3]', '00111110', '>', '01101001', 'i']),
        (['00010100', '[DEVICE CONTROL 4]', '00111111', '?', '01101010', 'j']),
        (['00010101', '[NEGATIVE ACKNOWLEDGE]', '01000000', '@', '01101011', 'k']),
        (['00010110', '[SYNCHRONOUS IDLE]', '01000001', 'A', '01101100', 'l']),
        (['00010111', '[END OF TRANS. BLOCK]', '01000010', 'B', '01101101', 'm']),
        (['00011000', '[CANCEL]', '01000011', 'C', '01101110', 'n']),
        (['00011001', '[END OF MEDIUM]', '01000100', 'D', '01101111', 'o']),
        (['00011010', '[SUBSTITUTE]', '01000101', 'E', '01110000', 'p']),
        (['00011011', '[ESCAPE]', '01000110', 'F', '01110001', 'q']),
        (['00011100', '[FILE SEPARATOR]', '01000111', 'G', '01110010', 'r']),
        (['00011101', '[GROUP SEPARATOR]', '01001000', 'H', '01110011', 's']),
        (['00011110', '[RECORD SEPARATOR]', '01001001', 'I', '01110100', 't']),
        (['00011111', '[UNIT SEPARATION]', '01001010', 'J', '01110101', 'u']),
        (['00100000', '[SPACE]', '01001011', 'K', '01110110', 'v']),
        (['00100001', '!', '01001100', 'L', '01110111', 'w']),
        (['00100010', '\"', '01001101', 'M', '01111000', 'x']),
        (['00100011', '#', '01001110', 'N', '01111001', 'y']),
        (['00100100', '$', '01001111', 'O', '01111010', 'z']),
        (['00100101', '%', '01010000', 'P', '01111011', '{']),
        (['00100110', '&', '01010001', 'Q', '01111100', '|']),
        (['00100111', '\'', '01010010', 'R', '01111101', '}']),
        (['00101000', '(', '01010011', 'S', '01111110', '~']),
        (['00101001', ')', '01010100', 'T', '01111111', '[DEL]']),
        (['00101010', '*', '01010101', 'U', ]),
    )

    code_instance = SingleTable(bin_data)  # Generates the table
    # code_instance.title = 'ASCII Table' -- Gives the table a title

    code_instance.inner_column_border = True  # When set to True, there are dividing lines for every column.
    # When set to False, there are no dividing lines.

    code_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center'}
    # This centers the text in the columns
    # Column Key:
    # 0: Decimal/Ordinal
    # 1: Characters
    # 2: Decimal/Ordinal
    # 3: Characters
    # 4: Decimal/Ordinal
    # 5: Characters

    code_instance.padding_left = 1  # Number of spaces to pad on the right side of every cell. Padding adds spacing
    # between the cell text and the column border.
    print(code_instance.table)


def hex_table():
    print('''
  _   _                          _              _                    _    _____       _      _        
 | | | |  ___  __  __  __ _   __| |  ___   ___ (_) _ __ ___    __ _ | |  |_   _|__ _ | |__  | |  ___ 
 | |_| | / _ \ \ \/ / / _` | / _` | / _ \ / __|| || '_ ` _ \  / _` || |    | | / _` || '_ \ | | / _ \ 
 |  _  ||  __/  >  < | (_| || (_| ||  __/| (__ | || | | | | || (_| || |    | || (_| || |_) || ||  __/
 |_| |_| \___| /_/\_\ \__,_| \__,_| \___| \___||_||_| |_| |_| \__,_||_|    |_| \__,_||_.__/ |_| \___|''')
    hex_data = (
        (['Hexadecimal', 'Character', 'Hexadecimal', 'Character', 'Hexadecimal', 'Character']),
        (['00', '[NULL]', '2B', '+', '56', 'V']),
        (['01', '[START OF HEADING]', '2C', ',', '57', 'W']),
        (['02', '[START OF TEXT]', '2D', '-', '58', 'X']),
        (['03', '[END OF TEXT]', '2E', '.', '59', 'Y']),
        (['04', '[END OF TRANSMISSION]', '2F', '/', '5A', 'Z']),
        (['05', '[ENQUIRY]', '30', 0, '5B', '[']),
        (['06', '[ACKNOWLEDGE]', '31', 1, '5C', '\\']),
        (['07', '[BELL]', '32', 2, '5D', ']']),
        (['08', '[BACKSPACE]', '33', 3, '5E', '^']),
        (['09', '[HORIZONTAL TAB]', '34', 4, '5F', '_']),
        (['0A', '[LINE FEED]', '35', 5, '60', '`']),
        (['0B', '[VERTICAL TAB]', '36', 6, '61', 'a']),
        (['0C', '[FROM FEED]', '37', 7, '62', 'b']),
        (['0D', '[CARRIAGE RETURN]', '38', 8, '63', 'c']),
        (['0E', '[SHIFT OUT]', '39', 9, '64', 'd']),
        (['0F', '[SHIFT IN]', '3A', ':', '65', 'e']),
        (['10', '[DATA LINK ESCAPE]', '3B', ';', '66', 'f']),
        (['11', '[DEVICE CONTROL 1]', '3C', '<', '67', 'g']),
        (['12', '[DEVICE CONTROL 2]', '3D', '=', '68', 'h']),
        (['13', '[DEVICE CONTROL 3]', '3E', '>', '69', 'i']),
        (['14', '[DEVICE CONTROL 4]', '3F', '?', '6A', 'j']),
        (['15', '[NEGATIVE ACKNOWLEDGE]', '40', '@', '6B', 'k']),
        (['16', '[SYNCHRONOUS IDLE]', '41', 'A', '6C', 'l']),
        (['17', '[END OF TRANS. BLOCK]', '42', 'B', '6D', 'm']),
        (['18', '[CANCEL]', '43', 'C', '6E', 'n']),
        (['19', '[END OF MEDIUM]', '44', 'D', '6F', 'o']),
        (['1A', '[SUBSTITUTE]', '45', 'E', '70', 'p']),
        (['1B', '[ESCAPE]', '46', 'F', '71', 'q']),
        (['1C', '[FILE SEPARATOR]', '47', 'G', '72', 'r']),
        (['1D', '[GROUP SEPARATOR]', '48', 'H', '73', 's']),
        (['1E', '[RECORD SEPARATOR]', '49', 'I', '74', 't']),
        (['1F', '[UNIT SEPARATION]', '4A', 'J', '75', 'u']),
        (['20', '[SPACE]', '4B', 'K', '76', 'v']),
        (['21', '!', '4C', 'L', '77', 'w']),
        (['22', '\"', '4D', 'M', '78', 'x']),
        (['23', '#', '4E', 'N', '79', 'y']),
        (['24', '$', '4F', 'O', '7A', 'z']),
        (['25', '%', '50', 'P', '7B', '{']),
        (['26', '&', '51', 'Q', '7C', '|']),
        (['27', '\'', '52', 'R', '7D', '}']),
        (['28', '(', '53', 'S', '7E', '~']),
        (['29', ')', '54', 'T', '7F', '[DEL]']),
        (['2A', '*', '55', 'U', ]),
    )

    code_instance = SingleTable(hex_data)  # Generates the table
    # code_instance.title = 'ASCII Table' -- Gives the table a title

    code_instance.inner_column_border = True  # When set to True, there are dividing lines for every column.
    # When set to False, there are no dividing lines.

    code_instance.justify_columns = {0: 'center', 1: 'center'}
    # This centers the text in the columns
    # Column Key:
    # 0: Hexadecimal
    # 1: Characters

    code_instance.padding_left = 1  # Number of spaces to pad on the right side of every cell. Padding adds spacing
    # between the cell text and the column border.
    print(code_instance.table)


def oct_table():
    print('''
           ___         _           _    _____       _      _        
          / _ \   ___ | |_   __ _ | |  |_   _|__ _ | |__  | |  ___ 
         | | | | / __|| __| / _` || |    | | / _` || '_ \ | | / _ \ 
         | |_| || (__ | |_ | (_| || |    | || (_| || |_) || ||  __/
          \___/  \___| \__| \__,_||_|    |_| \__,_||_.__/ |_| \___|''')
    oct_data = (
        (['Octal', 'Character', 'Octal', 'Character', 'Octal', 'Character']),
        (['000', '[NULL]', '053', '+', '126', 'V']),
        (['001', '[START OF HEADING]', '054', ',', '127', 'W']),
        (['002', '[START OF TEXT]', '055', '-', '130', 'X']),
        (['003', '[END OF TEXT]', '056', '.', '131', 'Y']),
        (['004', '[END OF TRANSMISSION]', '057', '/', '132', 'Z']),
        (['005', '[ENQUIRY]', '060', 0, '133', '[']),
        (['006', '[ACKNOWLEDGE]', '061', 1, '134', '\\']),
        (['007', '[BELL]', '062', 2, '135', ']']),
        (['010', '[BACKSPACE]', '063', 3, '136', '^']),
        (['011', '[HORIZONTAL TAB]', '064', 4, '137', '_']),
        (['012', '[LINE FEED]', '065', 5, '140', '`']),
        (['013', '[VERTICAL TAB]', '066', 6, '141', 'a']),
        (['014', '[FROM FEED]', '067', 7, '142', 'b']),
        (['015', '[CARRIAGE RETURN]', '070', 8, '143', 'c']),
        (['016', '[SHIFT OUT]', '071', 9, '144', 'd']),
        (['017', '[SHIFT IN]', '072', ':', '145', 'e']),
        (['020', '[DATA LINK ESCAPE]', '073', ';', '146', 'f']),
        (['021', '[DEVICE CONTROL 1]', '074', '<', '147', 'g']),
        (['022', '[DEVICE CONTROL 2]', '075', '=', '150', 'h']),
        (['023', '[DEVICE CONTROL 3]', '076', '>', '151', 'i']),
        (['024', '[DEVICE CONTROL 4]', '077', '?', '152', 'j']),
        (['025', '[NEGATIVE ACKNOWLEDGE]', '100', '@', '153', 'k']),
        (['026', '[SYNCHRONOUS IDLE]', '101', 'A', '154', 'l']),
        (['027', '[END OF TRANS. BLOCK]', '102', 'B', '155', 'm']),
        (['030', '[CANCEL]', '103', 'C', '156', 'n']),
        (['031', '[END OF MEDIUM]', '104', 'D', '157', 'o']),
        (['032', '[SUBSTITUTE]', '105', 'E', '160', 'p']),
        (['033', '[ESCAPE]', '106', 'F', '161', 'q']),
        (['034', '[FILE SEPARATOR]', '107', 'G', '162', 'r']),
        (['035', '[GROUP SEPARATOR]', '110', 'H', '163', 's']),
        (['036', '[RECORD SEPARATOR]', '111', 'I', '164', 't']),
        (['037', '[UNIT SEPARATION]', '112', 'J', '165', 'u']),
        (['040', '[SPACE]', '113', 'K', '166', 'v']),
        (['041', '!', '114', 'L', '167', 'w']),
        (['042', '\"', '115', 'M', '170', 'x']),
        (['043', '#', '116', 'N', '171', 'y']),
        (['044', '$', '117', 'O', '172', 'z']),
        (['045', '%', '120', 'P', '173', '{']),
        (['046', '&', '121', 'Q', '174', '|']),
        (['047', '\'', '122', 'R', '175', '}']),
        (['050', '(', '123', 'S', '176', '~']),
        (['051', ')', '124', 'T', '177', '[DEL]']),
        (['052', '*', '125', 'U', ]),
    )

    code_instance = SingleTable(oct_data)  # Generates the table
    # code_instance.title = 'ASCII Table' -- Gives the table a title

    code_instance.inner_column_border = True  # When set to True, there are dividing lines for every column.
    # When set to False, there are no dividing lines.

    code_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center', 4: 'center', 5: 'center'}
    # This centers the text in the columns
    # Column Key:
    # 0: Octal
    # 1: Characters

    code_instance.padding_left = 1  # Number of spaces to pad on the right side of every cell. Padding adds spacing
    # between the cell text and the column border.
    print(code_instance.table)


def morse_table():
    print('''
  __  __                            _____       _      _        
 |  \/  |  ___   _ __  ___   ___   |_   _|__ _ | |__  | |  ___ 
 | |\/| | / _ \ | '__|/ __| / _ \    | | / _` || '_ \ | | / _ \ 
 | |  | || (_) || |   \__ \|  __/    | || (_| || |_) || ||  __/
 |_|  |_| \___/ |_|   |___/ \___|    |_| \__,_||_.__/ |_| \___|''')
    morse_data = (
        (['Morse Code', 'Character', 'Morse Code', 'Character']),
        (['-.-.--', '!', '-...', 'B/b']),
        (['.-..-.', '\"', '-.-.', 'C/c']),
        (['...-..-', '$', '-..', 'D/d']),
        (['.-...', '&', '.', 'E/e']),
        (['.----.', '\'', '..-.', 'F/f']),
        (['-.--.', '(', '--.', 'G/g']),
        (['-.--.-', ')', '....', 'H/h']),
        (['.-.-.', '+', '..', 'I/i']),
        (['--..--', ',', '.---', 'J/j']),
        (['-....-', '-', '-.-', 'K/k']),
        (['.-.-.-', '.', '.-..', 'L/l']),
        (['-..-.', '/', '--', 'M/m']),
        (['-----', 0, '-.', 'N/n']),
        (['.----', 1, '---', 'O/o']),
        (['..---', 2, '.--.', 'P/p']),
        (['...--', 3, '--.-', 'Q/q']),
        (['....-', 4, '.-.', 'R/r']),
        (['.....', 5, '...', 'S/s']),
        (['-....', 6, '-', 'T/t']),
        (['--...', 7, '..-', 'U/u']),
        (['---..', 8, '...-', 'V/v']),
        (['----.', 9, '.--', 'W/w']),
        (['---...', ':', '-..-', 'X/x']),
        (['-.-.-.', ';', '-.--', 'Y/y']),
        (['-...-', '=', '--..', 'Z/z']),
        (['..--..', '?', '-.--.', '[']),
        (['.--.-.', '@', '-.--.-', ']']),
        (['.-', 'A/a', '..--.-', '_']),
    )

    code_instance = SingleTable(morse_data)  # Generates the table
    # code_instance.title = 'ASCII Table' -- Gives the table a title

    code_instance.inner_column_border = True  # When set to True, there are dividing lines for every column.
    # When set to False, there are no dividing lines.

    code_instance.justify_columns = {0: 'center', 1: 'center', 2: 'center', 3: 'center'}
    # This centers the text in the columns
    # Column Key:
    # 0: Morse Code
    # 1: Characters
    # 2: Morse Code
    # 3: Characters

    code_instance.padding_left = 1  # Number of spaces to pad on the right side of every cell. Padding adds spacing
    # between the cell text and the column border.
    print(code_instance.table)
    print('''Note: In Morse Code, ( = [ and ) = ]. This means there is only one parenthetical set used in Morse 
code. When the a message is encoded into Morse Code using this program, () are used ONLY. ''')


def ord2bin():
    print("This will convert ordinal to binary and vice versa.")


def ord2hex():
    print("This will convert ordinal to hexadecimal and vice versa.")


def ord2oct():
    print("This will convert ordinal to octal and vice versa.")


def ord2morse():
    print("This will convert ordinal to morse code and vice versa.")


def bin2hex():
    print("This will convert binary to hexadecimal and vice versa.")


def bin2oct():
    print("This will convert binary to octal and vice versa.")


def bin2morse():
    print("This will convert binary to hexadecimal and vice versa.")


# ascii_table()
