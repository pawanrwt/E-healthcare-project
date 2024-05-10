import tkinter as tk
from PIL import Image, ImageTk
import login_frame as lo
class HomePanel(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = Image.open("b3.png")
        self.background_image = self.background_image.resize((1300, 1000)) 
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self, image=self.background_photo)
        self.background_label.image = self.background_photo
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.logo_image = Image.open("hospit.png")
        self.logo_image = self.logo_image.resize((200, 200))  
        self.logo_photo = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(self, image=self.logo_photo,bg="deepskyblue4")
        self.back_b = tk.Button(self, text="🔙", width=5, height=2, bg="white", command=self.exit, font=(50))
        
        self.login_up = tk.Button(self, text="Login", command=self.login_action, bg="#007bff", fg="white", width=29, relief=tk.FLAT)
        self.signing_up = tk.Button(self, text="Sign up", command=self.sign_up, bg="#28a745", fg="white", width=29, relief=tk.FLAT)
        
    def login_action(self):
        self.destroy()
        self.login_frame = lo.LoginPanel(self.master)
        self.login_frame.show()

    def sign_up(self):
        self.destroy()
        self.sign_up_frame = lo.Signup_Panel(self.master)
        self.sign_up_frame.signing()
    def pack_home(self):
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.back_b.pack(side="top", padx=(1200, 0), pady=7)
        self.logo_label.pack(padx=20, pady=(20, 8), anchor="center")
        self.login_up.place(relx=0.5, rely=0.5, anchor="center")
        self.signing_up.place(relx=0.5, rely=0.56, anchor="center")
    def exit(self):
        exit(0)
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("E-HEALTHCARE MANAGEMENT SYSTEM")
        self.hp = HomePanel(self)
    def show(self):
        self.hp.pack_home()
        self.mainloop()
if __name__ == "__main__":
    app = App()
    app.show()
