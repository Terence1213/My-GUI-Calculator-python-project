from tkinter import *
#ALLOW THE USER TO ENTER VALUES FROM THE KEYBOARD

window = Tk()
photo = PhotoImage(file="img.png")
window.geometry("364x455")
window.title("Calculator")
window.iconphoto(True, photo)
equation_text = ""
def buttonPress(button):
    global equation_text
    entry.insert(len(entry.get()), str(button))
    entry.update()

def equals():
    global equation_text
    equation_text = entry.get()
    try:
        equation_text = str(eval(equation_text))
        entry.delete(0, END)
        entry.insert(0, equation_text)
    except ZeroDivisionError:
        entry.delete(0, END)
        entry.insert(0, "You cannot divide by zero!")
    except SyntaxError:
        entry.delete(0, END)
        entry.insert(0, "Invalid syntax!")

def clear():
    global equation_text
    equation_text=""
    entry.delete(0, END)


one_button = Button(window, text="1", font=35, height=4, width=9, command=lambda: buttonPress(1))
two_button = Button(window, text="2", font=35, height=4, width=9, command=lambda: buttonPress(2))
three_button = Button(window, text="3", font=35, height=4, width=9, command=lambda: buttonPress(3))
four_button = Button(window, text="4", font=35, height=4, width=9, command=lambda: buttonPress(4))
five_button = Button(window, text="5", font=35, height=4, width=9, command=lambda: buttonPress(5))
six_button = Button(window, text="6", font=35, height=4, width=9, command=lambda: buttonPress(6))
seven_button = Button(window, text="7", font=35, height=4, width=9, command=lambda: buttonPress(7))
eight_button = Button(window, text="8", font=35, height=4, width=9, command=lambda: buttonPress(8))
nine_button = Button(window, text="9", font=35, height=4, width=9, command=lambda: buttonPress(9))
zero_button = Button(window, text="0", font=35, height=4, width=9, command=lambda: buttonPress(0))
plus_button = Button(window, text="+", font=35, height=4, width=9, command=lambda: buttonPress("+"))
mult_button = Button(window, text="*", font=35, height=4, width=9, command=lambda: buttonPress("*"))
div_button = Button(window, text="/", font=35, height=4, width=9, command=lambda: buttonPress("/"))
sub_button = Button(window, text="-", font=35, height=4, width=9, command=lambda: buttonPress("-"))
decimal_button = Button(window, text=".", font=35, height=4, width=9, command=lambda: buttonPress("."))
#HALLO
clear_button = Button(window, text="Clear", font=35, height=3, width=9, command=clear)
entry = Entry(window, fg="lime", bg="black", font=("Arial", 25), width=20, justify=CENTER, )
equal_button = Button(window, text="=", font=35, height=4, width=9, command=equals)
entry.grid(row=0, columnspan=5)
one_button.grid(row=1, column=0)
two_button.grid(row=1, column=1)
three_button.grid(row=1, column=2)
four_button.grid(row=2, column=0)
five_button.grid(row=2, column=1)
six_button.grid(row=2, column=2)
seven_button.grid(row=3, column=0)
eight_button.grid(row=3, column=1)
nine_button.grid(row=3, column=2)
zero_button.grid(row=4, column=0)
plus_button.grid(row=1, column=4)
sub_button.grid(row=2, column=4)
mult_button.grid(row=3, column=4)
div_button.grid(row=4, column=4)
equal_button.grid(row=4, column=2)
clear_button.grid(row=5, columnspan=5)
decimal_button.grid(row=4, column=1)


window.mainloop()
