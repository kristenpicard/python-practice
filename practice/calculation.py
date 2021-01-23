import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets(master)

    def create_widgets(self, master=None):
        self.button1 = tk.Button(self, text="QUIT", fg="red")
        self.button1.grid(row=2,column=1)
        self.button1["text"] = "1"
        self.button1["command"] = command=self.add
        
        self.button2 = tk.Button(self, text="QUIT", fg="red")
        self.button2.grid(row=1,column=1)
        self.button2["text"] = "1"
        self.button2["command"] = command=self.add

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.button1.grid(row=3,column=1)


    def add(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Application(root)
app.mainloop()