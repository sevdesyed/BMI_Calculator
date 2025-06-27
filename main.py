from importlib.metadata import entry_points
from tkinter import *

from unicodedata import category

window = Tk()
window.title("BMI Calculator")
window. minsize(width=200, height=250)

#kg label
label_kg = Label(window, text="Enter Your Weight (kg)")
label_kg.place(x=35, y=50)

#kg entry
entry_kg = int
entry_kg = Entry(width=15)
entry_kg.place(x=50, y=75)

#cm label
label_cm = Label(window, text="Enter Your Height (cm)")
label_cm.place(x=35, y=100)

#cm entry
entry_cm = int
entry_cm = Entry(width=15)
entry_cm.place(x=50, y=125)

#result label
label_result = Label(window, text="")
label_result.place(x=45, y=185)


#calculate button
def calculate():
    try:
        weight = float(entry_kg.get())
        height = float(entry_cm.get())
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal"
        elif 25 <= bmi < 30:
            category = "Overweight"
        elif 30 <= bmi < 40:
            category = "Obesity"
        else:
            category = "Extreme Obesity"

        label_result.config(text=f"Your BMI is: {bmi:.2f}.\n You are {category}")
    except ValueError:
        label_result.config(text="Invalid Entry")


button = Button(window, text="Calculate", command=calculate)
button.place(x=65, y=150)



window.mainloop()
