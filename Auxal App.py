from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import sqlite3

root = Tk()
root.title("Auxal")
root.geometry("1920x1080")

conn = sqlite3.connect("Signup_details.db")

c = conn.cursor()



conn.commit()
conn.close()

bg_login = ImageTk.PhotoImage(Image.open("Signup_Login"))
bg_login_label = Label(root, image = bg_login)
bg_login_label.place(x=0, y=0, relwidth=1, relheight=1)

font_stark = Font(family = "Stark", size = 12)
font_stark2 = Font(family = "Stark", size = 15)
# Login Page
U_E = Entry(root, width = 30, font = font_stark, bg = "#F8F1F1")
U_E.place(x = 750, y = 300)

P_E = Entry(root, width = 30, font = font_stark, bg = "#F8F1F1")
P_E.place(x = 750, y = 400)   

login_btn = Button(root, text = "Login", font = font_stark2)
login_btn.place(x = 600, y= 700 )



root.mainloop()
