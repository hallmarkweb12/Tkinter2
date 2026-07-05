from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window = Tk()
window.title("Picture Album")
window.geometry('400x420')
title = Label(window,text="My Photo Album",fg="white",bg="purple")
title.pack(pady=10)
img_file = Image.open('Logo.jpg')
img_file = img_file.resize((300,100))
photo = ImageTk.PhotoImage(img_file)
pic = Label(window,image=photo)
pic.pack(pady=5)
def showmessage():
    messagebox.showinfo("Great","You clicked the button.")
msgbtn= Button(window,text='Click to React',bg='blue',fg='white',command=showmessage)
msgbtn.pack(pady=5)

def showdetails():
    top = Toplevel()
    top.title("Photo Details")
    top.geometry("200x120")
    info=Label(top,text="Taken on 1st June 2025")
    info.pack(pady=10)
    place=Label(top,text="Football Pitch")
    place.pack()
    place.mainloop()
detailsbtn = Button(window,text='See Details',bg='green',fg='white',command=showdetails) 
detailsbtn.pack(pady=10)
window.mainloop()    