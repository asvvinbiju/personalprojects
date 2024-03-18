from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as flk, scrolledtext, Menu, messagebox

window = Tk()
window.geometry("1000x800")
window.minsize(800, 600)
window.title("NOTEPAD")

mainmenu = Menu(window)
window.config(menu=mainmenu)

def open_():
    note.delete("1.0", END)
    filetype = (("text", "*.txt*"), ("All files", "*.*"))
    textfile = flk.askopenfile(mode='r',
     title= "Open file",
     filetypes = filetype)
    l = 1.0
    for line in textfile:
        note.insert(l, line)
        l += 1.0


def new_():
    note.delete(1.0, END)


def save_():
    filecontent = note.get('1.0', END)
    filetype = (("text", "*.txt*"), ("All files", "*.*"))
    file_path = flk.asksaveasfilename(
     filetypes = filetype,
     title = "Save as",
     defaultextension = ".txt")
    if file_path:
        with open(file_path, "w") as fl:
            fl.write(filecontent)


def exit_():
    msg_box = messagebox.askyesno("Exit application", "Are you sure you want to exit?")
    if msg_box:
        n = note.get("1.0", END)
        print(len(n))
        if len(n) > 1:
            savee = messagebox.askyesno("Save file?", "Would you like to save before you leave?")
            if savee:
                filecontent = note.get('1.0', END)
                filetype = (("text", "*.txt*"), ("All files", "*.*"))
                file_path = flk.asksaveasfilename(
                    filetypes = filetype,
                    title = "Save as",
                    defaultextension = ".txt")
                if file_path:
                    with open(file_path, "w") as fl:
                        fl.write(filecontent)
                window.destroy()
            else:
                window.destroy()
        else:
            window.destroy()
    else:
        messagebox.showinfo("Return", "You are now returning to application!")


def font_():
    global fontsize
    global fontfamily
    fontsize = 15
    fontfamily = "Courier"
    # window.withdraw()
    msg_box = Toplevel(window)
    msg_box.geometry("375x200")
    msg_box.maxsize(375, 200)
    msg_box.minsize(375, 200)
    sel_val = StringVar()
    def on_click():
        fontsize = combo1.get()
        fontfamily = combo2.get()
        note.config(font=(fontfamily, int(fontsize)))
        msg_box.destroy()
        # window.deiconify()

    
    Label(msg_box, text="Font size").place(relx=0.170, rely=0.100)

    combo1 = Combobox(msg_box, values=[15,18,20,24,27,30])
    combo1.set(fontsize)
    combo1.place(relx=0.370, rely=0.100)

    Label(msg_box, text="Font family").place(relx=0.170, rely=0.300)

    combo2 = Combobox(msg_box, values=['Courier','Verdana','Times','Helvetica','Comic San MS'])
    combo2.set(fontfamily)
    combo2.place(relx=0.370, rely=0.300)

    ok_button = Button(msg_box, command=on_click, text="OK")
    ok_button.place(relx=0.400, rely=0.600)

    msg_box.wait_window()


file_menu = Menu(mainmenu, tearoff= 0)
file_menu.add_command(label = "New", command= new_, font=("Times",15))
file_menu.add_command(label = "Save", command = save_, font=("Times",15))
file_menu.add_command(label = "Open", command= open_, font=("Times",15))
file_menu.add_command(label = "Exit", command= exit_, font=("Times",15))
mainmenu.add_cascade(label = "Menu", menu= file_menu, font=("Times",15))
edit_menu = Menu(mainmenu, tearoff=0)
edit_menu.add_command(label= "Font", command= font_, font=("Times", 15))
mainmenu.add_cascade(label = "Edit", menu = edit_menu, font=("Times",15))


note = scrolledtext.ScrolledText(window,font=("Courier", 13))
note.pack(expand=True, fill=BOTH)


window.mainloop()
