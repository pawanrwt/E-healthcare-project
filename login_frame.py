import tkinter as tk
import Backed_server as rs
import features as f
import getid as g
import fillinfo as fi

class LoginPanel(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = tk.PhotoImage(file="b1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.tag1 = tk.Label(self, text="User ID:", width=20, bg="dodgerblue2", fg="white")
        self.id_frame = tk.Entry(self, width=35)
        self.tag2 = tk.Label(self, text="Password:", width=20, bg="dodgerblue2", fg="white")
        self.password = tk.Entry(self, show="*", width=35)
        self.popup = tk.Label(self, text="", width=60, bg="dodgerblue2", fg="red")
        self.login_button = tk.Button(self, text="Login", font=('Arival', 10, 'bold'), command=self.login, bg="GREEN1", fg="white", width=10, relief=tk.FLAT)
        self.back_button = tk.Button(self, text="Back", font=('Arival', 10, 'bold'), command=self.backto, bg="cyan", fg="black", width=10, relief=tk.FLAT)
        
    def show(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.tag1.grid(row=1,column=4,padx=(140,4),pady=(150,7))
        self.id_frame.grid(row=1,column=4,padx=(550,50),pady=(150,7))
        self.tag2.grid(row=2,column=4,padx=(140,4),pady=11)
        self.password.grid(row=2,column=4,padx=(550,50),pady=1)
        self.login_button.grid(row=4,column=4,padx=(515,20), pady=10)
        self.back_button.grid(row=5,column=4,padx=(515,20), pady=10)

    def backto(self):
        self.destroy()
        self.b=f.Features(self.master)
        self.b.backtohome()

    def check_data(self):
        pid = self.id_frame.get()
        pasword=self.password.get()
        self.cr=rs.Code(self.master)
        check=self.cr.login(pid,pasword)
        self.password.delete(0, tk.END)
        print("ID and Password is vaild")
        if check==False:
            return False
        elif check=="False2":
            return "w_pass"
            
    def login(self):
        self.i=rs.Code(self.master)
        inter=self.i.check_internet()
        mat=self.check_data()
        if inter==False:
            self.popup.config(text="No internet connection. Please connect your device")
            self.popup.grid(row=3,column=4,padx=(500,30),pady=10,sticky="e")
        elif mat==False:
            self.popup.config(text="User not found. Please enter valid username..?")
            self.popup.grid(row=3,column=4,padx=(500,30),pady=10,sticky="e")
        elif mat=="w_pass":
            self.popup.config(text="Incorrect password. Please try again...!!!!!")
            self.popup.grid(row=3,column=4,padx=(500,30),pady=10,sticky="e")
        else:
            self.user_id=self.accessing()
            LoginPanel.last_user_id = self.user_id
            self.destroy()
            self.fe_frame = f.Features(self.master)
            self.fe_frame.packing()

    def accessing(self):
        self.Id=self.id_frame.get()
        LoginPanel.last_user_id = self.Id
        print("Your ID : " ,self.Id)
        return self.Id

class Signup_Panel(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = tk.PhotoImage(file="b1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.tag1 = tk.Label(self, text="User Name:", width=20, bg="dodgerblue2", fg="white")
        self.username = tk.Entry(self, width=35)
        self.tag2 = tk.Label(self, text="Password:", width=20, bg="dodgerblue2", fg="white")
        self.password = tk.Entry(self, show="*", width=35)
        self.popup = tk.Label(self, width=40, fg="red", bg="dodgerblue2")
        self.Sign_button = tk.Button(self, text="Create Account", command=self.creating, bg="green1", fg="white", width=20, relief=tk.FLAT)
        self.back_button = tk.Button(self, text="Back", command=self.backing, bg="cyan", fg="black", width=20, relief=tk.FLAT)
  
    def signing(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tag1.grid(row=1,column=4,padx=(140,4),pady=(150,7))
        self.username.grid(row=1,column=4,padx=(550,50),pady=(150,7))
        self.tag2.grid(row=2,column=4,padx=(140,4),pady=11)
        self.password.grid(row=2,column=4,padx=(550,50),pady=1)
        self.Sign_button.grid(row=4,column=4,padx=(515,20), pady=10)
        self.back_button.grid(row=5,column=4,padx=(515,20), pady=10)

    def save_data(self):
        self.name = self.username.get()
        self.pasword=self.password.get()
        self.cretae_new=rs.Code(self.master)
        gen_id=self.cretae_new.signup(self.name,self.pasword) 
        return gen_id
        
    def creating(self):
        ids=self.save_data()
        if ids==False:
            self.popup.config(text="Please Enter User Name and password.")
            self.popup.grid(row=3,column=4,padx=(515,20), pady=10)
        elif ids=="false1":
            self.popup.config(text="No internet connection. Please connect your device")
            self.popup.grid(row=3,column=4,padx=(515,20), pady=10)
        else:
            self.destroy()
            self.finfo=fi.Fillinfo(self.master)
            self.finfo.packed()
            
    def backing(self):
        LoginPanel.backto(self)
