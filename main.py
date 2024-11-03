from playsound import playsound
from time import sleep

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

password = input("Enter the password you want to convert into Morse Code\n")
Morse_Code_password = ""

for char in password:
    if(char.upper() in chars_in_Morse_Code):
        Morse_Code_password += chars_in_Morse_Code[char.upper()].strip()
    else:
        print(f"This letter {char} Cann't be converted to Morse Code.")

print(Morse_Code_password)

for char in Morse_Code_password:
    if(char == '.'):
        playsound("dot.wav")
    elif(char == '-'):
        playsound("dash.wav")
    elif(char == ' '):
        sleep(0.1)
    sleep(0.15)
