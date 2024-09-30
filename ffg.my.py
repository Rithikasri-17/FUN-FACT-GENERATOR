"""Fun Fact Generator"""

import json 
import requests
from tkinter import * 

window = Tk()
window.title("Fun Fact Generator")
window.geometry('800x80')

def get_fun_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    useless_facts = data['text']
    lbl.configure(text=useless_facts)

btn = Button(window, text='Click Me', command=get_fun_fact)
btn.pack()

lbl = Label(window, text='Click the button to get a random fact')
lbl.pack()

window.mainloop()
