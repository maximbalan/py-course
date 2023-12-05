from icecream import ic

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def decode_morse(morse_code):
    morse_code += ' '
    morse_letter_list = []
    morse_letter_list = morse_code.split(' ') 
    
    message = []

    ic(morse_letter_list)
    word = ''
    
    for morse_letter in morse_letter_list:
        if morse_letter != '':
            i = 0
            ic(morse_letter)
            for key, val in MORSE_CODE_DICT.items():
                if val == morse_letter:
                    word += key
        else:            
            i += 1
            if i == 2:
                message.append(" ")
            else:
                message.append(word)
                word = ''
    ic("".join(message))
    


decode_morse('.... . -.--   .--- ..- -.. .')