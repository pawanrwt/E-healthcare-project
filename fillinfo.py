import mysql.connector
import tkinter as tk
import login_frame as lf
import getid as gi

class Fillinfo(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pawan82',
            database='Ehealthcare'
        )
        self.cur = self.mydb.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS DR_LIST(
        DR_NAME VARCHAR(50) PRIMARY KEY,
        SPECIALIST VARCHAR(100),
        WORK_EXP VARCHAR(12),
        SHIFT varchar(10),
        Phone varchar(11)
        )''')
        self.mydb.commit()
        #health details table
        self.cur.execute('''CREATE TABLE IF NOT EXISTS Health(
        Patient_id varchar(7) PRIMARY KEY,
        Patient_Name varchar(50), 
        Blood_Group varchar(6) NOT NULL,
        Blood_pressure varchar(20) NOT NULL,
        Current_health_issue VARCHAR(80),
        Treatment_by Varchar(50),
        Emc_contact varchar(12) NOT NULL
        )''')
        self.mydb.commit()
        
        self.background_image = tk.PhotoImage(file="b1.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.mszlabel=tk.Label(self,text="Please fill your information : ",font=("Arival",15,'bold'),width=30,fg="green1",bg="dodgerblue2")
        self.age=tk.Label(self,text="Age",font=("Arival",13,'bold'),fg="black",bg="dodgerblue2",width=20)
        
        self.bloodL = tk.Label(self,text="Blood Group", font=("Arival",13,'bold'),fg="black",bg="dodgerblue2",width=20)
        self.hbp=tk.Label(self,text="HBP"  ,font=("Arival",13,'bold'),fg="black",bg="dodgerblue2" ,width=20)
        self.lbp=tk.Label(self,text="LBP"  , font=("Arival",13,'bold'),fg="black",bg="dodgerblue2",width=20)
        self.dr_name=tk.Label(self,text="Doctor Name (optional) "  ,font=("Arival",13,'bold'),fg="black",bg="dodgerblue2" ,width=20)
        self.currentH=tk.Label(self,text="Current Health Issue"  ,font=("Arival",13,'bold'),fg="black",bg="dodgerblue2" ,width=20)
        self.phno=tk.Label(self,text="Phone No. "  ,font=("Arival",13,'bold'),fg="black",bg="dodgerblue2" ,width=20)
        self.agep=tk.Entry(self,width=35)
        self.blood = tk.Entry(self, width=35)
        self.bph= tk.Entry(self, width=35)
        
        self.bpl = tk.Entry(self, width=35,)
        
        self.healthi = tk.Entry(self, width=35)
        self.drN= tk.Entry(self, width=35)
        self.mobile= tk.Entry(self, width=35)
        
        self.popup=tk.Label(self,bg="dodgerblue2",text="Please fill all entries",font=("Arival",10,'bold'),fg="red")
        self.submitB = tk.Button(self, text="Submit",font=('Helvetica' ,10 ,'bold'), command=self.confirm, bg="blue", fg="white", width=15, relief=tk.FLAT)
    
    
    
    def save_entrys(self):
        b = self.blood.get()
        bh = self.bph.get()
        bl=self.bpl.get()
        hi=self.healthi.get()
        dr = self.drN.get()
        mo = self.mobile.get()
        if b =="" or bh  =="" or bl  =="" or hi  =="" or mo  =="":
            print("You can't")
            self.popup.grid(row=8,column=1,padx=(40,10),pady=5)

            return False
        else:
            with open('store.txt','r+') as f:
                pid=f.read()
            pname=Require.getname(self)
            if dr=="":
                dr=" "
            
            Require.insert_health(self,pid,pname,b,bh,bl,hi,dr,mo)
            self.blood.delete(0,tk.END)
            self.bph.delete(0,tk.END)
            self.bpl.delete(0,tk.END)
            self.healthi.delete(0,tk.END)
            self.drN.delete(0,tk.END)
            self.mobile.delete(0,tk.END)
            return True
        
    def confirm(self):
        check=self.save_entrys()
        if check==True:
            self.destroy()
            with open('store.txt','r+') as f:
                ids=f.read()
            print("Your id get to get : ",ids)
            self.g=gi.Getids(self.master)
            self.g.getting(ids)
        
    def packed(self):
        self.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        self.mszlabel.grid(row=0,column=1,padx=(10,1),pady=(60,30))
        self.age.grid(row=1,column=0,padx=(400,10),pady=(40,10))
        self.agep.grid(row=1,column=1,padx=(50,10),pady=(40,10))
        self.bloodL.grid(row=2,column=0,padx=(400,10),pady=10)
        self.blood.grid(row=2,column=1,padx=(50,10),pady=10)
        self.hbp.grid(row=3,column=0,padx=(400,10),pady=10)
        self.bph.grid(row=3,column=1,padx=(50,10),pady=10)
        self.lbp.grid(row=4,column=0,padx=(400,10),pady=10)
        self.bpl.grid(row=4,column=1,padx=(50,10),pady=10)
        self.currentH.grid(row=5,column=0,padx=(400,10),pady=10)
        self.healthi.grid(row=5,column=1,padx=(50,10),pady=10)
        self.dr_name.grid(row=6,column=0,padx=(400,10),pady=10)
        self.drN.grid(row=6,column=1,padx=(50,10),pady=10)
        self.phno.grid(row=7,column=0,padx=(400,10),pady=10)
        self.mobile.grid(row=7,column=1,padx=(50,10),pady=10)
        self.submitB.grid(row=9,column=1,padx=(50,10),pady=40)
        
class Require(tk.Tk):
    def __init__(self, master, **kwargs):
        self.master = master
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pawan82',
            database='Ehealthcare'
        )
        self.cur = self.mydb.cursor()
        #Doctor table
        
        
    def insert_health(self,pid,p_name,bg,Hbp,Lbp,chi,tb,mo):
        try:
            self.cur.execute("INSERT INTO HEALTH ( Patient_id,Patient_Name,Blood_Group,Blood_pressure,Current_health_issue,Treatment_by,Emc_contact) VALUES (%s,%s,%s,%s,%s,%s,%s)", (pid,p_name,bg, Hbp+"/"+Lbp+" mm Hg",chi,"Dr. "+tb,mo))
            self.mydb.commit() 
            print("successfully") 
        except Exception as e:
            print(e)
    def Udr(self):
        try:
            ids=lf.LoginPanel.last_user_id
            self.cur.execute("SELECT Treatment_by FROM HEALTH WHERE Patient_id=%s",(ids,))
            data=self.cur.fetchone()
            
            print("Dr name : ",data[0])
            if (data[0]== "Dr.  " or data[0]):
                with open('store.txt','r') as f:
                        dr=f.read()  
                        self.cur.execute("UPDATE HEALTH SET Treatment_by =%s WHERE PATIENT_ID=%s",("Dr. "+dr,ids))
                        self.mydb.commit()
                        f.truncate()
            else:
                print("Doctor already fixed")
                with open('store.txt','r') as f:
                    f.truncate()
                
               
        except Exception as e:
            print(e)

    def getname(self):
        try:
            with open('store.txt','r') as f:
                ids=f.read()
            self.cur.execute("SELECT NAME FROM IDS WHERE ID = %s", (ids,))
            result = self.cur.fetchone()
            if result:
                return result[0]
            else:
                return None
        except Exception as e:
            print("Error fetching name:", e)
            return None

    
    def insert_dr(self,dname,spe,wexp,shift,ph):
        try:
            self.cur.execute("INSERT INTO DR_LIST (DR_NAME,SPECIALIST,WORK_EXP,shift,Phone) VALUES (%s,%s,%s,%s,%s)", ("Dr. "+dname,spe, wexp +" years",shift,ph))
            self.mydb.commit()
        except Exception as e:
            print("can't : ",e)

    def updateBP(self,hb,lb):
        try:
            ids=lf.LoginPanel.last_user_id
            self.cur.execute("SELECT NAME FROM IDS WHERE ID = %s", (ids,))
            p_name = self.cur.fetchone()
            print(p_name)
            print("here is ok")
            print("Name is upadate: ",p_name[0])
            self.cur.execute("UPDATE HEALTH SET BLOOD_PRESSURE=%s WHERE PATIENT_NAME=%s",(hb+"/"+lb+" mm Hg",p_name[0]))
            self.mydb.commit()
            print("yes yes")
        except Exception as e:
            print("Error : ",e)
        
class Store(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.geometry("800x600")
        self.title("E-HEALTHCARE MANAGEMENT SYSTEM")
        self.r=Require(self)
        self.f=Fillinfo(self)
    def show(self):
        self.f.packed()
        self.mainloop()

if __name__ == "__main__":
    app = Store()
    app.show()
