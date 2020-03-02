from tkinter import *
import parser
import math

root = Tk()
root.title('Calculator')

# putting the data in textfield
i = 0


def get_value(num):
    global i
    display.insert(i, num)
    i += 1


def getOperator(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def calculate():
    entireString = display.get()
    try:
        a = parser.expr(entireString).compile()
        result = eval(a)
        clearAll()
        display.insert(0, result)
    except:
        clearAll()
        display.insert(0, "Error")


def clearAll():
    display.delete(0, END)


def undo():
    entireString = display.get()
    if len(entireString) > 0:
        newString = entireString[:-1]
        clearAll()
        display.insert(0, newString)
    else:
        clearAll()
        display.insert(0, "Error")


display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

# Adding buttons

Button(root, text="1", command=lambda: get_value(1)).grid(row=2, column=0)
Button(root, text="2", command=lambda: get_value(2)).grid(row=2, column=1)
Button(root, text="3", command=lambda: get_value(3)).grid(row=2, column=2)

Button(root, text="4", command=lambda: get_value(4)).grid(row=3, column=0)
Button(root, text="5", command=lambda: get_value(5)).grid(row=3, column=1)
Button(root, text="6", command=lambda: get_value(6)).grid(row=3, column=2)

Button(root, text="7", command=lambda: get_value(7)).grid(row=4, column=0)
Button(root, text="8", command=lambda: get_value(8)).grid(row=4, column=1)
Button(root, text="9", command=lambda: get_value(9)).grid(row=4, column=2)

# Adding other buttons
Button(root, text="AC", command=lambda: clearAll()).grid(row=5, column=0)
Button(root, text="0", command=lambda: get_value(0)).grid(row=5, column=1)
Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

# Adding buttons to opperations
Button(root, text="+", command=lambda: getOperator("+")).grid(row=2, column=3)
Button(root, text="-", command=lambda: getOperator("-")).grid(row=3, column=3)
Button(root, text="*", command=lambda: getOperator("*")).grid(row=4, column=3)
Button(root, text="/", command=lambda: getOperator("/")).grid(row=5, column=3)

# Adding special operations
Button(root, text="PI", command=lambda: getOperator("*3.14")).grid(row=2, column=4)
Button(root, text="%", command=lambda: getOperator("%")).grid(row=3, column=4)
Button(root, text="(", command=lambda: getOperator("(")).grid(row=4, column=4)
Button(root, text="exp", command=lambda: getOperator("**")).grid(row=5, column=4)

Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
Button(root, text="x!", command=lambda: [getOperator("!"), math.factorial()]).grid(row=4, column=5)
Button(root, text=")", command=lambda: getOperator(")")).grid(row=3, column=5)
Button(root, text="^2", command=lambda: getOperator("**2")).grid(row=5, column=5)


root.mainloop()
