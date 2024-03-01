import tkinter as tk


def doorbell(event):
    print(" You clicked the Doorbell ! ")


window = tk.Tk()
window.title(" Pythonista Planet Desktop ")
window.geometry("600x400")

label_text = " Visit Pythonista Planet to improve your Python skills "
label1 = tk.Label(text = label_text)
label1.grid(column=0,row=0)

button_text = " some button text "
button1 = tk.Button(window, text = button_text)
button1.grid(column=1,row=1)
button1.bind("<Button-1>",doorbell)


window.mainloop()