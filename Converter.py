# code = text.delete(1.0,END)
# Copyright:  @2018.

import math
import base64
import tkinter
from tkinter import *
from math import *
from base64 import *

# Text variables
function_one = "EURO - NOK"
function_two = "DOLLAR - NOK"
function_Three = "PEN- NOK"
function_four  = "PUND - NOK"

# Loop start
window = Tk()
window.title("Valuta Converter")

# Buttons key functions
def function_one():
	one = float(entry1_value.get())
	try:
		t1.delete(1.0,END)
		t1.insert(END,"{}\tNOK".format(one*9.56))
	except ValueError:
		return t1.insert(END, "Error, Failure")

def function_two():
	two = float(entry2_value.get())
	try:
		t2.delete(1.0,END)
		t2.insert(END,"{}\tNOK".format(two*8.25))
	except:
		return t2.insert(END, "Error, Failure")

def function_Three():
	three = float(entry3_value.get())
	try:
		t3.delete(1.0,END)
		t3.insert(END,"{}\tNOK".format(three*2.52))
	except:
		return t3.insert(END, "Error, Failure")

def function_four():
	four = float(entry4_value.get())
	try:
		t4.delete(1.0,END)
		t4.insert(END,"{}\tNOK".format(four*10.73))
	except:
		return t4.insert(END, "Error, Failure")
# Buttons
b1 = Button(window, text="EURO - NOK", 	command=function_one)
b2 = Button(window, text="DOLLAR - NOK",command=function_two)
b3 = Button(window, text="PEN - NOK", 	command=function_Three)
b4 = Button(window, text="PUND - NOK", 	command=function_four)

# Buttons Grids
b1.grid(row=0, column=0)
b2.grid(row=1, column=0)
b3.grid(row=2, column=0)
b4.grid(row=3, column=0)

#Entry Values
entry1_value = StringVar()
entry2_value = StringVar()
entry3_value = StringVar()
entry4_value = StringVar()

#Entry
entry1 = Entry(window, textvariable=entry1_value)
entry2 = Entry(window, textvariable=entry2_value)
entry3 = Entry(window, textvariable=entry3_value)
entry4 = Entry(window, textvariable=entry4_value)

#Entry Place
entry1.place(x=1.5, y=1.5, width=30)
entry2.place(x=1.5, y=1.5, width=30)
entry3.place(x=1.5, y=1.5, width=30)
entry4.place(x=1.5, y=1.5, width=30)

#Entry Grid
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)

#TEXT
t1 = Text(window, height=1, width=30)
t2 = Text(window, height=1, width=30)
t3 = Text(window, height=1, width=30)
t4 = Text(window, height=1, width=30)

#TEXT GRID
t1.grid(row=0, column=2)
t2.grid(row=1, column=2)
t3.grid(row=2, column=2)
t4.grid(row=3, column=2)

#End of loop
window.mainloop()
