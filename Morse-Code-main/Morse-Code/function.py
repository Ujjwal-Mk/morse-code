import simpleaudio as sa  # importing the audio playing library
from gtts import gTTS
import  os
# Dictionary of alphanumeric and their respective morse code
code = {'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----', ', ': '--..--', '.': '.-.-.-',
        '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-'}

# list of alphanumeric for check
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
              '9', ' ']


def morse_to_alphanumeric(message):
    # extra space added at the end to access the
    # last morse code
    # We have tweaked this to work for empty spaces at the end so that the last character is unaltered and translated properly
    message += ' '
    # Checking if the given message is in morse code:
    for i in message:
        if i != " " and i != "." and i != "-":
            return "Enter Valid Morse Code"
    # Two strings to decode the morse code to english
    decipher = '' # Final String output
    citext = ''  # Morse string for each letter
    for letter in message.upper():
        # Checks if the letter is a space or not: if it's not adds morse characters till a space
        if letter != ' ':

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of spaces
        else:
            # if i=1 a single character exists
            i += 1

            # if two empty spaces indicate a new word
            if i == 2:
                # adding space to separate the words
                decipher += ' '
            else:

                # accessing the keys using their values

                decipher += list(code.keys())[
                    list(code.values()).index(citext)]
                
                # Intializing the citext back to empty string for another iteration
                citext = ''
# returning the string:
    return decipher


def alpha_to_morse(message):
    # Checking if message's characters are alphabets
    for i in message:
        if i not in alpha_list:
            return "Enter Valid Text"
    # Initialzing an empty string to return morse code
    cipher = ''
    # Converting all the characters to capital letters, because morse code is not case-sensitive:
    message = message.upper()

    for letter in message:
        if letter != ' ':
            # Gets the value from the key obtained by the letter variable
            cipher += code[letter] + ' ' # Adds a space to signify the end of a character in morse.
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
            # In the case of a different word another additional space is added to the previous space of 
            # the last characters
    return cipher

def speech(text):
    language = "en"
    obj = gTTS(text=text, lang=language, slow=False)
    obj.save("speech.mp3")
    os.system("afplay speech.mp3")
    
# importing the sound files
dat_sound = sa.WaveObject.from_wave_file("dat.wav")
dit_sound = sa.WaveObject.from_wave_file("dit.wav")
space_sound = sa.WaveObject.from_wave_file("space.wav")


# play the sound respect to the morse
def morse_play(morse):
    for i in morse:
        if i == '-':
            dat_play = dat_sound.play()
            dat_play.wait_done()

        if i == '.':
            dit_play = dit_sound.play()
            dit_play.wait_done()

        if i == ' ':
            space_play = space_sound.play()
            space_play.wait_done()
