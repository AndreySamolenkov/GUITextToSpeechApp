import os
from gtts import gTTS
import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.title("Text To Speech Converter")

def textToSpeech():
    text = entry.get()
    language = clicked.get()
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')

label = tk.Label(root, text="Enter your text:",font=('Helvetica', 11))
label.pack(pady=20)

entry = tk.Entry(root, width=50, font=('Helvetica', 11))
entry.pack(padx=10,ipadx=20, ipady=20)

options = [
    "en",
    "fr",
    "sp",
    "gr",
    "pt",
    "ru",
    "it"
]
clicked = tk.StringVar()
clicked.set("en")

drop = tk.OptionMenu(root, clicked, *options)
drop.pack(pady=10)

button = tk.Button(text='Convert to audio', command=textToSpeech, font=('Helvetica', 10))
button.pack(pady=5)

root.mainloop()
