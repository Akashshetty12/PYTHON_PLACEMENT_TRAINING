# file = open("1.txt", "r")
# data = file.readlines()
# for i in data:
#     print(i.split())


# TKINTER
import tkinter
from tkinter import messagebox
def calculate():
    weight = float(wt_val.get())
    height = float(ht_val.get())
    height = height/100
    bmi = round(weight/(height**2),2)
    if bmi < 18.5:
        status = "Under weight"
    elif bmi >= 18.5 and bmi < 24.9:
        status = "Normal"
    elif bmi >= 24.9 and bmi < 30:
        status = "Overweight"
    else:
        status = "Obesity"
    res.config(text=f"BMI: {bmi} ({status})")
#     blink_text()
#
# def blink_text():
#     current_color = res.cget("foreground")
#     # Toggle between visible and invisible text color
#     next_color = "#f9f9f9" if current_color == "black" else "black"
#     res.config(foreground=next_color)
#     root.after(500, blink_text)

root = tkinter.Tk()
root.geometry("500x500")
root.title("Calculator")
root.configure(background='#f9f9f9')

head = tkinter.Label(root, text = "CALCULATOR", font = ("Arial",20, "bold"))
head.pack(pady = 30)

fr = tkinter.Frame(root, bg = "#f0f0f0")
fr.pack(pady = 5)

ht = tkinter.Label(fr, text = "Height (in cm)" , font = ("Arial", 15))
ht.grid(row = 0, column = 0, pady = 5 , padx = 5)

ht_val = tkinter.Entry(fr, bg = "#ffffff")
ht_val.grid(row = 0, column = 1, pady = 5 , padx = 5)

wt = tkinter.Label(fr, text = "Weight (in kg)" , font = ("Arial", 15))
wt.grid(row = 1, column = 0, pady = 5 , padx = 5)

wt_val = tkinter.Entry(fr, bg = "#f0f0f0")
wt_val.grid(row = 1, column = 1, pady = 5 , padx = 5)

button = tkinter.Button(fr, bg = "#ffffff", text = "submit" ,command = calculate, font = ("Arial", 15))
button.grid(row = 2, column = 1, pady = 10 , padx = 10)
# res = tkinter.Label(text = "", font = ("Arial", 15))
# res.pack()

res = tkinter.Label(root, text="", font=("Arial", 15), fg="black")
res.pack(pady=10)


root.mainloop()