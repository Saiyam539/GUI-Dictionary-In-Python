from tkinter import *
import PyDictionary

window = Tk()
window.geometry('750x600')
window.title("Any Word Dictionary")
window.minsize(750,600)
window.maxsize(750,600)

bg = PhotoImage(file='image.png')
background = Label(window, image = bg)
background.place(x = 0, y =0)

try:
    def Dictionary():   
        from PyDictionary import PyDictionary
        Dictionary = PyDictionary()

        INPUT = user_input.get("1.0","end-1c")
        print(INPUT)
        meaning_of_word = Dictionary.meaning(INPUT)
        output.insert(END,f'The meaning of "{INPUT}" is- {meaning_of_word}')
except Exception as e:
    output.insert(END,'The meaning of {INPUT} is not found.')


Heading = Label(text="WELCOME TO ANY WORD DICTIONARY",bg='RED',fg='BLACK',width=600,
font =("Courier", 40),pady=10)
Heading.pack()

Label_1 = Label(text='Enter the word below.',font=("Courier", 35))
Label_1.pack()

user_input = Text(window,bg='LIGHT CYAN',width=600,height=3,font=("Courier", 25))
user_input.pack()

button =Button(window, text='Enter', font=("Courier", 30),padx=10,pady=1,
bg='BLUE',fg='BLACK',command=lambda:Dictionary())
button.pack()

output = Text(window,bg='LIGHT CYAN',width=600,height=3,font=("Courier", 20))
output.pack()


window.mainloop()
