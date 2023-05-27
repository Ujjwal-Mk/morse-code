import function as f
import tkinter as tk
from tkinter import ttk
import googletrans
from googletrans import Translator

# Global Objects
translator = Translator()
DEST = "en"

# below code is for GUI

def morse(morse):
    global DEST                           #function called when 'Morse → AlphaNumeric' button is pressed
    output_text.delete('1.0', tk.END)       #Clear output section
    alpha = f.morse_to_alphanumeric(morse)  #calling the conversion function
    alpha_text = translator.translate(text=alpha,dest=DEST).text
    # print(alpha_text)
    output_text.insert(1.0, alpha_text)          #Display the output


def alpha(alpha):                          #function called when 'AlphaNumeric → Morse' button is pressed
    output_text.delete('1.0', tk.END)       #Clear output section
    alpha_text = translator.translate(text=alpha,dest="en")# Translating the input to the preferred language 
    morse = f.alpha_to_morse((alpha_text.text).upper()) #calling the conversion function
    output_text.insert(1.0, morse)          #Display the output


def play(alpha):                            #function called when 'Play Morse' button is pressed
    output_text.delete('1.0', tk.END)       #Clear output section
    alpha_text = translator.translate(text=alpha,dest="en") # Translate the regional language to english for conversion
    morse = f.alpha_to_morse((alpha_text.text).upper()) #calling the conversion function
    output_text.insert(1.0, morse)          #Display the output
    f.morse_play(morse)                     #calling the morse play function


def speech_main(text):
    isAlpha = True
    for i in text:
        if i=='.' or i=='-':
            isAlpha = False
            break
    if isAlpha:
        alpha = translator.translate(text=text,dest="en").text
        f.speech(alpha)
    else:
        alpha = f.morse_to_alphanumeric(text)
        output_text.delete('1.0',tk.END)
        output_text.insert(1.0, alpha) 
        f.speech(alpha)

languages_dict = {"en":"English","bn": "Bengali", 
                  "gu":"Gujarati", "hi": "Hindi",
                  "kn": "Kannada", "ml": "Malayalam",
                  "mr": "Marathi", "pa": "Punjabi",
                  "ta": "Tamil",  "te": "Telugu",
                  "ur" :"Urdu"}


def UpdateDEST(event):
    global languages_dict
    global DEST
    DEST = [k for k,v in languages_dict.items() if clicked.get()==v][0]

#create the tkinter window
root = tk.Tk()
clicked = tk.StringVar()
clicked.set(list(languages_dict.values())[0])

#Creating GUI widgets
canvas = tk.Canvas(root, height=700, width=750)

head_label = tk.Label(canvas, text='Morse Code Converter', font=('Times New Roman', 30))

notice_frame = tk.Frame(canvas, height=200, width=550, bd=10, bg='#a0a0a0')

input_notice1 = tk.Label(notice_frame, text='The input is accepted in Morse or Alpha-Numeric.', bg='#a0a0a0',
                         font=('Times New Roman', 15))

input_notice2 = tk.Label(notice_frame,
                         text='If input is in morse then leave one space between each character and two space between each word.',
                         bg='#a0a0a0', font=('Times New Roman', 15))

input_label = tk.Label(canvas, text='Input: ', font=('Helvetica', 20))

input_entry = tk.Entry(canvas, font=('Helvetica', 13),width=55)

output_label = tk.Label(canvas, text='Output ↓', font=('Helvetica', 20))

output_text = tk.Text(canvas, height=5, width=55, borderwidth=1, font=('Helvetica', 15))

morse_alpha_button = tk.Button(canvas, text='Morse → AlphaNumeric', font=('Helvetica', 15),
                                command=lambda: morse(input_entry.get()))

alpha_morse_button = tk.Button(canvas, text='AlphaNumeric → Morse', font=('Helvetica', 15),
                               command=lambda: alpha(input_entry.get()))

play_button = tk.Button(canvas, text='Play\nMorse', font=('Helvetica', 15), height=3,
                        command=lambda: play(input_entry.get()))
speech_button = tk.Button(canvas, text='Play\nText', font=('Helvetica', 15), height=3,
                        command=lambda: speech_main(input_entry.get()))

notice_frame_1 = tk.Frame(canvas, height=80, width=245, bd=10, bg='#a0a0a0')

input_label_1 = tk.Label(canvas,text="Select Output Language for your Morse-Code:",font=('Helvetica',20))

input_notice3 = tk.Label(notice_frame_1,text="Select the language you want your morse code to be translated into:\n(English is set as default)",
                         bg='#a0a0a0',font=('Times New Roman',15))

dropDownBox = tk.OptionMenu(canvas,clicked, *list(languages_dict.values()),command=UpdateDEST)

#placing the GUI widgets
canvas.pack()
head_label.place(y=2, relx=0.35)
notice_frame.place(y=55, x=75)
input_notice1.pack()
input_notice2.pack()
input_label.place(y=150, x=25)
input_entry.place(y=150, x=95)
output_label.place(y=225, x=25)
output_text.place(y=265, x=25)
alpha_morse_button.place(y=520, x=75)
morse_alpha_button.place(y=565, x=75)
play_button.place(y=525, x=350)
speech_button.place(y=525, x=450)
input_label_1.place(y=380,x=15)
notice_frame_1.place(y=420,x=12)
input_notice3.pack()
dropDownBox.place(y=440, x=475)

root.mainloop()