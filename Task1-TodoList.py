# Code for a GUI-based To-Do List application in Python

from tkinter import *

root = Tk()
root.title("To-Do List")

tasks = []

def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0, "end")

def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "Please enter a task."

def delete_task():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()

lbl_title = Label(root, text="To-Do List", bg="lightblue")
lbl_title.grid(row=0, column=0)

lbl_display = Label(root, text="", bg="lightblue")
lbl_display.grid(row=3, column=0)

txt_input = Entry(root, width=15)
txt_input.grid(row=1, column=0)

btn_add = Button(root, text="Add Task", fg="green", bg="lightblue", command=add_task)
btn_add.grid(row=1, column=1)

btn_delete = Button(root, text="Delete Task", fg="red", bg="lightblue", command=delete_task)
btn_delete.grid(row=1, column=2)

btn_clear = Button(root, text="Clear List", fg="blue", bg="lightblue", command=clear_listbox)
btn_clear.grid(row=2, column=1)

lb_tasks = Listbox(root, bg="lightyellow")
lb_tasks.grid(row=2, column=0, rowspan=1, columnspan=3)

root.mainloop()
