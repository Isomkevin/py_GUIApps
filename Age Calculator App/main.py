import datetime
import tkinter as tk
from PIL import Image, ImageTk

window=tk.Tk()
window.geometry("350x400")
window.title(" Age Calculator App ")

name = tk.Label(text = "Name")
name.grid(column=0,row=1)
year = tk.Label(text = "Year")
year.grid(column=0,row=2)
year = tk.Label(text = "Month")
year.grid(column=0,row=3)
year = tk.Label(text = "Day")
year.grid(column=0,row=4)

nameEntry = tk.Entry()
nameEntry.grid(column=1,row=1)
yearEntry = tk.Entry()
yearEntry.grid(column=1,row=2)
monthEntry = tk.Entry()
monthEntry.grid(column=1,row=3)
dateEntry = tk.Entry()
dateEntry.grid(column=1,row=4)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
        
    def age(self):
        today = datetime.date.today()
        age = today.year-self.birthdate.year
        return age

def getInput():
    name: str = nameEntry.get()
    monkey = Person(name, 
                    datetime.date(int(yearEntry.get()), 
                                  int(monthEntry.get()),
                                  int(dateEntry.get())))
    textArea = tk.Text(master=window, height=10, width=30)
    textArea.grid(column=1, row=6)
    answer = f''' Heyy {monkey.name}!!!, 
    You are {monkey.age()} years old!!!''' 
    textArea.insert(tk.END, answer)

button = tk.Button(window, text="Calculate Age", 
                   command = getInput, bg="pink")
button.grid(column=1,row=5)


image_path = r"C:\Users\LENOVO\OneDrive\Desktop\EdoC_Files\GUIApps_py\Age Calculator App\AgeCalc_App.jpg"
image = Image.open(image_path)
image.thumbnail((300,300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1,row=0)


window.mainloop()