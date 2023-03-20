from tkinter import *

root = Tk()
root.title("Chatbot for Income Estimator")
root.geometry("400x300+100+100")
root.resizable(False, False)
f = ("Times New Roman", 20, "bold")

wlcm_lb = Label(root, text="Welcome to Chatbot!", font=f, bg="skyblue")
wlcm_lb.place(x=80, y=100)

root.mainloop()
