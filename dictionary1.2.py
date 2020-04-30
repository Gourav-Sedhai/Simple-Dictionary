from tkinter import *
import json
from difflib import get_close_matches
import tkinter.messagebox
import wikipedia

data = json.load(open("data.json"))

word = None

def dictionary():
    global word
    word = e1.get()
    word = word.lower()
    if len(e1.get()) == 0:
        tkinter.messagebox.showinfo("Empty", "Enter word to search!")
    elif e1.get() == 'Enter word to search':
        tkinter.messagebox.showinfo("Empty", "Enter word to search!")
    else:
        if word in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word])
        elif word.title() in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word.title()])  
        elif word.upper() in data:
            txt.delete("1.0", END)
            txt.insert(END, data[word.upper()])   
        elif len(get_close_matches(word, data.keys())) > 0:
            getWord = get_close_matches(word, data.keys())[0]
            ask = tkinter.messagebox.askquestion("Word not found", "Trying to search %s? " % getWord)
            if ask == 'yes':
                txt.delete("1.0", END)
                txt.insert(END, data[getWord])
            else:
                tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
        else:
            tkinter.messagebox.showerror("No such word", "There is no such word as %s " % word)
            
def noClick(event):
    if e1.get() == "Enter word to search":
       e1.delete(0, "end")
       e1.insert(0, "")
       e1.config(fg="#000000")

def onClick(event):
    if e1.get() == "":
        e1.insert(0, "Enter word to search")
        e1.config(fg = "grey")

def clear():
    e1.delete("0", END)
    txt.delete("1.0", END)

def close():
    get = tkinter.messagebox.askquestion("Exit", "Do you want to exit?")
    if get == 'yes':
        window.destroy()
    
def askWiki():
    word = e1.get()
    if len(e1.get()) == 0:
        tkinter.messagebox.showinfo("Empty", "Enter word to search!")
    elif e1.get() == 'Enter word to search':
        tkinter.messagebox.showinfo("Empty", "Enter word to search!")
    else:
        try:
            txt.delete("1.0", END)
            txt.insert(END, wikipedia.summary(word))
        except:
            tkinter.messagebox.showerror("Error", "Please check word or internet connection!")

window = Tk()

window.configure(bg='#81de90')

window.title("Dictionary")

text=StringVar()
e1 = Entry(window, bd=3, textvariable=text, width=38, fg="#000000", bg='#81de90')
e1.insert(0, "Enter word to search")
e1.bind("<FocusIn>", noClick)
e1.bind("<FocusOut>", onClick)
e1.config(fg = "grey")
e1.grid(row=0, column=0, columnspan=2)

b1 = Button(window, bd=4,  font="Times 10", text="Search", width=16, fg="#000000", command=dictionary)
b1.grid(row=0, column=2)

b2 = Button(window, bd=4, font="Times 10", text="Clear", width=15, fg="#000000", command=clear)
b2.grid(row=1, column=1)

b3 = Button(window, bd=4, font="Times 10", text="Close", width=15, fg="#000000", command=close)
b3.grid(row=1, column=0)

b4 = Button(window, bd=4, font="Times 10", text="Wikipedia", width=16, fg="#000000", command=askWiki)
b4.grid(row=1, column=2)

txt=Text(window, height=11, width=45, wrap=WORD, fg="#000000", bg='#81de90')
txt.grid(row=2, column=0, rowspan=6, columnspan=3)

sb1=Scrollbar(window)
sb1.grid(row=2, column=3, rowspan=6)

txt.configure(yscrollcommand=sb1.set)
sb1.configure(command=txt.yview)

txt.bind('<<TextSelect>>')

window.mainloop()