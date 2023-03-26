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

    def save_file():
        pass

    def close_action():
        global window_counter1
        window_counter1 -= 1
        child.destroy()

    def when_focused1(event):
        check = entry_4.get()
        if check == placeholder_ent4a or check == placeholder_ent4b:
            event.widget.delete(0, END)
            entry_4.configure(fg="black")

    def enable_prod():
        if v1.get() == 1:
            entry_5.configure(state=NORMAL)
            btn_7.configure(state=NORMAL)
            btn_8.configure(state=NORMAL)
            btn_9.configure(state=NORMAL)
            btn_10.configure(state=NORMAL)
            cmb_box.configure(state="readonly")
            lbl_2.configure(state=NORMAL)
            lbl_3.configure(state=NORMAL)
            lbl_9.configure(state=NORMAL)
            lbl_10.configure(state=NORMAL)
        elif v1.get() == 0:
            entry_5.configure(state=DISABLED)
            btn_7.configure(state=DISABLED)
            btn_8.configure(state=DISABLED)
            btn_9.configure(state=DISABLED)
            btn_10.configure(state=DISABLED)
            cmb_box.configure(state=DISABLED)
            lbl_2.configure(state=DISABLED)
            lbl_3.configure(state=DISABLED)
            lbl_9.configure(state=DISABLED)
            lbl_10.configure(state=DISABLED)

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

    def choose():
        entry_3.focus_set()
        if v2.get() == 1:
            entry_4.delete(0, END)
            entry_4.configure(state=NORMAL)
            if entry_4.get() == "":
                entry_4.configure(fg="#b4b4b4")
                entry_4.insert(0, placeholder_ent4a)
        elif v2.get() == 2:
            entry_4.delete(0, END)
            entry_4.configure(state=NORMAL)
            if entry_4.get() == "":
                entry_4.configure(fg="#b4b4b4")
                entry_4.insert(0, placeholder_ent4b)

    def add_rec_tree1():
        global count_tree1
        global list_tree1
        for record in tree_view1.get_children():
            tree_view1.delete(record)
            count_tree1 -= 1
        if cmb_box.get() != "" and entry_5.get() != "":
            list_tree1.append((cmb_box.get(), int(entry_5.get()), "Empty"))
        for record in list_tree1:
            tree_view1.insert(parent="", index="end", iid=count_tree1, text="", values=record)
            count_tree1 += 1

    def upd_rec_tree1():
        global count_tree1
        global list_tree1
        records = tree_view1.selection()
        for record in records:
            instance = tuple(tree_view1.item(record)["values"])
            place_at = list_tree1.index(instance)
            list_tree1.remove(instance)
            if cmb_box.get() != "" and entry_5.get() != "":
                list_tree1.insert(place_at, (cmb_box.get(), int(entry_5.get()), "Empty"))
        for record in tree_view1.get_children():
            tree_view1.delete(record)
            count_tree1 -= 1
        for record in list_tree1:
            tree_view1.insert(parent="", index="end", iid=count_tree1, text="", values=record)
            count_tree1 += 1

    def rem_all_rec_tree1():
        global count_tree1
        global list_tree1
        list_tree1.clear()
        for record in tree_view1.get_children():
            tree_view1.delete(record)
            count_tree1 -= 1

    def rem_select_rec_tree1():
        global count_tree1
        global list_tree1
        records = tree_view1.selection()
        for record in records:
            instance = tuple(tree_view1.item(record)["values"])
            list_tree1.remove(instance)
        for record in tree_view1.get_children():
            tree_view1.delete(record)
            count_tree1 -= 1
        for record in list_tree1:
            tree_view1.insert(parent="", index="end", iid=count_tree1, text="", values=record)
            count_tree1 += 1

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
        tree_frame1 = Frame(child)
        tree_frame1.place(x=340, y=120, width=180, height=209)
        tree_frame2 = Frame(child)
        tree_frame2.place(x=1000, y=50, width=330, height=298)
        tree_frame3 = Frame(child, bg="#b4b4b4")
        tree_frame3.place(x=40, y=388, width=927, height=330)

        scr1a = Scrollbar(tree_frame1, width=15)
        scr1a.pack(side=RIGHT, fill=Y)
        scr1b = Scrollbar(tree_frame1, orient=HORIZONTAL, width=15)
        scr1b.pack(side=BOTTOM, fill=X)
        scr2a = Scrollbar(tree_frame2, width=15)
        scr2a.pack(side=RIGHT, fill=Y)
        scr2b = Scrollbar(tree_frame2, orient=HORIZONTAL, width=15)
        scr2b.pack(side=BOTTOM, fill=X)
        scr3a = Scrollbar(tree_frame3, width=15)
        scr3a.pack(side=RIGHT, fill=Y)

        tree_view1 = ttk.Treeview(tree_frame1, yscrollcommand=scr1a.set, xscrollcommand=scr1b.set)
        tree_view1["columns"] = ("Product", "Quantity", "Total Profit")
        tree_view1.column("#0", width=0, stretch=NO)
        tree_view1.column("Product", anchor=W, width=80)
        tree_view1.column("Quantity", anchor=W, width=80)
        tree_view1.column("Total Profit", anchor=W, width=80)
        tree_view1.heading("Product", text="Product", anchor=W)
        tree_view1.heading("Quantity", text="Quantity", anchor=W)
        tree_view1.heading("Total Profit", text="Total Profit", anchor=W)
        tree_view1.pack(side=LEFT, expand=True, fill=BOTH)
        scr1a.config(command=tree_view1.yview)
        scr1b.config(command=tree_view1.xview)

        tree_view2 = ttk.Treeview(tree_frame2, yscrollcommand=scr2a.set, xscrollcommand=scr2b.set)
        tree_view2["columns"] = ("Product Name", "Employee Margin", "Cost Price", "Selling Price")
        tree_view2.column("#0", width=0, stretch=NO)
        tree_view2.column("Product Name", anchor=W, width=140)
        tree_view2.column("Employee Margin", anchor=W, width=120)
        tree_view2.column("Cost Price", anchor=W, width=120)
        tree_view2.column("Selling Price", anchor=W, width=120)
        tree_view2.heading("Product Name", text="Product Name", anchor=W)
        tree_view2.heading("Employee Margin", text="Employee Margin", anchor=W)
        tree_view2.heading("Cost Price", text="Cost Price", anchor=W)
        tree_view2.heading("Selling Price", text="Selling Price", anchor=W)
        tree_view2.pack(side=LEFT, expand=True, fill=BOTH)
        scr2a.config(command=tree_view2.yview)
        scr2b.config(command=tree_view2.xview)

        tree_view3 = ttk.Treeview(tree_frame3, yscrollcommand=scr3a.set)
        tree_view3["columns"] = ("ID", "Name", "Fixed Salary", "% Salary from Collection", "Products Sold",
                                 "Estimated Income")
        tree_view3.column("#0", width=0, stretch=NO)
        tree_view3.column("ID", anchor=W, width=80)
        tree_view3.column("Name", anchor=W, width=80)
        tree_view3.column("Fixed Salary", anchor=W, width=80)
        tree_view3.column("% Salary from Collection", anchor=W, width=80)
        tree_view3.column("Products Sold", anchor=W, width=80)
        tree_view3.column("Estimated Income", anchor=W, width=80)
        tree_view3.heading("ID", text="ID", anchor=W)
        tree_view3.heading("Name", text="Name", anchor=W)
        tree_view3.heading("Fixed Salary", text="Fixed Salary", anchor=W)
        tree_view3.heading("% Salary from Collection", text="% Salary from Collection", anchor=W)
        tree_view3.heading("Products Sold", text="Products Sold", anchor=W)
        tree_view3.heading("Estimated Income", text="Estimated Income", anchor=W)
        tree_view3.pack(side=LEFT, expand=True, fill=BOTH)
        scr3a.config(command=tree_view3.yview)

        btn_1 = Button(child, text="Save File", font=("Calibre", 15, "bold"))
        btn_1.place(x=990, y=655, width=234, height=65)
        btn_2 = Button(child, text="Estimate Incomes", font=("Times New Roman", 22, "bold"))
        btn_2.place(x=990, y=390, width=234, height=52)
        btn_3 = Button(child, text="Add Record")
        btn_3.place(x=50, y=350, width=129, height=30)
        btn_4 = Button(child, text="Update Selected")
        btn_4.place(x=190, y=350, width=129, height=30)
        btn_5 = Button(child, text="Remove Selected")
        btn_5.place(x=330, y=350, width=129, height=30)
        btn_6 = Button(child, text="Remove All")
        btn_6.place(x=470, y=350, width=129, height=30)
        btn_7 = Button(child, text="Add Record", state=DISABLED, command=add_rec_tree1)
        btn_7.place(x=540, y=220, width=120, height=20)
        btn_8 = Button(child, text="Update Selected", state=DISABLED, command=upd_rec_tree1)
        btn_8.place(x=540, y=250, width=120, height=20)
        btn_9 = Button(child, text="Remove Selected", state=DISABLED, command=rem_select_rec_tree1)
        btn_9.place(x=540, y=280, width=120, height=20)
        btn_10 = Button(child, text="Remove All", state=DISABLED, command=rem_all_rec_tree1)
        btn_10.place(x=540, y=310, width=120, height=20)
        btn_11 = Button(child, text="Add Product")
        btn_11.place(x=760, y=200, width=211, height=30)
        btn_12 = Button(child, text="Update Selected Products")
        btn_12.place(x=760, y=240, width=211, height=30)
        btn_13 = Button(child, text="Remove Selected Products")
        btn_13.place(x=760, y=280, width=211, height=30)
        btn_14 = Button(child, text="Remove All")
        btn_14.place(x=760, y=320, width=211, height=30)

        v1 = IntVar()
        chk_btn1 = Checkbutton(child, text="Include Products", variable=v1, offvalue=0, onvalue=1, command=enable_prod)
        chk_btn1.place(x=420, y=0, width=208, height=38)

        v2 = IntVar()
        rad_btn1 = Radiobutton(child, text="Fixed Amount", bg="#b4b4b4", variable=v2, value=1, command=choose)
        rad_btn1.place(x=130, y=220, width=99, height=30)
        rad_btn2 = Radiobutton(child, text="Percentage Based", bg="#b4b4b4", variable=v2, value=2, command=choose)
        rad_btn2.place(x=128, y=250, width=122, height=30)

        lbl_1 = Label(child, text="Enter total collection:", font=f)
        lbl_1.place(x=30, y=0, width=146, height=30)
        lbl_2 = Label(child, text="Total Profit from Product Sale:", font=f, state=DISABLED)
        lbl_2.place(x=20, y=40, width=214, height=30)
        lbl_3 = Label(child, text="-", font=f, state=DISABLED)
        lbl_3.place(x=214, y=40, width=102, height=30)
        lbl_4 = Label(child, text="Collection excluding Product Sale:", font=f)
        lbl_4.place(x=30, y=70, width=216, height=30)
        lbl_5 = Label(child, text="-", font=f)
        lbl_5.place(x=240, y=70, width=111, height=31)
        lbl_6 = Label(child, text="ID:", font=f, bg="#b4b4b4")
        lbl_6.place(x=41, y=130, width=61, height=37)
        lbl_7 = Label(child, text="Name:", font=f, bg="#b4b4b4")
        lbl_7.place(x=41, y=170, width=82, height=32)
        lbl_8 = Label(child, text="Salary:", font=f, bg="#b4b4b4")
        lbl_8.place(x=42, y=208, width=82, height=39)
        lbl_9 = Label(child, text="Product:", font=f, bg="#b4b4b4", state=DISABLED)
        lbl_9.place(x=520, y=130, width=70, height=25)
        lbl_10 = Label(child, text="Quantity:", font=f, bg="#b4b4b4", state=DISABLED)
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
        entry_2.place(x=120, y=140, width=140, height=20)
        entry_3 = Entry(child, justify=CENTER)
        entry_3.place(x=120, y=180, width=140, height=20)
        entry_4 = Entry(child, fg="#b4b4b4", justify=CENTER, state=DISABLED)
        placeholder_ent4a = "Enter Amount"
        placeholder_ent4b = "Enter % Collection"
        entry_4.bind("<FocusIn>", when_focused1)
        entry_4.place(x=120, y=290, width=135, height=30)
        entry_5 = Entry(child, justify=CENTER, state=DISABLED)
        entry_5.place(x=590, y=170, width=79, height=30)
        entry_6 = Entry(child, justify=CENTER)
        entry_6.place(x=860, y=67, width=125, height=20)
        entry_7 = Entry(child, justify=CENTER)
        entry_7.place(x=860, y=100, width=125, height=20)
        entry_8 = Entry(child, justify=CENTER)
        entry_8.place(x=860, y=130, width=125, height=20)
        entry_9 = Entry(child, justify=CENTER)
        entry_9.place(x=860, y=160, width=125, height=20)

        global products
        products = ["Product1", "Product2", "Product3"]
        cmb_box = ttk.Combobox(child, values=products, state=DISABLED)
        cmb_box.place(x=590, y=130, width=80, height=25)
        cmb_box.bind("<Configure>", on_combo_configure)
    else:
        messagebox.showinfo("Limit reached!", "Can Open Only One Window")


f1 = ("Times New Roman", 20, "bold")
f = ("Calibre", 10)
global window_counter1
window_counter1 = 0
global count_tree1
count_tree1 = 0
global list_tree1
list_tree1 = []
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
crt_new = Button(root, text="Create New File", font=f1, justify="center", command=open_create)
crt_new.place(x=116, y=230, width=305, height=30)
src_old = Button(root, text="View Existing File", font=f1, justify="center", command=browse_folder)
src_old.place(x=116, y=280, width=306, height=30)
chat_bot = Button(root, image=chat_img, font=f, command=open_chatbot)
chat_bot.place(x=460, y=380, width=69, height=51)
global products


root.mainloop()
