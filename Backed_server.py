import mysql.connector
import tkinter as tk
import random as rd
import login_frame as lo
import requests

class Code(tk.Tk):
    def __init__(self, master, **kwargs):
        self.master = master
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='pawan82',
            database='Ehealthcare'
        )
        self.cur = self.mydb.cursor()
        c1 = '''CREATE TABLE IF NOT EXISTS SIGN_UP(
            USER_NAME VARCHAR(30) PRIMARY KEY,
            PASSWORD VARCHAR(12)
        )'''
        self.cur.execute(c1)
        self.mydb.commit()
        c2 = '''CREATE TABLE IF NOT EXISTS IDS(
            ID VARCHAR(7) PRIMARY KEY,
            PASSWORD VARCHAR(12),
            Name varchar(50)
        )'''
        self.cur.execute(c2)
        self.mydb.commit()

        c3 = '''CREATE TABLE IF NOT EXISTS Appointments(
                Patient_name Varchar(50),
                Specification varchar(30),
                Doctor_name VARCHAR(50),
                Phone varchar(20),
                email varchar(50),
                Appointment_date DATE,
                Appointment_time TIME,
                Location VARCHAR(80)
            )'''
        self.cur.execute(c3)
        self.mydb.commit()

    def check_internet(self):
        try:
            requests.get("http://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False
        
    def signup(self,f_name,password):
        try:
            conection=self.check_internet()
            if conection==False:
                raise Exception("No internet connection. Please connect your device")
            else:
                if f_name and password:
                    self.cur.execute("INSERT INTO SIGN_UP (USER_NAME, PASSWORD) VALUES (%s, %s)", (f_name,password))
                    self.mydb.commit()
                    print("Account created successfully.")

                    gen_id = 'EHC' + str(rd.randint(100, 999))
                    print(f"Your ID genrate : {gen_id}")
                    try:
                        with open('store.txt','w') as f:
                            f.write(gen_id)
                    except Exception as e:
                        print("File not found")

                    self.cur.execute("INSERT INTO IDS (ID, NAME, PASSWORD) VALUES (%s, %s, %s)", (gen_id,f_name, password))
                    self.mydb.commit()
                    return gen_id
                else:
                    return False
                
        except mysql.connector.Error as e:
            print("MySQL Error:", e)
        except Exception as e:
            print(e)
            return "false1"
            
    def login(self,Id,password):
        try:
            if not self.check_internet():
                raise Exception("No internet connection. Please connect your device")
            self.cur.execute("SELECT * FROM IDS WHERE ID = %s", (Id,))
            user = self.cur.fetchone()
            if user:
                stored_password = user[1]
                if password == stored_password:
                    print("Login successful......!")
                    return True
                else:
                    print("Incorrect password. Please try again...!!!!!")
                    return "False2"       
            else:
                print("User not found. Please enter valid username..?")
                return False
        except mysql.connector.Error as e:
            print("MySQL Error:", e)
        except Exception as e:
            print("Error:", e)

    def appointment(self, p_id, spe, doctor, ph, em, meet, timing, loc):
        try:
            if not self.check_internet():
                raise Exception("No internet connection. Please check your internet")

            self.cur.execute("SELECT NAME FROM IDS WHERE ID=%s", (p_id,))
            data = self.cur.fetchone()
            if data:
                patient_name = data[0]
                self.cur.execute("SELECT * FROM Appointments WHERE Patient_name = %s", (patient_name,))
                eapp = self.cur.fetchone()
                print("Patient name : ", patient_name)
                if eapp:
                        return f"Your appointment already fixed with {eapp[2]}."
                else:
                    print("Inserting info : ")
                    self.cur.execute("""INSERT INTO Appointments (Patient_name, Specification, Doctor_name, Phone, email, Appointment_date,
                                        Appointment_time, location) VALUES (%s, %s, %s, %s,%s,%s, %s, %s)""",(patient_name, spe, "Dr. " + doctor, ph, em, meet, timing, loc))
                    self.mydb.commit()
                    print("success fully")
                    return f"Your Appointment successfully fixed with Dr. {doctor} on {meet} at {timing}."
        except mysql.connector.Error as e:
            print("MySQL Error:", e)
            return "MySQL Error: " + str(e)
        except Exception as e:
            print("Exception:", e)
            return "Server is Down, Please try after few minutes"
            
    def cancel_appointment(self,p_id):
        try:
            if not self.check_internet():
                raise Exception("No internet connection. Please check your network settings.")
            self.cur.execute("SELECT NAME FROM IDS WHERE ID=%s", (p_id,))
            data = self.cur.fetchone()
            if data:
                patient_name =data[0]
            self.cur.execute("SELECT * FROM Appointments WHERE Patient_name = %s", (patient_name,))
            existing_appointment = self.cur.fetchone()
            
            if existing_appointment:
                self.cur.execute("DELETE FROM Appointments WHERE Patient_name = %s", (patient_name,))
                self.mydb.commit()
                print("Appointment for {} canceled successfully.".format(patient_name))
            else:
                print("No appointment found for {}.".format(patient_name))
        except mysql.connector.Error as e:
            print("MySQL Error:", e)
        except Exception as e:
            print("Error:", e)
     
    def show_list(self,spe):
        self.cur.execute("SELECT * FROM DR_LIST WHERE SPECIALIST=%s", (spe,))
        return self.cur.fetchall()
    
    def show_all(self):
        self.cur.execute("SELECT * FROM DR_LIST")
        return self.cur.fetchall()
    
    def log_out(self, p_id):
        self.cur.execute("SELECT NAME FROM IDS WHERE ID=%s", (p_id,))
        data = self.cur.fetchone()
        if data:
            f_name =data[0]
            self.cur.execute("DELETE FROM SIGN_UP WHERE USER_NAME=%s", (f_name,))
            self.mydb.commit()
            self.cur.execute("DELETE FROM IDS WHERE ID=%s", (p_id,))
            self.mydb.commit()
            self.cur.execute("DELETE FROM HEALTH WHERE Patient_id=%s",(p_id,))
            self.mydb.commit()
            print("Logout sucsessful")
        else:
            print("Data not fonud..")

    def check_appointment(self,p_id):
        self.cur.execute("SELECT NAME FROM IDS WHERE ID=%s",(p_id,))
        data=self.cur.fetchone()
        if data:
            p_name=data[0]
            self.cur.execute("SELECT Appointment_date, Doctor_name, Appointment_time FROM appointments where Patient_name=%s",(p_name,))
            d=self.cur.fetchone()
            if d:
                d1=d[0]
                d2=d[1]
                d3=d[2]
                return f"Your Appointment fixed with {d2} on {d1} at {d3} "
            else:
                return "You don't have any appointment"

    def healthD(self,ids):
            print("Your health deatils")
            self.cur.execute("SELECT NAME FROM IDS WHERE ID=%s",(ids,))
            data=self.cur.fetchone()
            print("Your name is : ",data[0])
            if data:
                self.cur.execute(" SELECT * FROM HEALTH WHERE PATIENT_NAME=%s",(data[0],))
                return self.cur.fetchall()
            else:
                print("NO information ")
                return "NO information "
 
        
            

