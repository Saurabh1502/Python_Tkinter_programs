# check box in tkinter

from tkinter import *
t=Tk()
t.geometry("700x300")
t.title("checkbox in Tkinter")
def alldata():
    print("name is :",name_var.get())
    print("last name is : ",last_name_var.get())
    print("location is : ",location_var.get())
    print("your age is : ",age_var.get())
    print("you mentioned your drean is : ",dream_var.get())

# this is label section 
heading=Label(t,text="Welcome to the online servay",font=" comicsansms 13 bold",pady=10).grid(row=0,column=1)
name=Label(t,text="First Name : ").grid(row=1,column=0)
last_name=Label(t, text="Last Name :").grid(row=2,column=0)
location=Label(t,text="Location : ").grid(row=3,column=0)
age=Label(t,text="Age : ").grid(row=4,column=0)
dream=Label(t,text="Write your Dream : ").grid(row=5,column=0)
# this is checkbox
checkbox = IntVar()
check=Checkbutton(t,text="I am Declaring all the information are correct ", variable= checkbox).grid(row=6,column=1)

#defining the data type of variable
name_var = StringVar()
last_name_var= StringVar()
location_var= StringVar()
age_var= IntVar()
dream_var= StringVar()

# creating text box

name_text=Entry(t,textvariable=name_var).grid(row=1,column=1)
last_text=Entry(t, textvariable = last_name_var).grid(row=2,column=1)
location_text=Entry(t,textvariable=location_var).grid(row=3,column=1)
age_text=Entry(t,textvariable=age_var).grid(row=4,column=1)
dream_text=Entry(t,textvariable=dream_var).grid(row=5,column=1)


# submit button
submit=Button(t,text="Submit", bg="lightgreen", command=alldata).grid(row=7,column=0)

t.mainloop()
