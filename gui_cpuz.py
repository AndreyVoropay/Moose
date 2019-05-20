import tkinter


class Main(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()        


    def init_main(self):
        toolbar = tkinter.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tkinter.TOP, fill=tkinter.X)

        self.add_img = tkinter.PhotoImage(file='add.gif')
        btn_open_dialog = tkinter.Button(toolbar, text='Add position',
                                         command=self.open_dialog,
                                         bg='#d7d8e0', bd=0,
                                         compound=tkinter.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tkinter.LEFT)


    def open_dialog(self):
        Chield()


class Chield(tkinter.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        

    def init_child(self):
        self.title('Add')
        self.geometry('400x220+200+200')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root = tkinter.Tk()
    app  = Main(root)
    app.pack()
    root.title('Test 1')
    root.geometry('650x450+100+100')
    root.resizable(True, True)
    root.mainloop()
