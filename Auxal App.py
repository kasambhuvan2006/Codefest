from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import re
import smtplib
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Auxal")
root.geometry("1920x1080")

conn = sqlite3.connect("Signup_details.db")

c = conn.cursor()

'''c.execute(""" CREATE TABLE Info(
Name text,
Username text,
Password text,
Email text )""")'''
conn.commit()


conn.close()

Background_image = ImageTk.PhotoImage(Image.open("Signup_Login.png"))
my_label = Label(root, image = Background_image)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
Font_candl = Font(family = "Champagne & Limousines", size = 21)

font_stark = Font(family = "Stark", size = 16)




# Login Page
U_E = Entry(root, width = 30, font = font_stark, bg = "#F8F1F1")
U_E.place(x = 650, y = 500)

U_E_Label = Label(root, text = "Username:", font = Font_candl)
U_E_Label.place(x = 470, y = 500)

P_E = Entry(root, width = 30, font = font_stark, bg = "#F8F1F1")
P_E.place(x = 650, y = 600)   

P_E_Label = Label(root, text = "Password:", font = Font_candl)
P_E_Label.place(x = 475, y = 600)

login_image = ImageTk.PhotoImage(Image.open("1.png"))
login_btn = Button(root, image = login_image)
login_btn.place(x = 500, y= 700)



logind_image = ImageTk.PhotoImage(Image.open("3.png"))
logind_btn = Button(root, image = logind_image)
logind_btn.place(x = 1200, y= 700)

signupd_image = ImageTk.PhotoImage(Image.open("4.png"))
signupd_btn = Button(root, image = signupd_image)
signupd_btn.place(x = 100, y= 700)

def register():
      U_E.destroy()
      U_E_Label.destroy()
      P_E.destroy()
      P_E_Label.destroy()
      login_btn.destroy()
      logind_btn.destroy()
      signupd_btn.destroy()
      signup_btn.destroy()


      Name = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = font_stark)
      Name.place(x = 600, y = 500)

      Name_label = Label(root, text = "Enter your name:", font = Font_candl)
      Name_label.place(x  = 400, y = 500)

      Username = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = font_stark )
      Username.place(x = 600, y = 550)

      Username_label = Label(root, text = "Pick a Username:", font = Font_candl)
      Username_label.place(x = 400, y = 550)

      Password = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = font_stark)
      Password.place(x = 600, y = 600)

      Password_label = Label(root, text = "Pick a Password:", font = Font_candl)
      Password_label.place(x = 400, y = 600)

      Email = Entry(root, width = 35, bg = "#F8F1F1", bd = 2, font = font_stark)
      Email.place(x = 600, y = 650)

      Email_label = Label(root, text = "Enter your Email:", font = Font_candl)
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

        conn = sqlite3.connect('User_Info')

        # create cursor

        c = conn.cursor()

        #insert into tabel
        c.execute("INSERT INTO Info VALUES (:Name, :Username, :Password, :Email )",
                    {
                        'Name':Name.get(),
                        'Username':Username.get(),
                        'Password':Password.get(),
                        'Email': Email.get()


                        })
      signup_image1 = ImageTk.PhotoImage(Image.open("2.png"))
      signup_btn2 = Button(root, image = signup_image, command = Register)
      signup_btn2.place(x = 700, y= 700)


      

signup_image = ImageTk.PhotoImage(Image.open("2.png"))
signup_btn = Button(root, image = signup_image, command = register)
signup_btn.place(x = 900, y= 700)


root.mainloop()
