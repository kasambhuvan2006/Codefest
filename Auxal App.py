from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import re
import smtplib
from tkinter import messagebox
import sqlite3



root = Tk() 
root.title("Log in")

root.geometry("1920x1080")


conn = sqlite3.connect("User_Info.db")

# create cursor

c = conn.cursor()

'''
c.execute(""" CREATE TABLE Info(
Name text,
Username text,
Password text,
Email text )""")
'''

conn = sqlite3.connect("Information.db")

# create cursor

c = conn.cursor()
'''

c.execute(""" CREATE TABLE Misinfo(
Title text,
Des text,
YN text )""")

'''
conn.commit()
#close database
conn.close

pic = "Verification page.png"

#close database

Font_candl = Font(family = "Champagne & Limousines", size = 17)
Font_candl2 = Font(family = "Champagne & Limousines", size = 21)
Font_candl3 = Font(family = "Champagne & Limousines", size = 48)


my_image = ImageTk.PhotoImage(Image.open("Signup_Login.png"))

my_label = Label(root, image = my_image)

my_label.place(x=0, y=0, relwidth=1, relheight=1)

my_image1 = ImageTk.PhotoImage(Image.open("Home page.png"))

my_label1 = Label(root, image = my_image1)





btn_FAQ = ImageTk.PhotoImage(Image.open("FAQ.png"))
btn_FAQ_btn = Button(root, image = btn_FAQ)



def mispage():
      s = Toplevel(height = 1080, width = 1920)

      vbg_image = ImageTk.PhotoImage(Image.open("Verification page.png"))
      vbg = Label(s, image = vbg_image)
      vbg.place(x = 0, y = 0, relwidth=1, relheight=1 )

      def Sub():
            conn = sqlite3.connect("Information.db")
            c = conn.cursor()

            r = Title.get()

            y = des.get("1.0","end")

            c.execute("INSERT INTO Misinfo VALUES (:Name, :Des, :YN)",
            {
            'Name':Title.get(),
            'Des':des.get("1.0","end"),
            'YN':'' })
            

            
            
            conn.commit()
            conn.close

            

      
      Title = Entry(s, width = 40, font = Font_candl2, bg = "#F2EDED")


      Title_label = Label(s, text = "Title:", font = Font_candl2, bg = "#F8F1F1")


      des = Text ( s, height = 15, font = Font_candl, width = 70, bg = "#F2EDED")


      des_label = Label(s, text = "Description:", font = Font_candl2, bg = "#F8F1F1")


      EnterLabel = Label(s, text = "Enter the information that you want to check", font = Font_candl3, bg = "#F8F1F1")

      
      des.place(x = 405, y = 450)
      Title.place(x= 483, y =300)
      Title_label.place(x = 400, y = 300)
      des_label.place(x = 400, y = 400)
      EnterLabel.place(x = 300, y = 150)


      sub_btn = Button(s, text = "Submit", font = Font_candl2, command = Sub)
      sub_btn.place(x = 800, y = 700)

      
def mis1():
      r = Tk()
      r.title("Hello")
      r.geometry("1920x1080")

      
      


onl_con = ImageTk.PhotoImage(Image.open("Online consultation.png"))
onl_con_btn = Button(root, image = onl_con)

my_label = Label(root, image = my_image)

my_label.place(x=0, y=0, relwidth=1, relheight=1)

Choose = Label(root, text = "Choose where you want to go next: ", font = Font_candl3)

mis = ImageTk.PhotoImage(Image.open("Minform.png"))
mis_btn = Button(root, image = mis, command = mispage )

mis1 = ImageTk.PhotoImage(Image.open("Minform.png"))
mis_btn1 = Button(root, image = mis1, command = mis1 )

Font_pas = Font(family = "Password", size = 17)
Font_pas1 = Font(family = "Password", size = 21)

Username1 = Entry(root, width = 50, bg = "#F8F1F1", bd = 2, font = Font_candl )
Username1.place(x = 700, y = 500)

Username_label = Label(root, text = "Username:", font = Font_candl2)
Username_label.place(x = 500, y = 500)

Password1 = Entry(root, width = 50, bg = "#F8F1F1", bd = 2, font = Font_pas )
Password1.place(x = 700, y = 600)

Password1_label = Label(root, text = "Password:", font = Font_candl2)
Password1_label.place(x = 500, y = 600)

