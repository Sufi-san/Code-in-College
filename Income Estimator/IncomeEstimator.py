from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter.font as tkfont
from PIL import ImageTk, Image
import webbrowser


def open_chatbot():
    webbrowser.open_new_tab("Chatbot.html")


def browse_folder():
    filedialog.askopenfilename(initialdir="Records", title="Select a Record", filetypes=(("Text files", "*.txt*"),
                                                                                         ("all files", "*.*")))


def open_create():
    def estimate_inc():
        pass

    def save_rec():
        pass

    def close_action():
        global window_counter1
        window_counter1 -= 1
        child.destroy()

    def when_focused1(event):
        check = entry_4.get()
        if check == placeholder_ent4:
            event.widget.delete(0, END)
            entry_4.configure(fg="black")

    def when_unfocused1(event):
        check = entry_4.get()
        if check == "":
            entry_4.configure(fg="#b4b4b4")
            entry_4.insert(0, placeholder_ent4)

    def when_focused2(event):
        check = entry_5.get()
        if check == placeholder_ent5:
            event.widget.delete(0, END)
            entry_5.configure(fg="black")

    def when_unfocused2(event):
        check = entry_5.get()
        if check == "":
            entry_5.configure(fg="#b4b4b4")
            entry_5.insert(0, placeholder_ent5)

    def on_combo_configure(event):
        global products
        font = tkfont.nametofont(str(event.widget.cget('font')))
        max_num = 0
        for product in products:
            if len(product) > max_num:
                max_num = products.index(product)
        width = font.measure(products[max_num] + "0") - event.width
        if width > cmb_box.winfo_width():
            style = ttk.Style()
            style.configure('TCombobox', postoffset=(0, 0, width, 0))

    global window_counter1
    if window_counter1 < 1:
        window_counter1 += 1
        child = Toplevel()
        child.title("Create A Record")
        child.resizable(False, False)
        child.geometry(f"{child.winfo_screenwidth()}x{child.winfo_screenheight()}+-7+0")
        child.protocol("WM_DELETE_WINDOW", close_action)
        child.iconbitmap("app_icon.ico")

        frame1 = LabelFrame(child, bg="#b4b4b4", text="Employee Details")
        frame1.place(x=40, y=110, width=653, height=280)
        frame2 = LabelFrame(child, bg="#b4b4b4", text="Product Details")
        frame2.place(x=740, y=40, width=606, height=320)
        tree_frame1 = Frame(child, bg="#b4b4b4")
        tree_frame1.place(x=40, y=388, width=927, height=345)
        tree_frame2 = Frame(child)
        tree_frame2.place(x=340, y=120, width=180, height=209)
        tree_frame3 = Frame(child)
        tree_frame3.place(x=1000, y=50, width=330, height=298)

        btn_1 = Button(child, text="Save Record", font=("Calibre", 15, "bold"))
        btn_1.place(x=1170, y=670, width=126, height=65)
        btn_2 = Button(child, text="Estimate Incomes", font=("Times New Roman", 22, "bold"))
        btn_2.place(x=990, y=390, width=234, height=52)
        btn_3 = Button(child, text="Add to Record")
        btn_3.place(x=50, y=350, width=129, height=30)
        btn_4 = Button(child, text="Update Selected")
        btn_4.place(x=190, y=350, width=129, height=30)
        btn_5 = Button(child, text="Remove Selected")
        btn_5.place(x=330, y=350, width=129, height=30)
        btn_6 = Button(child, text="Remove All")
        btn_6.place(x=470, y=350, width=129, height=30)
        btn_7 = Button(child, text="Add")
        btn_7.place(x=540, y=220, width=120, height=20)
        btn_8 = Button(child, text="Update Selected")
        btn_8.place(x=540, y=250, width=120, height=20)
        btn_9 = Button(child, text="Remove Selected")
        btn_9.place(x=540, y=280, width=120, height=20)
        btn_10 = Button(child, text="Remove All")
        btn_10.place(x=540, y=310, width=120, height=20)
        btn_11 = Button(child, text="Add Product")
        btn_11.place(x=760, y=200, width=211, height=30)
        btn_12 = Button(child, text="Update Selected Products")
        btn_12.place(x=760, y=240, width=211, height=30)
        btn_13 = Button(child, text="Remove Selected Products")
        btn_13.place(x=760, y=280, width=211, height=30)
        btn_14 = Button(child, text="Remove All")
        btn_14.place(x=760, y=320, width=211, height=30)

        chk_btn1 = Checkbutton(child, text="Include Products")
        chk_btn1.place(x=420, y=0, width=208, height=38)

        rad_btn1 = Radiobutton(child, text="Fixed Amount:", bg="#b4b4b4")
        rad_btn1.place(x=50, y=240, width=119, height=30)
        rad_btn2 = Radiobutton(child, text="Percentage Based:", bg="#b4b4b4")
        rad_btn2.place(x=55, y=270, width=124, height=37)

        lbl_1 = Label(child, text="Enter total collection:", font=f)
        lbl_1.place(x=30, y=0, width=146, height=30)
        lbl_2 = Label(child, text="Total Profit from Product Sale:", font=f)
        lbl_2.place(x=20, y=40, width=214, height=30)
        lbl_3 = Label(child, text="-", font=f)
        lbl_3.place(x=210, y=40, width=102, height=30)
        lbl_4 = Label(child, text="Collection excluding Product Sale:", font=f)
        lbl_4.place(x=30, y=70, width=216, height=30)
        lbl_5 = Label(child, text="-", font=f)
        lbl_5.place(x=240, y=70, width=111, height=31)
        lbl_6 = Label(child, text="ID:", font=f, bg="#b4b4b4")
        lbl_6.place(x=41, y=130, width=61, height=37)
        lbl_7 = Label(child, text="Name:", font=f, bg="#b4b4b4")
        lbl_7.place(x=41, y=170, width=82, height=32)
        lbl_8 = Label(child, text="Salary:", font=f, bg="#b4b4b4")
        lbl_8.place(x=42, y=210, width=82, height=39)
        lbl_9 = Label(child, text="Product:", font=f, bg="#b4b4b4")
        lbl_9.place(x=520, y=130, width=70, height=25)
        lbl_10 = Label(child, text="Quantity:", font=f, bg="#b4b4b4")
        lbl_10.place(x=520, y=170, width=70, height=25)
        lbl_11 = Label(child, text="Product Name:", font=f, bg="#b4b4b4")
        lbl_11.place(x=740, y=60, width=108, height=37)
        lbl_12 = Label(child, text="Employee Margin:", font=f, bg="#b4b4b4")
        lbl_12.place(x=740, y=90, width=126, height=38)
        lbl_13 = Label(child, text="Cost Price:", font=f, bg="#b4b4b4")
        lbl_13.place(x=740, y=120, width=83, height=36)
        lbl_14 = Label(child, text="Selling Price:", font=f, bg="#b4b4b4")
        lbl_14.place(x=740, y=150, width=96, height=39)
        lbl_15 = Label(child, text="Amount left after Distribution:", font=("Roboto", 13, "bold"))
        lbl_15.place(x=990, y=480, width=262, height=30)
        lbl_16 = Label(child, text="-", font=("Times New Roman", 12, "bold"))
        lbl_16.place(x=990, y=510, width=239, height=38)
        lbl_17 = Label(child, bg="black")
        lbl_17.place(x=40, y=340, width=652, height=1)
        lbl_17 = Label(child, bg="white")
        lbl_17.place(x=40, y=341, width=652, height=1)

        entry_1 = Entry(child, justify=CENTER)
        entry_1.place(x=170, y=1, width=155, height=30)
        entry_2 = Entry(child, justify=CENTER)
        entry_2.place(x=120, y=140, width=70, height=20)
        entry_3 = Entry(child, justify=CENTER)
        entry_3.place(x=120, y=180, width=70, height=20)
        entry_4 = Entry(child, fg="#b4b4b4", justify=CENTER)
        placeholder_ent4 = "Enter Amount"
        entry_4.insert(0, placeholder_ent4)
        entry_4.bind("<FocusIn>", when_focused1)
        entry_4.bind("<FocusOut>", when_unfocused1)
        entry_4.place(x=190, y=240, width=130, height=30)
        entry_5 = Entry(child, fg="#b4b4b4", justify=CENTER)
        placeholder_ent5 = "Enter % Collection"
        entry_5.insert(0, placeholder_ent5)
        entry_5.bind("<FocusIn>", when_focused2)
        entry_5.bind("<FocusOut>", when_unfocused2)
        entry_5.place(x=190, y=280, width=130, height=30)
        entry_6 = Entry(child, justify=CENTER)
        entry_6.place(x=590, y=170, width=79, height=30)
        entry_7 = Entry(child, justify=CENTER)
        entry_7.place(x=860, y=67, width=125, height=20)
        entry_8 = Entry(child, justify=CENTER)
        entry_8.place(x=860, y=100, width=125, height=20)
        entry_9 = Entry(child, justify=CENTER)
        entry_9.place(x=860, y=130, width=125, height=20)
        entry_10 = Entry(child, justify=CENTER)
        entry_10.place(x=860, y=160, width=125, height=20)

        global products
        products = ["Product1", "Product2", "Product3"]
        cmb_box = ttk.Combobox(child, values=products, state="readonly")
        cmb_box.place(x=590, y=130, width=80, height=25)
        cmb_box.bind("<Configure>", on_combo_configure)
    else:
        messagebox.showinfo("Limit reached!", "Can Open Only One Window")


f1 = ("Times New Roman", 20, "bold")
f = ("Calibre", 10)
global window_counter1
window_counter1 = 0
root = Tk()
root.title("Income Estimator")
root.geometry("540x440+0+0")
root.resizable(False, False)
root.iconbitmap("app_icon.ico")
img = ImageTk.PhotoImage(Image.open("MainWindowImage.jpg"))
chat_img = ImageTk.PhotoImage(Image.open("chat_image.png"))
img_lbl = Label(image=img)
img_lbl.pack()
title_lbl = Label(root, text="Income Estimator", bg="tomato", font=f1, justify="center")
title_lbl.place(x=36, y=20, width=465, height=85)
crt_new = Button(root, text="Create New Record", font=f1, justify="center", command=open_create)
crt_new.place(x=116, y=230, width=305, height=30)
src_old = Button(root, text="View Existing Record", font=f1, justify="center", command=browse_folder)
src_old.place(x=116, y=280, width=306, height=30)
chat_bot = Button(root, image=chat_img, font=f, command=open_chatbot)
chat_bot.place(x=460, y=380, width=69, height=51)
global products


root.mainloop()
