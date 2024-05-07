import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sql

tasks = []

def addTasks():
    taskData = taskField.get()
    if len(taskData) == 0:
        messagebox.showinfo("Error", "Field is Empty")
    else:
        tasks.append(taskData)
        listUpdate()
        taskField.delete(0, 'end')

def listUpdate():
    taskListBox.delete(0, 'end')
    for task in tasks:
        taskListBox.insert('end', task)

def deleteTask():
    try:
        selectedTaskIndex = taskListBox.curselection()[0]
        taskListBox.delete(selectedTaskIndex)
        tasks.pop(selectedTaskIndex)
    except IndexError:
        messagebox.showinfo("Error", "No tasks Selected. Cannot Delete.")

def deleteAllTasks():
    messageBox = messagebox.askyesno("Delete All", "Are you sure?")
    if messageBox == tk.YES:
        taskListBox.delete(0, 'end')
        tasks.clear()

def close():
    print(tasks)
    window.destroy()


window = tk.Tk()
window.title("To-Do List")
window.geometry("600x500")
window.resizable(0, 0)
window.configure(bg = "#bf9278")

headerFrame = tk.Frame(window, bg = "#bf9278")
functionsFrame = tk.Frame(window, bg = "#bf9278")
listboxFrame = tk.Frame(window, bg = "#bf9278")

headerFrame.pack(fill = "both")
functionsFrame.pack(side = "left", expand = True, fill = "both")
listboxFrame.pack(side = "right", expand = True, fill = "both")

headerLabel = ttk.Label(headerFrame, text = "Your To-Do List", font = ("Pristina", 40, "bold"), background =  "#bf9278", foreground = "#fff")
headerLabel.pack(padx = 20, pady = 10)

taskLabel = ttk.Label(functionsFrame, text = "Enter the Task : ", font=("Baskerville Old Face", 15), background="#bf9278", foreground="#000000")
taskLabel.place(x = 30, y = 40)

taskField = ttk.Entry(functionsFrame, font=("Baskerville Old Face", 15), width = 18, background="#bf9278", foreground="#bf9278")
taskField.place(x = 30, y = 80)

addButton = ttk.Button(functionsFrame, text = "Add Task", width = 24, command = addTasks, style = "TButton")
delButton = ttk.Button(functionsFrame, text = "Delete Task", width = 24, command = deleteTask, style = "TButton")
delAllButton = ttk.Button(functionsFrame, text = "Delete All Tasks", width = 24, command = deleteAllTasks, style = "TButton")
exitButton = ttk.Button(functionsFrame, text = "Exit", width = 24, command = close, style = "TButton")

addButton.place(x = 40, y = 120)
delButton.place(x = 40, y = 160)
delAllButton.place(x = 40, y = 200)
exitButton.place(x = 40, y = 240)

style = ttk.Style()
style.configure("TListbox", background = "FFF", foreground = "#000", selectbackground = "#cce072", selectforeground="#FFFFFF")

taskListBox = tk.Listbox(listboxFrame, width = 26, height = 13, selectmode = 'SINGLE', background = "#FFFFFF", foreground = "#000000", selectbackground = "#cce072", selectforeground = "#000", font = ("Baskerville Old Face", 14))
taskListBox.place(x = 10, y = 20)

window.mainloop()
