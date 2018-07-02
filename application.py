from tkinter import *
import sqlite_backend

def view_command():
    list1.delete(0,END)
    for row in sqlite_backend.view():
        list1.insert(END,row)
        

def search_command():
    list1.delete(0,END)
    for row in sqlite_backend.search(Title_text.get(),Author_text.get(),Year_text.get(),Isbn_text.get()):
        list1.insert(END,row)

def add_command():
    list1.delete(0,END)
    row = Title_text.get(),Author_text.get(),Year_text.get(),Isbn_text.get()
    sqlite_backend.insert(Title_text.get(),Author_text.get(),Year_text.get(),Isbn_text.get())
    list1.insert(END,(Title_text.get(),Author_text.get(),Year_text.get(),Isbn_text.get()))
    
def get_selected_row(event):
    global selected_row
    index=list1.curselection()[0]
    selected_row=list1.get(index)
    t1.delete(0,END)
    t1.insert(END,selected_row[1])
    t2.delete(0,END)
    t2.insert(END,selected_row[2])
    t3.delete(0,END)
    t3.insert(END,selected_row[3])
    t4.delete(0,END)
    t4.insert(END,selected_row[4])

def delete_command():
    sqlite_backend.delete(selected_row[0])

def update_command():
    sqlite_backend.update(selected_row[0],t1.get(),t2.get(),t3.get(),t4.get())

window = Tk()
window.wm_title("BookStore")

l1=Label(window,text="Title")
l1.grid(row=0,column=0)

l2=Label(window,text="Author")
l2.grid(row=0,column=2)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)

Title_text = StringVar()
t1 = Entry(window,textvariable=Title_text)
t1.grid(row=0,column=1)

Author_text = StringVar()
t2 = Entry(window,textvariable=Author_text)
t2.grid(row=0,column=3)

Year_text = StringVar()
t3 = Entry(window,textvariable=Year_text)
t3.grid(row=1,column=1)

Isbn_text = StringVar()
t4 = Entry(window,textvariable=Isbn_text)
t4.grid(row=1,column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text="Search Entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text="Add Entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text="Update",width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6=Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()
