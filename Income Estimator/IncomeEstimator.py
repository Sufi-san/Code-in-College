from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image

f1 = ("Times New Roman", 20, "bold")
f = ("Calibre", 10)
global second_window_counter
second_window_counter = 0


def open_chatbot():
    with open("Chatbot.py") as cb:
        exec(cb.read())


def open_create():
    global second_window_counter

    def close_action():
        global second_window_counter
        second_window_counter -= 1
        cr_win.destroy()

    if second_window_counter < 1:
        second_window_counter += 1
        cr_win = Toplevel()
        cr_win.title("Create A Record.")
        cr_win.resizable(False, False)
        cr_win.geometry("600x500+700+100")
        cr_win.protocol("WM_DELETE_WINDOW", close_action)
        v1 = IntVar()

        class InsideFrames:

            def __init__(self, win_frame, new_height, sr_num):
                ins_frame = Frame(win_frame, bg="#b4b4b4")
                ins_frame.place(x=0, y=new_height, width=475, height=20)

                self.fr_lbl1 = Label(ins_frame, text=sr_num, font=f, justify="center")
                self.fr_lbl1.place(x=0, y=0, width=60, height=15)
                self.fr_lbl2 = Label(ins_frame, text=f"Employee ID: ", font=f, justify="center")
                self.fr_lbl2.place(x=63, y=0, width=150, height=15)
                self.fr_btn1 = Button(ins_frame, text="Details", font=f, justify="center")
                self.fr_btn1.place(x=218, y=0, width=60, height=15)
                self.fr_btn2 = Button(ins_frame, text="X", bg="red", fg="white", justify="center", command=ins_frame.destroy)
                self.fr_btn2.place(x=286, y=0, width=20, height=15)
                self.fr_lbl3 = Label(ins_frame, text="-", font=f, justify="center")
                self.fr_lbl3.place(x=316, y=0, width=160, height=15)

        def enable_prod():
            if v1.get() == 1:
                lbl_2.configure(state=NORMAL)
                entry_2.configure(state=NORMAL)
                btn_1.configure(state=NORMAL)
                btn_2.configure(state=NORMAL)
            elif v1.get() == 0:
                lbl_2.configure(state=DISABLED)
                entry_2.delete(0, END)
                entry_2.configure(state=DISABLED)
                btn_1.configure(state=DISABLED)
                btn_2.configure(state=DISABLED)

        def create_frames():
            ins_frame_height = 20
            num = int(entry_3.get())
            for i in range(0, num):
                ins_frame = InsideFrames(frame_1, ins_frame_height, i+1)
                ins_frame_height += 20

        frame_1 = Frame(cr_win,bg="#b4b4b4", padx=5, pady=5)
        frame_1.place(x=40, y=220, width=510, height=187)

        scrollbar_1 = Scrollbar(frame_1, orient=VERTICAL)
        scrollbar_1.pack(side="right", fill=Y)

        fr_lbl1 = Label(frame_1, text="Sr.No.", font=f, justify="center")
        fr_lbl1.place(x=0, y=0, width=60, height=15)
        fr_lbl2 = Label(frame_1, text="Employee Details", font=f, justify="center")
        fr_lbl2.place(x=63, y=0, width=250, height=15)
        fr_lbl3 = Label(frame_1, text="Income/Salary", font=f, justify="center")
        fr_lbl3.place(x=316, y=0, width=160, height=15)

        lbl_1 = Label(cr_win, text="Enter Total Collection:", font=f, justify="center", )
        lbl_1.place(x=30, y=20, width=146, height=30)
        lbl_2 = Label(cr_win, text="Enter Total Profit from Products:", font=f, justify="center", state=DISABLED)
        lbl_2.place(x=20, y=90, width=219, height=30)
        lbl_3 = Label(cr_win, text="Enter Number of Employees to Add/Remove:", font=f, justify="center")
        lbl_3.place(x=40, y=180, width=258, height=30)
        lbl_4 = Label(cr_win, text="Amount Left after Distribution:", font=f, justify="center")
        lbl_4.place(x=310, y=420, width=224, height=30)
        lbl_5 = Label(cr_win, text="-", font=f, justify="center")
        lbl_5.place(x=310, y=450, width=210, height=30)

        entry_1 = Entry(cr_win, font=f, justify="center")
        entry_1.place(x=180, y=20, width=155, height=30)
        entry_2 = Entry(cr_win, font=f, justify="center", state=DISABLED)
        entry_2.place(x=240, y=90, width=176, height=30)
        entry_3 = Entry(cr_win, font=f, justify="center")
        entry_3.place(x=300, y=180, width=52, height=30)

        chk_box1 = Checkbutton(cr_win, text="Include Products", font=f, variable=v1, command=enable_prod, onvalue=1,
                               offvalue=0)
        chk_box1.place(x=30, y=60, width=125, height=32)

        btn_1 = Button(cr_win, text="Add New Product", state=DISABLED)
        btn_1.place(x=40, y=140, width=238, height=30)
        btn_2 = Button(cr_win, text="View List of Products", state=DISABLED)
        btn_2.place(x=300, y=140, width=244, height=30)
        btn_3 = Button(cr_win, text="Add", command=create_frames)
        btn_3.place(x=360, y=180, width=76, height=30)
        btn_4 = Button(cr_win, text="Remove")
        btn_4.place(x=440, y=180, width=76, height=30)
        btn_5 = Button(cr_win, text="Estimate Incomes")
        btn_5.place(x=40, y=420, width=226, height=30)
        btn_6 = Button(cr_win, text="Save Record")
        btn_6.place(x=40, y=460, width=226, height=30)
    else:
        messagebox.showinfo("Limit reached!", "Can Open Only One Window")


def browse_folder():
    filedialog.askopenfilename(initialdir="Records", title="Select a Record", filetypes=(("Text files", "*.txt*"),
                                                                                         ("all files", "*.*")))


main_win = Tk()
main_win.title("Income Estimator")
main_win.geometry("600x500+100+100")
main_win.resizable(False, False)
img = ImageTk.PhotoImage(Image.open("MainWindowImage.jpg"))
chat_img = ImageTk.PhotoImage(Image.open("chat_image.png"))
img_lbl = Label(image=img)
img_lbl.pack()
title_lbl = Label(main_win, text="Income Estimator", bg="tomato", font=f1, justify="center")
title_lbl.place(x=50, y=20, width=495, height=105)
crt_new = Button(main_win, text="Create New Record", font=f1, justify="center", command=open_create)
crt_new.place(x=130, y=230, width=325, height=30)
src_old = Button(main_win, text="View Existing Record", font=f1, justify="center", command=browse_folder)
src_old.place(x=130, y=280, width=326, height=30)
chat_bot = Button(main_win, image=chat_img, font=f, command=open_chatbot)
chat_bot.place(x=490, y=410, width=79, height=61)


main_win.mainloop()
