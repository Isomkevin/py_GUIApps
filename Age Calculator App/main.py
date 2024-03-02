import datetime
import tkinter as tk
from PIL import Image, ImageTk

window=tk.Tk()
window.geometry("620x780")
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


def getinput():
    name = nameEntry.get()
    monkey = Person(name, 
                    datetime.date(int(yearEntry.get()), 
                                  int(monthEntry.get()),
                                  int(dateEntry())))
    textArea = tk.text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = f" Heyy {monkey}!!!, You are {monkey.age()} years old!!! "
    textArea.insert(tk.END, answer)

image = Image.open('AgeCalc_App.jpeg')
image.thumbnail((300,300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=1,row=0)


window.mainloop()