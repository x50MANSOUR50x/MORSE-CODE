from playsound import playsound
from time import sleep
import os

chars_in_Morse_Code = {
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. ',
    '0': '----- ',
    '!': '-.-.-- ',
    '"': '.-..-. ',
    '$': '...-..- ',
    '&': '.-... ',
    "'": '.----. ',
    '(': '-.--. ',
    ')': '-.--.- ',
    '+': '.-.-. ',
    ',': '--..-- ',
    '-': '-....- ',
    '.': '.-.-.- ',
    '/': '-..-. ',
    ':': '---... ',
    ';': '-.-.-. ',
    '=': '-...- ',
    '?': '..--.. ',
    '@': '.--.-. ',
    '_': '..--.- ',
}

os.system('cls')

print("Welcome to the MORSE CODE Text Converter Project!")
sleep(2)

program_on = True

while(program_on):
    os.system('cls')
    password = input("Enter the password you want to convert into Morse Code\n")
    Morse_Code_password = ""

    for char in password:
        if(char.upper() in chars_in_Morse_Code):
            Morse_Code_password += chars_in_Morse_Code[char.upper()].strip()
        else:
            Morse_Code_password += ' '

    print(Morse_Code_password)

    for char in Morse_Code_password:
        if(char == '.'):
            playsound("dot.wav")
        elif(char == '-'):
            playsound("dash.wav")
        elif(char == ' '):
            sleep(0.1)
        sleep(0.15)
    
    if(input("Would you like to add another password? (Enter \'y\' or \'n\') \n").lower() == 'n'):
        program_on = False

os.system('cls')

print("Thank you for using the MORSE CODE Text Converter!")
sleep(2)

os.system('cls')