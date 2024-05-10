import tkinter as tk
import login_frame as lf

class Getids(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.mframe=tk.Frame(self, width=10, height=4,bd=10,relief=tk.RAISED ,bg="black")
        self.msz=tk.Label(self.mframe,text="",width=50,height=3,bd=2,relief="ridge",font=("Arival",21))
        self.ok=tk.Button(self.mframe, text="ok", command=self.gologin, bg="#007bff", fg="white", width=10, relief=tk.FLAT)
    def getting(self,ids):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.mframe.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.msz.config(text=f" your id is : {ids}. Now login with your ID and Password.")
        self.msz.pack(padx=20,pady=(200,10),anchor="center")
        self.ok.pack(padx=20,pady=20,anchor="center")
        print("ID show successfully")
    def gologin(self):
        self.destroy()
        with open('store.txt','r+') as f:
            f.truncate()
            print("Turncate successfull")
        self.log=lf.LoginPanel(self.master)
        self.log.show()
        print("After get Id you are in login frame")

