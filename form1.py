# login page with tkinter with grid 

from tkinter import *
t = Tk()
def storedata():
    print("user name is : ",uservar.get())
    print("password is : ",passvar.get())
t.geometry("400x300")
t.title("this is user taking form ") # you can change the title of the form
user = Label(t, text= "User Name : ").grid(row=0,column=0)
password=Label(t, text="Password : ").grid(row=1,column=0)
# declare the initalize the variabel
uservar= StringVar()
passvar=StringVar()
userenter=Entry(t,textvariable=uservar).grid(row=0,column=1)
passentry=Entry(t,textvariable=passvar).grid(row=1,column=1)

button = Button(t,text="Submit",bg="green", command=storedata).grid()


t.mainloop()
