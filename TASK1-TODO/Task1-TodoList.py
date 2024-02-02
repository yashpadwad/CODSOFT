# Code for a GUI-based To-Do List application in Python

from tkinter import *

root = Tk()
root.title("To-Do List")
root.configure(bg="black")

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

def clear_all_tasks():
    tasks.clear()
    update_listbox()

lbl_title = Label(root, text="To-Do List", bg="#99FF99", font=("Open Sans", 20))
lbl_title.grid(row=0, column=0, columnspan=3, pady=10, sticky='n')

lbl_display = Label(root, text="", bg="lightblue", font=("Open Sans", 12))
lbl_display.grid(row=3, column=0, columnspan=3, pady=10, sticky='n')

txt_input = Entry(root, width=15, font=("Open Sans", 14))
txt_input.grid(row=1, column=0, padx=5, pady=10, sticky='we')

btn_add = Button(root, text="Add Task", fg="black", bg="yellow", font=("Open Sans", 12, "bold"), command=add_task)
btn_add.grid(row=1, column=1, pady=10, padx=5, sticky='we')

btn_delete = Button(root, text="Delete Task", fg="black", bg="yellow", font=("Open Sans", 12, "bold"), command=delete_task)
btn_delete.grid(row=1, column=2, pady=10, padx=5, sticky='we')

btn_clear = Button(root, text="Clear List", fg="black", bg="yellow", font=("Open Sans", 12, "bold"), command=clear_listbox)
btn_clear.grid(row=2, column=1, pady=10, padx=5, sticky='we')

btn_clear_all = Button(root, text="Clear All Tasks", fg="white", bg="brown", font=("Open Sans", 12, "bold"), command=clear_all_tasks)
btn_clear_all.grid(row=4, column=0, columnspan=3, pady=10, sticky='we')

lb_tasks = Listbox(root, bg="lightyellow", font=("Open Sans", 12))
lb_tasks.grid(row=2, column=0, rowspan=1, columnspan=3, pady=10, sticky='we')

root.geometry("600x500")
root.mainloop()