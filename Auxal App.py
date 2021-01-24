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
'''c.execute(""" CREATE TABLE Doc_info2(
name text,
spec text,
av_d text,
money text,
yof text,
link text,
lang text)""")'''
conn = sqlite3.connect("Information.db")

# create cursor

c = conn.cursor()

'''
c.execute(""" CREATE TABLE Misinfo2(
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

FAQ1 = ImageTk.PhotoImage(Image.open("FAQ.png"))


def FAQ():
      s = Toplevel(width = 1920, height = 1080, bg = "#f8f1f1")


      label = Label(s, image = FAQ1)
      label.place(x = 800, y = 10)
      
      label1 = Label(s, text = "Q. What does Auxsal mean?", font = ("Stark", 11)).place(x = 50, y = 60)
      label2 = Label(s, text = "A. Auxsal is short for Auxilium Salutis, which means Health Helpers in Latin.", font = ("Stark", 11)).place(x = 70, y = 80)
      label3 = Label(s, text = "Q. Who made this app?", font = ("Stark", 11)).place(x = 50, y = 110)
      label4 = Label(s, text = "A. Four ninth graders, Bhuvan Kasam, Preetam Byahatti, Krishna Kalathur, and Isha Matta, together known as Glitch Advil, have collaborated and brought to existence Auxsal!", font = ("Stark", 11)).place(x = 70, y = 130)
      label5 = Label(s, text = "Q. How can we trust this app?", font = ("Stark", 11)).place(x = 50, y = 160)
      label6 = Label(s, text = "A. All of the information provided is verified by trustworthy doctors.", font = ("Stark", 11)).place(x = 70, y = 180)
      label7 = Label(s, text = "Q. Are there any in-app purchases?", font = ("Stark", 11)).place(x = 50, y = 210)
      label8 = Label(s, text = "A. In Auxsal, there are no-app purchases, however, services provided by doctors will require you to pay.", font = ("Stark", 11)).place(x = 70, y = 230)
      label9 = Label(s, text = "Q. How are questions asked in the app answered?", font = ("Stark", 11)).place(x = 50, y = 260)
      label10 = Label(s, text = "A. Certified doctors receive the questions asked in the app and return their answers which are displayed on the home page. The question is passed on to a few doctors specializing in that certain field,", font = ("Stark", 11)).place(x = 70, y = 280)
      label11 = Label(s, text = "and the majority vote is considered correct.", font = ("Stark", 11)).place(x = 70, y = 300)
      label12 = Label(s, text = "Q. What is the price for online consultation?", font = ("Stark", 11)).place(x = 50, y = 325)
      label13 = Label(s, text = "A. The price varies according to the doctor and the requirements attended to. It’s like a regular visit to the doctor’s office, except for the fact that it’s online.", font = ("Stark", 11)).place(x = 70, y = 345)
      label14 = Label(s, text = "Q. How do we know that the answers we receive are the most reliable?", font = ("Stark", 11)).place(x = 50, y = 375)
      label15 = Label(s, text = "A. When at least 80% of the doctors the question has been sent to have replied with the same answer, that is considered to be the solution to whether the question is valid or not. So don’t ", font = ("Stark", 11)).place(x = 70, y = 395)
      label16 = Label(s, text = "worry! The answers are coming from the experts.", font = ("Stark", 11)).place(x = 70, y = 415)
      label17 = Label(s, text = "Q. How should we prepare for the online consultation?", font = ("Stark", 11)).place(x = 50, y = 440)
      label18 = Label(s, text = "A. Just come ready with a list of symptoms and if you’ve tried any remedies before, please tell us what they are and the degree to which they worked.", font = ("Stark", 11)).place(x = 70, y = 460)
      label19 = Label(s, text = "Q. What happens if the consultation doesn’t satisfy our concerns?", font = ("Stark", 11)).place(x = 50, y = 490)
      label20 = Label(s, text = "A. If you don’t feel your consultation with the doctor was completely up to the mark, you can always book another appointment with another doctor who might be of better help. However, a refund may not ", font = ("Stark", 11)).place(x = 70, y = 510)
      label21 = Label(s, text = "be possible as the doctors are very busy people with their own schedules that must be taken into account.", font = ("Stark", 11)).place(x = 70, y = 530)
      label22 = Label(s, text = "Q. How does the online consultation work?", font = ("Stark", 11)).place(x = 50, y = 555)
      label23 = Label(s, text = "A. Here’s the process to the entire online consultation: A search bar is given for you to input your specifications, for example your budget or the type of doctor you want to meet.", font = ("Stark", 11)).place(x = 70, y = 575)
      label24 = Label(s, text = "According to those specifications, a list of available doctors will be shown, from which you can choose from. Once you choose a doctor, an appointment will be confirmed, where you would", font = ("Stark", 11)).place(x = 70, y = 600)
      label25 = Label(s, text = "have a video call with that doctor to discuss with them.", font = ("Stark", 11)).place(x = 70, y = 625)





btn_FAQ = ImageTk.PhotoImage(Image.open("FAQ.png"))
btn_FAQ_btn = Button(root, image = btn_FAQ, command = FAQ)

def Forum():
      y = Toplevel(width = 1920, height = 1080, bg = "#f8f1f1")
      print("Clicked")
      conn = sqlite3.connect("Information.db")
      n = conn.cursor()
      n.execute(""" SELECT * , oid from Misinfo2 """)
      records1 = n.fetchall()

      print_ = ''

      on_off1 = ['on','off']

      print(on_off1[0])

      for record1 in records1:
            on_off1 = record1[2].split()
            
            if on_off1[0] == "on":
                  print(0)
                  print_ += str(record1[0]) + "\n" + str(record1[1]) + "\n"
            else:
                  continue

      label = Label(y, text = print_, font = Font_candl2  )
      label.place(x = 550, y = 200)
      print(print_)
      print( record1[2] , on_off1[0])
      conn.commit()
      conn.close

      
      y.mainloop()

forum = ImageTk.PhotoImage(Image.open("forum.png"))
btn_forum_btn = Button(root, image = forum, command = Forum)


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

            c.execute("INSERT INTO Misinfo2 VALUES (:Name, :Des, :YN)",
            {
            'Name':Title.get(),
            'Des':des.get("1.0","end"),
            'YN':'' })

            Title.delete(0, END)
            des.delete('1.0', 'end')

            
            
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

      
def misinfo():
      print("clicked!")
      r = Toplevel(height = 1080, width = 1920)

      bg = Label(r, image = my_image1)

      bg.place(x = 0, y =0 , relwidth=1, relheight=1 )

      conn = sqlite3.connect("Information.db")
      c = conn.cursor()


      c.execute(""" SELECT * , oid from Misinfo2 """)
      records = c.fetchall()
      xn = 100
      
      print_ = ''
      print(records)

      var = StringVar()
      var1 = StringVar()
      var2 = StringVar()
      var3 = StringVar()
      var4 = StringVar()
      var5 = StringVar()
      var6 = StringVar()
      var7 = StringVar()
      
      for record in records:
            print_+= "Title:                                                  " + "\t" + str(record[0]) +"\n" + "Description: " + "\t" + str(record[1]) + "\n" + "\n"
      c = Checkbutton(r, text = "If true check this box",variable = var, onvalue = "on", offvalue = "off")
      c1 = Checkbutton(r, text = "If true check this box",variable = var1, onvalue = "on", offvalue = "off")
      c2 = Checkbutton(r, text = "If true check this box",variable = var2, onvalue = "on", offvalue = "off")
      c3 = Checkbutton(r, text = "If true check this box",variable = var3, onvalue = "on", offvalue = "off")
      c4 = Checkbutton(r, text = "If true check this box",variable = var4, onvalue = "on", offvalue = "off")
      c5 = Checkbutton(r, text = "If true check this box",variable = var5, onvalue = "on", offvalue = "off")
      c6 = Checkbutton(r, text = "If true check this box",variable = var6, onvalue = "on", offvalue = "off")
      c7 = Checkbutton(r, text = "If true check this box",variable = var7, onvalue = "on", offvalue = "off")

      c.deselect()
      c1.deselect()
      c2.deselect()
      c3.deselect()
      c4.deselect()
      c5.deselect()
      c6.deselect()
      c7.deselect()

      c.place(x = 1300 , y = 100)
      c1.place(x = 1300 , y = 200 )
      c2.place(x = 1300, y = 300 )
      c3.place(x = 1300, y = 400)
      c4.place(x = 1300, y = 500 )
      c5.place(x = 1300 , y = 600)
      c6.place(x = 1300, y = 700)
      c7.place(x = 1300, y = 800)

      

      print(print_)
      
      label = Label(r, text = print_, font = Font_candl2, bg = "#F8F1F1")
      label.place(x =400, y = 100)
      print("Printed")
      conn.commit()
       #close database
      conn.close

      def Subm():
            cs = [var.get(), var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get()]
            print(cs[0])
            conn = sqlite3.connect("Information.db")
            x = conn.cursor()
            x.execute(""" SELECT * , oid from Misinfo2 """)
            records = x.fetchall()
            n = 1
            for record in records:
                  x.execute(""" UPDATE Misinfo2 SET

                  Title = :Title,
                  des = :des,
                  Yn = :Yn

                  WHERE oid = :oid """,
                  { 'Title' : record[0],
                  'des' : record[1],
                  'Yn': cs[n],
                    'oid': record[3]
                    }
                            )
                  print("Success")
                  n+= 1
                  c.deselect()
                  c1.deselect()
                  c2.deselect()
                  c3.deselect()
                  c4.deselect()
                  c5.deselect()
                  c6.deselect()
                  c7.deselect()

            conn.commit()
             #close database
            conn.close
      btn = Button(r, text = "Submit", font = Font_candl, command = Subm)
      btn.place(x = 700, y = 750)

      
      r.mainloop()

search1 = ImageTk.PhotoImage(Image.open("Search.png"))


bg_con = ImageTk.PhotoImage(Image.open("Online consultation page.png"))

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

      btn_forum_btn.place(x = 1000, y = 600)

      onl_con_btn.place(x = 700, y = 600, )

      mis_btn.place(x = 400, y = 600)
            
      Choose.place(x = 400, y = 300)



def con():
      o = Toplevel(width = 1920, height = 1080)
      bg_con_label = Label(o, image = bg_con)
      bg_con_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

      e = Entry(o, width = 50, font = Font_candl2)
      e.place(x = 350, y = 150)
      
      def search():

            c.execute("SELECT *, oid FROM Doc_info2")
            print_ = ''
            records = c.fetchall()
            for y in records:
                  r = e.get()

                  if (r) == (y[0]) or (r) == (y[1]) or (r) == (y[2]) or (r) == (y[3]) or (r) == (y[4]) or (r) == (y[5])or (r) == (y[6]) or (r) == (y[7]):
                        print_ = y[0] + '\n' + y[1] + '\n'+ y [2] + '\n' + y[3] + '\n' + y[4] + '\n'+ y [5] + '\n' + y[6]
            label = Label(o, text = print_, font = Font_candl2, bg ="#f8f1f1")
            label.place(x = 750, y = 400)
            e.delete(0, END)

      search_button = Button(o, image = search1, command = search)
      search_button.place(x = 550, y = 200)



      conn = sqlite3.connect("User_Info.db")

      # create cursor

      c = conn.cursor()


      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Rajeev Manmohan",
            'spec': "Psychology" ,
            'av_d':"9pm to 10pm",
            'money': "5,000",
            'yof': "12",
            'link':"meet.google.com/smb-jtij-tdi",
            'lang':"Hindi, English"})

      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Raj Malhotra",
            'spec': "E.N.T" ,
            'av_d':"9am to 10am",
            'money': "2,000",
            'yof': "10",
            'link':"meet.google.com/xxd-daas-qcq",
            'lang':"Bhojpuri, English"})
      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Rajesh Koothrapalli",
            'spec': "E.N.T" ,
            'av_d':"9am to 10am",
            'money': "1,500",
            'yof': "5",
            'link':"meet.google.com/xxd-daas-qcq",
            'lang':"Marathi, English"})

      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Rajeev Manmohan",
            'spec': "Psychology" ,
            'av_d':"9pm to 10pm",
            'money': "5,000",
            'yof': "12",
            'link':"meet.google.com/smb-jtij-tdi",
            'lang':"Hindi, English"})

      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Raj Malhotra",
            'spec': "gastroenterologist" ,
            'av_d':"9am to 10am",
            'money': "2,000",
            'yof': "10",
            'link':"meet.google.com/xxd-daas-qcq",
            'lang':"Bhojpuri, English"})
      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Tarak Mehta",
            'spec': "Pediatrician" ,
            'av_d':"3:00 PM to 5:00 PM",
            'money': "3,500",
            'yof': "9",
            'link':"meet.google.com/ckj-extb-fdc",
            'lang':"Marathi, English"})
      c.execute("INSERT INTO Doc_info2 VALUES (:Name, :spec, :av_d , :money, :yof,:link, :lang  )",
        {
            'Name':"Tarak Mehta",
            'spec': "Pediatrician" ,
            'av_d':"3:00 PM to 5:00 PM",
            'money': "3,500",
            'yof': "9",
            'link':"meet.google.com/ckj-extb-fdc",
            'lang':"Marathi, English"})

      




       
            
      
      conn.commit()

      conn.close
      
      o.mainloop()      

      

onl_con = ImageTk.PhotoImage(Image.open("Online consultation.png"))
onl_con_btn = Button(root, image = onl_con, command = con)

my_label = Label(root, image = my_image)

my_label.place(x=0, y=0, relwidth=1, relheight=1)

Choose = Label(root, text = "Choose where you want to go next: ", font = Font_candl3)

mis = ImageTk.PhotoImage(Image.open("Minform.png"))
mis_btn = Button(root, image = mis, command = mispage )

mis1 = ImageTk.PhotoImage(Image.open("Minform.png"))
mis_btn1 = Button(root, image = mis1, command = misinfo )

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

      def home():
            Username.destroy()
            Username_label1.destroy()
            Password.destroy()
            Password_label.destroy()
            Email.destroy()
            Email_label.destroy()
            home_btn.destroy()
            Name.destroy()
            Name_label.destroy()
            Signup_Btn.destroy()

            Username1 = Entry(root, width = 50, bg = "#F8F1F1", bd = 2, font = Font_candl )
            Username1.place(x = 700, y = 500)

            Username_label = Label(root, text = "Username:", font = Font_candl2)
            Username_label.place(x = 500, y = 500)

            Password1 = Entry(root, width = 50, bg = "#F8F1F1", bd = 2, font = Font_pas )
            Password1.place(x = 700, y = 600)

            Password1_label = Label(root, text = "Password:", font = Font_candl2)
            Password1_label.place(x = 500, y = 600)
            
            Login_image= ImageTk.PhotoImage(Image.open("1.png"))
            Login_Btn = Button(root, image = Login_image, command = Login)
            Login_Btn.place(x = 450, y = 700)

            Login()


            


      home_btn = Button(root , text = "Go to Login Page", font = Font_candl2, command = home)
      home_btn.place(x = 100, y = 0)





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