def Signup():

      Username1.destroy()
      Username_label.destroy()
      Username_label.destroy()
      Password1.destroy()
      Password1_label.destroy()
      Login_Btn.destroy()
      Signup_Btn1.destroy()
      

      Font_candl = Font(family = "Champagne & Limousines", size = 17)
      Font_candl2 = Font(family = "Champagne & Limousines", size = 21)

      Font_pas1 = Font(family = "Password", size = 21)


      Name = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = Font_candl)
      Name.place(x = 600, y = 500)

      Name_label = Label(root, text = "Enter your name:", font = Font_candl2)
      Name_label.place(x  = 400, y = 500)

      Username = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = Font_candl)
      Username.place(x = 600, y = 550)

      Username_label1 = Label(root, text = "Pick a Username:", font = Font_candl2)
      Username_label1.place(x = 400, y = 550)

      Password = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = Font_pas )
      Password.place(x = 600, y = 600)

      Password_label = Label(root, text = "Pick a Password:", font = Font_candl2)
      Password_label.place(x = 400, y = 600)

      Email = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = Font_candl )
      Email.place(x = 600, y = 650)

      Email_label = Label(root, text = "Enter your Email:", font = Font_candl2)
      Email_label.place(x = 400, y = 650)





      def Register():
        #Send email and error
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

        r = Email.get()
        print(r)
        smtp_object = smtplib.SMTP('smtp.gmail.com',587)
        smtp_object.ehlo()

        smtp_object.starttls()

        email = "glitch.advil4@gmail.com"

        password= "iqft tdcc nosl xjbr"

        smtp_object.login(email,password)

        from_adress = email
        to_adress = r

        def check(em):
            if(re.search(regex,em)):  
                print("Valid Email")  
                  
            else:  
                print("Invalid Email")
                messagebox.showwarning("Warning", "Invalid Email")

          

        if __name__ == '__main__' :
            check(r)


        subject = "Auxal"
        message = "Thank you for registering to our app, for future convenience we will send emails from this email \n Thank you, \n Team Glitch Advil"

        msg = "Subject: "+subject+'\n'+message

        smtp_object.sendmail(from_adress,to_adress,msg)

        conn = sqlite3.connect('User_Info.db')

        # create cursor

        c = conn.cursor()

        #insert into tabel
        c.execute("INSERT INTO Info VALUES (:Name, :Username, :Password, :Email )",
                    {
                        'Name':Name.get(),
                        'Username':Username.get(),
                        'Password':Password.get(),
                        'Email': Email.get() })

        c.execute("SELECT *, oid FROM Info")
        records = c.fetchall()
        print_record = ''       
        for record in records:
              print_record += str(record[0]) + " " + str(record[1])

              

            #commit changes
        conn.commit()
       #close database
        conn.close



        Username.delete(0, END)
        Password.delete(0, END)
        Email.delete(0, END)
        Name.delete(0, END)

      Signup_image= ImageTk.PhotoImage(Image.open("1.png"))
      Signup_Btn = Button(root, text = "Signup", command = Register, font = Font_candl2 )
      Signup_Btn.place(x = 700, y = 690)


      


def homepage():
      Username1.destroy()
      Username_label.destroy()
      Username_label.destroy()
      Password1.destroy()
      Password1_label.destroy()
      Login_Btn.destroy()
      Signup_Btn1.destroy()
      my_label.destroy()

      my_label1.place(x=0, y=0, relwidth=1, relheight=1)

      btn_FAQ_btn.place(x = 96, y = 700)

      onl_con_btn.place(x = 800, y = 600)

      mis_btn.place(x = 500, y = 600)

      
      Choose.place(x = 400, y = 300)


def homepagedoc():
      Username1.destroy()
      Username_label.destroy()
      Username_label.destroy()
      Password1.destroy()
      Password1_label.destroy()
      Login_Btn.destroy()
      Signup_Btn1.destroy()
      my_label.destroy()

      my_label1.place(x=0, y=0, relwidth=1, relheight=1)

      mis_btn1.place(x = 500, y = 600)

      
      
def Login():


    use = Username1.get()
    pas = Password1.get()
    
    conn = sqlite3.connect('User_Info.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM Info")
    records = c.fetchall()

    for record in records:
        m = 0
        print(record)
        print(use)
        m = 0
        if use == record[1]:
            r = record
            print("success")
            if pas == record[2]:
                  print("success")
                  homepage()
            else:
                print("Fail")
                messagebox.showerror("Error", "Wrong username or  password")
                break
                

        elif use == "1234" and pas == "1234":
              homepagedoc()
              

                
            
                        
        else:
            print("Fail")
            #messagebox.showerror("Error", "Please enter your username or  password")

         


        #commit changes
        conn.commit()

        #close database
        conn.close
        




# Buttons
Login_image= ImageTk.PhotoImage(Image.open("1.png"))
Login_Btn = Button(root, image = Login_image, command = Login)
Login_Btn.place(x = 450, y = 700)

Signup_image= ImageTk.PhotoImage(Image.open("2.png"))
Signup_Btn1 = Button(root, image = Signup_image, command = Signup)
Signup_Btn1.place(x = 850, y = 700)





root.mainloop()
