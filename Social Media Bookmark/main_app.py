import tkinter as tk
import webbrowser

linkedin_profile = "https://www.linkedin.com/in/kevin-isom-a58bb3201/"
facebook_profile = "https://www.facebook.com/profile.php?id=100015443014495"

def linkedin(event):
    webbrowser.open_new_tab(' put your linkedin profile link here ')

def facebook(event):
    webbrowser.open_new_tab(' put your facebook profile link here ')


window = tk.Tk()
window.title(" Social Media Bookmark App ")
window.geometry("300x200")

label1=tk.Label(text="My Social media", font=("Times new roman", 16))
label1.grid(column=0,row=0)

button1=tk.Button(window,text="Linkedin",bg="orange")
button1.grid(column=1,row=1)
button2=tk.Button(window,text="Facebook",bg="pink")
button2.grid(column=3,row=1)

button1.bind("<Button-1>",linkedin)
button2.bind("<Button-1>",facebook)

window.mainloop()