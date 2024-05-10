import tkinter as tk
import all_feature as af
import homeinterface as h
import login_frame as l
import Backed_server as r

class Features(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = tk.PhotoImage(file="b1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.appointment=tk.Button(self, text="Book Appointment", command=self.book_ap, bg="green1", fg="Black", width=28, relief=tk.FLAT)
        self.dr_deatail=tk.Button(self, text="Doctors Details", command=self.dr_info, bg="green1", fg="black", width=28, relief=tk.FLAT)
        self.cencel_a=tk.Button(self, text="Cancel Appointement", command=self.cencel_app, bg="green1", fg="black", width=28, relief=tk.FLAT)
        self.chealth=tk.Button(self, text="Check Your Health Details", command=self.health, bg="green1", fg="black", width=28, relief=tk.FLAT)
        self.clast_ap=tk.Button(self, text="Check your appointment Status", command=self.last_app, bg="green1", fg="black", width=28, relief=tk.FLAT)
        self.logout=tk.Button(self, text="Logout", command=self.logouting, bg="green1", fg="black", width=28, relief=tk.FLAT)
        self.back_button=tk.Button(self, text="Back", command=self.backtohome, bg="green1", fg="black", width=28, relief=tk.FLAT)

    def book_ap(self):
        self.destroy()
        self.booking=af.Appointment(self.master)
        self.booking.packed()

    def dr_info(self):
        self.destroy()
        self.dr=af.Dr_details(self.master)
        self.dr.pack_dr()

    def cencel_app(self):
        self.destroy()
        self.cen=af.Cancel_App(self.master)
        self.cen.cancel_pack()

    def health(self):
        self.destroy()
        self.sd=af.Health(self.master)
        self.sd.show_health()
        
    def last_app(self):
        self.destroy()
        self.ca=af.Check_app(self.master)
        self.ca.check_end()

    def logouting(self):
        self.out=l.LoginPanel(self.master)
        p_id=self.out.last_user_id
        self.log=r.Code(self.master)
        self.log.log_out(p_id)
        self.backtohome()

    def backtohome(self):
        self.destroy()
        self.b=h.HomePanel(self.master)
        self.b.pack_home()
        
    def packing(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.pack( fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.appointment.pack(padx=20, pady=(120,10), anchor="center")
        self.dr_deatail.pack(padx=20, pady=10, anchor="center")
        self.cencel_a.pack(padx=20, pady=10, anchor="center")
        self.chealth.pack(padx=20, pady=10, anchor="center")
        self.clast_ap.pack(padx=20, pady=10, anchor="center")
        self.logout.pack(padx=20, pady=10, anchor="center")
        self.back_button.pack(padx=20, pady=10, anchor="center")
        

