from tkinter import *
from tkinter import messagebox

def newTask():
    task=my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("Please enter some task")
def deleteTask():
    lb.delete(ANCHOR)
    
root=Tk()
root.geometry("500x500")
root.title("To-do List")
root.config(bg="#720B98")

root.resizable(width=False,height=False)

frame=Frame(root)
frame.pack(pady=10)
lb=Listbox(
    frame,
    width=25,
    height=8,
    font=("Times",20),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#00008B',
    activestyle="none",
    )
lb.pack(side=LEFT, fill=BOTH) 
task_list=[
    'Drink water',
    'Walking',
    'Read book for 15 mins',
    'Eat fruits',
    'Do yoga'
    ]
for item in task_list:
    lb.insert(END,item)
sb=Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry=Entry(
    root,
    font=("Arial",26)
    )
my_entry.pack(pady=20)
button_frame=Frame(root)
button_frame.pack(pady=20)

addTask_btn=Button(
    button_frame,
    text="Add Task",
    font=("Arial 16"),
    bg="#87CEEB",
    padx=20,
    pady=10,
    command=newTask
    )
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

delTask_btn=Button(
    button_frame,
    text="Delete Task",
    font=("Arial 16"),
    bg="#FFC0CB",
    padx=20,
    pady=10,
    command=deleteTask
    )
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)   
root.mainloop()