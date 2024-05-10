import tkinter as tk
import features as f
import login_frame as lof
import Backed_server as r
import fillinfo as rq

class Appointment(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.mframe = tk.Frame(self, width=1500, height=4000, bd=10,  relief="raised",bg="black",)
        self.dr_frame = tk.Listbox(self.mframe, bd=2,relief="solid",width=80,height=10,bg="black")
        self.insertion=tk.Frame(self.mframe,width=120,height=10,bg="black")
        self.specify = tk.Entry(self.insertion, width=35,)
        self.specify.insert(0,"Specialist")
        self.search = tk.Button(self.insertion, width=15, fg="white", bg="green",text="🔍 Search Dr.", command=self.perform_search)
        self.details=tk.Label(self.dr_frame,text="Dr. Name",bd=2,relief="raised",bg="red")
        self.details1=tk.Label(self.dr_frame,text="Specification",bd=2,relief="raised",bg="yellow")
        self.details2=tk.Label(self.dr_frame,text="Work Experience",bd=2,relief="raised",bg="Orange")
        self.details3=tk.Label(self.dr_frame,text="Shif",bd=2,relief="raised",bg="Orange")
        self.dr_name = tk.Entry(self.insertion, width=35)
        self.dr_name.insert(0,"Select Dr. name")
        self.phn = tk.Entry(self.insertion, width=35)
        self.phn.insert(0,"Mobile number")
        self.emails = tk.Entry(self.insertion, width=35,)
        self.emails.insert(0,"Email")
        self.Adate = tk.Entry(self.insertion, width=35)
        self.Adate.insert(0,"yyyy-mm-dd")
        self.atime = tk.Entry(self.insertion, width=35)
        self.atime.insert(0,"Time (00:00)")
        self.location = tk.Entry(self.insertion, width=35)
        self.location.insert(0,"Your Location")
        self.buttons = tk.Frame(self.insertion,bg="black")
        self.back_button = tk.Button(self.buttons,text="Back",font=('Helvetica' ,10 ,'bold') ,command=self.backto, bg="cyan", fg="black", width=15, relief=tk.FLAT)
        self.confirm_button = tk.Button(self.buttons, text="Confirm",font=('Helvetica' ,10 ,'bold'), command=self.confirm, bg="blue", fg="white", width=15, relief=tk.FLAT)

    def save_entrys(self):
        spe = self.specify.get()
        doctor = self.dr_name.get()
        with open('store.txt','w') as f:
            f.write(doctor)
        ph=self.phn.get()
        em=self.emails.get()
        print("Phone:",ph,"email :",em)
        meet = self.Adate.get()
        timing = self.atime.get()
        loc = self.location.get()
        self.Id=lof.LoginPanel(self.master)
        p_id=self.Id.last_user_id
        self.booking = r.Code(self.master)
        inserting=self.booking.appointment(p_id, spe, doctor,ph,em, meet, timing, loc)
        self.specify.delete(0, tk.END)
        self.dr_name.delete(0, tk.END)
        self.phn.delete(0, tk.END)
        self.emails.delete(0, tk.END)
        self.Adate.delete(0, tk.END)
        self.atime.delete(0, tk.END)
        self.location.delete(0, tk.END)
        print("msz ",inserting)
        return inserting

    def perform_search(self):
        for widget in self.dr_frame.winfo_children():
            print("Dr info clear")
            if widget not in [self.details, self.details1, self.details2, self.details3]:
                widget.destroy()
        self.dr_frame.pack(side="right",fill="both",padx=10,pady=10)
        self.details.grid(row=1,column=0,padx=10,pady=5)
        self.details1.grid(row=1,column=1,padx=10,pady=5)
        self.details2.grid(row=1,column=2,padx=10,pady=5)
        self.details3.grid(row=1,column=3,padx=(5,2),pady=5)
        speci = self.specify.get()
        self.data = r.Code(self.master)
        show = self.data.show_list(speci)
        print("Dr list : ",show)
        i=2
        for s in show:
            self.label_text1= tk.Label(self.dr_frame,text=f"{s[0]}",bg="black",font=("Arival",12),fg="white")
            self.label_text2= tk.Label(self.dr_frame,text=f"{s[1]}",bg="black",font=("Arival",12),fg="white")
            self.label_text3= tk.Label(self.dr_frame,text=f"{s[2]}",bg="black",font=("Arival",12),fg="white")
            self.label_text4= tk.Label(self.dr_frame,text=f"{s[3]}",bg="black",font=("Arival",12),fg="white")
            self.label_text1.grid(row=i,column=0,padx=20,pady=5)
            self.label_text2.grid(row=i,column=1,padx=20,pady=5)
            self.label_text3.grid(row=i,column=2,padx=20,pady=5)
            self.label_text4.grid(row=i,column=3,padx=20,pady=5)
            i=i+1
        
    def backto(self):
        self.destroy()
        self.bf=f.Features(self.master)
        self.bf.packing()
        
    def confirm(self):
        msz=self.save_entrys()
        dr=rq.Require(self.master)
        dr.Udr()
        self.destroy()
        packing=Getmsz(self.master)
        packing.getting(msz)

    def packed(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.mframe.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.insertion.pack(side="left",expand=True, fill="both",padx=(300,5),pady=20)
        self.specify.grid(row=1,column=0,padx=25,pady=(20,4))
        self.search.grid(row=3,column=0,padx=25,pady=(2,10))
        self.dr_name.grid(row=4,column=0,padx=25,pady=20)
        self.phn.grid(row=5,column=0,padx=25,pady=20)
        self.emails.grid(row=6,column=0,padx=25,pady=20)
        self.Adate.grid(row=7,column=0,padx=25,pady=20)
        self.atime.grid(row=8,column=0,padx=25,pady=20)
        self.location.grid(row=9,column=0,padx=25,pady=20)
        self.buttons.grid(row=10,column=0,padx=25,pady=20)
        self.back_button.grid(row=1,column=0,padx=25,pady=10)
        self.confirm_button.grid(row=1,column=1,padx=2,pady=10)


class Getmsz(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.mframe = tk.Frame(self, width=10, height=4, bd=10, relief=tk.RAISED, bg="black")
        self.msz = tk.Label(self.mframe, text="", width=100, height=3, bd=2, relief="ridge", font=("Arial", 21))
        self.ok = tk.Button(self.mframe, text="OK", command=self.gofeature, bg="#007bff", fg="white", width=10, relief=tk.FLAT)

    def getting(self, popup_text):
        self.msz.config(text=popup_text)
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.mframe.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.msz.pack(padx=20, pady=(200, 10), anchor="center")
        self.ok.pack(padx=20, pady=20, anchor="center")
    def gofeature(self):
        self.destroy()
        Appointment.backto(self)
        
class Dr_details(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
        self.mframe = tk.Frame(self,width=1500, height=4000,bg="black", bd=10,  relief=tk.RAISED)
        self.mlabel = tk.Label(self.mframe, text="Here is Doctors Details :",font=("Arival",23),width=25,height=1,bg="black",fg="white")
        
        self.dr_frame = tk.Frame(self.mframe,width=120,height=700,bg="deepskyblue")
        self.details=tk.Label(self.dr_frame,text="Dr. Name",font=("Arival" ,15 ,'bold'),bg="deepskyblue",fg="black")
        self.details1=tk.Label(self.dr_frame,text="Specialist",bg="deepskyblue",fg="black",font=("Arival" ,15 ,'bold'))
        self.details2=tk.Label(self.dr_frame,text="Work Experience",bg="deepskyblue",font=("Arival" ,15 ,'bold'))
        self.details3=tk.Label(self.dr_frame,text="Shift",bg="deepskyblue",fg="black",font=("Arival" ,15 ,'bold'))
        self.details4=tk.Label(self.dr_frame,text="Phone No.",bg="deepskyblue",fg="black",font=("Arival" ,15 ,'bold'))
        self.back_button = tk.Button(self.mframe, text="Back", command=self.back, bg="green1", fg="white", width=15, relief=tk.FLAT)

    def pack_dr(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.mframe.pack(fill=tk.BOTH, expand=True, padx=15, pady=1)
        self.mlabel.pack(anchor="center",padx=90,pady=(1,8))
        self.dr_frame.pack(fill="both",expand=True,padx=20, pady=(0,8), anchor="center")

        self.details.grid(row=1,column=0,padx=(200,20),pady=20)
        self.details1.grid(row=1,column=1,padx=30,pady=20)
        self.details2.grid(row=1,column=2,padx=30,pady=20)
        self.details3.grid(row=1,column=3,padx=30,pady=20)
        self.details4.grid(row=1,column=4,padx=30,pady=20)
        self.dr_d=r.Code(self.master)
        dr_l=self.dr_d.show_all()
        i=2
        for s in dr_l:
            self.label_text1= tk.Label(self.dr_frame,text=f"{s[0]}",bg="deepskyblue",fg="black",font=("Arival",18,'bold'))
            self.label_text2= tk.Label(self.dr_frame,text=f"{s[1]}",bg="deepskyblue",fg="black",font=("Arival",18))
            self.label_text3= tk.Label(self.dr_frame,text=f"{s[2]}",bg="deepskyblue",fg="black",font=("Arival",18))
            self.label_text4= tk.Label(self.dr_frame,text=f"{s[3]}",bg="deepskyblue",fg="black",font=("Arival",18))
            self.label_text5= tk.Label(self.dr_frame,text=f"{s[4]}",bg="deepskyblue",fg="black",font=("Arival",18))
            self.label_text1.grid(row=i,column=0,padx=(200,20),pady=5)
            self.label_text2.grid(row=i,column=1,padx=30,pady=5)
            self.label_text3.grid(row=i,column=2,padx=30,pady=5)
            self.label_text4.grid(row=i,column=3,padx=30,pady=5)
            self.label_text5.grid(row=i,column=4,padx=30,pady=5)
            i=i+1
        self.back_button.pack(anchor="center",padx=90,pady=8)

    def back(self):
        Appointment.backto(self)

class Cancel_App(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = tk.PhotoImage(file="b1.png")
        self.mframe = tk.Label(self, image=self.background_image)
        self.mframe.place(x=0, y=0, relwidth=1, relheight=1)
        self.id = lof.LoginPanel(self.master)
        p_id = self.id.last_user_id
        self.c = r.Code(self.master)
        ask = self.c.check_appointment(p_id)
        self.another = tk.Frame(self.mframe, width=20, height=10, bg="dodgerblue2")
        self.boxlabel = tk.Label(self.another, text=f"{ask}", font=('arial', 19, 'bold'), bg="dodgerblue2")
        self.popup = None 
        if ask == "You don't have any appointment":
            self.buttons = tk.Label(self.another, bg="dodgerblue2")
            self.nob = tk.Button(self.buttons, text="Back", bg="green", fg="black", width=10, relief=tk.FLAT, command=self.no)
        else:
            self.popup = tk.Label(self.another, text="Are you sure you want to cancel your appointment?", bg="dodgerblue2", font=('arial', 14))
            self.buttons = tk.Label(self.another, bg="dodgerblue2")
            self.yesb = tk.Button(self.buttons, text="Yes", bg="red", fg="white", width=10, relief=tk.FLAT, command=self.yes)
            self.nob = tk.Button(self.buttons, text="No", bg="green", fg="black", width=10, relief=tk.FLAT, command=self.no)

    def cancel_pack(self):
        self.pack(fill=tk.BOTH, expand=True)
        self.another.pack(padx=50, pady=100, anchor="center")
        self.boxlabel.pack(padx=10, pady=120, anchor="center")
        if self.popup:
            self.popup.pack(padx=10, pady=10, anchor="center")
        self.buttons.pack(padx=10, pady=16, anchor="center")
        self.nob.grid(row=2, column=0, padx=8, pady=20)
        if hasattr(self, 'yesb'):
            self.yesb.grid(row=2, column=2, padx=8, pady=20)


        
    def yes(self):
        self.Id=lof.LoginPanel(self.master)
        Id=self.Id.last_user_id
        self.cen=r.Code(self.master)
        self.cen.cancel_appointment(Id)
        Appointment.backto(self)

    def no(self):
        Appointment.backto(self)

class Check_app(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.id=lof.LoginPanel(self.master)
        p_id=self.id.last_user_id
        self.check=r.Code(self.master)
        checking=self.check.check_appointment(p_id)
        self.background_image = tk.PhotoImage(file="b1.png")
        self.mframe = tk.Label(self, image=self.background_image)
        self.mframe.place(x=0, y=0, relwidth=1, relheight=1)
        self.msz=tk.Label(self.mframe,text=f"{checking}",width=100,height=3,bd=3,relief="raised")
        self.back_but=tk.Button(self.mframe,text="Back",bg="Black",fg="white",width=10,relief=tk.FLAT,command=self.backing)
    def check_end(self):
        self.pack(fill=tk.BOTH,expand=True)
        self.msz.pack(padx=10,pady=100,anchor="center")
        self.back_but.pack(padx=10, pady=10,anchor="center")

    def backing(self):
        Appointment.backto(self)

class Health(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = tk.PhotoImage(file="b1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.info = tk.Label(self, text="Your Health Details",bg="deepskyblue",fg="Black" ,font=("Arival",20,'bold'),width=62,height=3, bd=1, relief="solid")
        self.heading_frame = tk.Frame(self, bg="mediumspringgreen",width=60,height=3, bd=1, relief="ridge")
        self.blood = tk.Label(self.heading_frame,bg="mediumspringgreen", text="Blood Group",height=3,font=('bold'))
        self.Bp = tk.Label(self.heading_frame,bg="mediumspringgreen", text="Blood Presure",font=('bold'))
        self.CurrentP = tk.Label(self.heading_frame, bg="mediumspringgreen",text="Current Health Issues",font=('bold'))
        self.treat = tk.Label(self.heading_frame,bg="mediumspringgreen", text="Treatment By",font=('bold'))
        self.emc = tk.Label(self.heading_frame,bg="mediumspringgreen", text="Emergency Contacts",font=('bold'))
        self.content_box = tk.Frame(self, width=80,height=100, bd=2, relief="raised")
        self.show=tk.Frame(self,width=80,height=4,bg="dodgerblue2")
        self.tag=tk.Label(self.show,text="You can update your Blood Pressure record: ",font=("Arival",14,'bold'),bg="dodgerblue2",fg="black")
        self.l1=tk.Label(self.show,text="HBP",width=30,font=("Arival",12,'bold'),bg="dodgerblue2",fg="white")
        self.l2=tk.Label(self.show,text="LBP",width=30,relief="flat",font=("Arival",12,'bold'),bg="dodgerblue2",fg="white")
        self.hbp=tk.Entry(self.show,width=30,relief="solid")
        self.lbp=tk.Entry(self.show,width=30,relief="solid")   
        
        self.popu=tk.Label(self.show,bg="dodgerblue2",fg="red",font=("Arival",13,'bold'))
        self.confirm=tk.Button(self.show,width=8,bg="green1",text="Confirm",command=self.confirmbut)
        self.backb = tk.Button(self.show, text="Back", bg="black",fg="white", width=8, command=self.back)
    
    def show_health(self):
        self.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=15, pady=(15, 0))
        self.info.pack(padx=30, pady=(100, 1))
        self.heading_frame.pack(padx=30, pady=1)
        self.blood.grid(row=0, column=0, padx=40)
        self.Bp.grid(row=0, column=1, padx=(35, 65))
        self.CurrentP.grid(row=0, column=2, padx=(20, 65))
        self.treat.grid(row=0, column=3, padx=40)
        self.emc.grid(row=0, column=4, padx=50)
        self.content_box.propagate(False)
        self.content_box.pack(padx=20, pady=1)
        self.d = lof.LoginPanel(self.master)
        ids=self.d.last_user_id
        self.f=r.Code(self.master)
        dr_l = self.f.healthD(ids)
        print(dr_l)

        for s in dr_l:
            self.label_text1 = tk.Label(self.content_box, text=f"{s[2]}", font=("Arial", 12))
            self.label_text2 = tk.Label(self.content_box, text=f"{s[3]}", font=("Arial", 12))
            self.label_text3 = tk.Label(self.content_box, text=f"{s[4]}", font=("Arial", 12))
            self.label_text4 = tk.Label(self.content_box, text=f"{s[5]}", font=("Arial", 12))
            self.label_text5 = tk.Label(self.content_box, text=f"{s[6]}", font=("Arial", 12))
            self.label_text1.grid(row=0, column=1, padx=65)
            self.label_text2.grid(row=0, column=2, padx=65)
            self.label_text3.grid(row=0, column=3, padx=70)
            self.label_text4.grid(row=0, column=4, padx=65)
            self.label_text5.grid(row=0, column=5, padx=65)

        self.show.config(highlightbackground="WHITE", highlightthickness=10)
        self.show.pack(padx=20, pady=40)
        self.tag.grid(row=1, column=0, padx=10, pady=10)
        self.l1.grid(row=2, column=0, padx=5, pady=20)
        self.l2.grid(row=2, column=1, padx=5, pady=20)
        self.hbp.grid(row=3, column=0, padx=5, pady=10)
        self.lbp.grid(row=3, column=1, padx=5, pady=10)
        lb=120
        hb=80
        try:
            with open('store.txt','r') as fi:
                data=fi.read()
                hb=data[0:3]
                lb=data[3:]
               
                lb=int(lb)
                hb=int(hb)

                if hb>150 or lb<60:
                    self.popu.config(text="Please take treatment from your Doctor \n and Take a rest")
                    self.popu.grid(row=4,column=0,padx=1,pady=1)
                    print("grid closing ")
                elif hb>130 or lb<70:
                    self.popu.config(text="Please take rest")
                    self.popu.grid(row=4,column=0,padx=1,pady=1)
                    
                    
        except Exception as e:
            print(e)
        with open ('store.txt','w') as w:
            w.write("")
        self.backb.grid(row=4,column=1,padx=(300,10),pady=40,sticky="e")
        self.confirm.grid(row=4, column=2, padx=(5,30), pady=40,sticky="e")
        
        
    def save_bp(self):
        hb=self.hbp.get()
        lb=self.lbp.get()
        with open('store.txt','w') as f:
            f.write(hb)
            f.write(lb)
        self.u=rq.Require(self.master)
        self.u.updateBP(hb,lb)
        self.hbp.delete(0,tk.END)
        self.lbp.delete(0,tk.END)

    def confirmbut(self):
        self.save_bp()
        self.destroy()
        refersh=Health(self.master)
        refersh.show_health()
        

                
        

    def back(self):
        Appointment.backto(self)

    
