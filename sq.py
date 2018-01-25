import sqlite3

conn = sqlite3.connect('as.db')
c = conn.cursor()
#c.execute(" CREATE  TABLE student2(tk text)")


#print c.fetchmany(1)


import Tkinter 
import random

from Tkinter import Tk, RIGHT, BOTH, RAISED


root = Tkinter.Tk()

root.title("A.A.N.M & V.V.R.S.R Polytechnic")

root.geometry("800x800")
root.configure(background='DARKCYAN')



t = []

#functions

def update_listbox():
        c.execute("SELECT * FROM student2")
        t = c.fetchall()
	#Clear the current list
        clear_listbox()
        for task in t:
                lb_tasks.insert("end", task)

def clear_listbox():
	lb_tasks.delete(0, "end")

def add_task():
	#Get the task to add
	task = txt_input.get()
	print task
	c.execute("INSERT INTO student2(tk) VALUES(?)", (task,))
	conn.commit()
	c.execute("SELECT * FROM student2")
	print c.fetchall()
                  
	#Make sure the task is not empty
	if task !="":
		#Append to the list
		t.append(task)
		#Update the listbox
		update_listbox()
	else:
		lbl_display["text"] = "Please enter a task."
	txt_input.delete(0, "end")
		
def del_all():
	#Since we are changing the list, it needs to be global.
	global t
	#Clear the tasks list
	t = c.execute(" DELETE FROM student2")
	conn.commit()
	t = []
	
	#Update the listbox
	update_listbox()
	

def del_one():
	#Get the text of the currently selected item
	task = lb_tasks.get("active")
	c.execute(" DELETE FROM student2 WHERE tk = ?", (task[0],))
	conn.commit()
	print t	

	#Confirm it is in the list
	if task in t:
		t.remove(task)
	#print type(task)
	#print task[0];
	
	#Update the listbox
	update_listbox()

def choose_random():
	#Choose a random task
	task = random.choice(t)
	#Update the display label
	lbl_display["text"]=task

def show_number_of_tasks():
        #Get the numbers of tasks
	number_of_tasks = len(t)
	#Create and format the message
	msg = "Number of tasks: %s" %number_of_tasks
	#Display the message
	lbl_display["text"]=msg


lbl_title = Tkinter.Label(root, text="To -Do -List", fg="YELLOW", bg="darkcyan", font = "Times")
lbl_title.pack()

lbl_display = Tkinter.Label(root, text="Enter Your Task Here:", bg="darkcyan")
lbl_display.pack()

                          
txt_input = Tkinter.Entry(root, width=90, fg="darkblue")
txt_input.pack()

btn_add_task = Tkinter.Button(root, text="Add task", fg="white", bg="darkblue", command=add_task)
btn_add_task.pack(padx=50, pady=10)

btn_del_all = Tkinter.Button(root, text="Delete All", fg="white", bg="darkred", command=del_all)
btn_del_all.pack(padx=50, pady=10)

btn_del_one = Tkinter.Button(root, text="Delete One", fg="white", bg="purple", command=del_one)
btn_del_one.pack(padx=50, pady=10)



btn_choose_random = Tkinter.Button(root, text="Choose Random", fg="darkblue", bg="green", command=choose_random)
btn_choose_random.pack(padx=50, pady=10)

btn_number_of_tasks = Tkinter.Button(root, text="Number of Tasks", fg="white", bg="brown", command=show_number_of_tasks)
btn_number_of_tasks.pack(padx=50, pady=10)

btn_exit = Tkinter.Button(root, text="Exit", fg="black", bg="yellow", width=8, command=exit)
btn_exit.pack(padx=50, pady=10)

lb_tasks = Tkinter.Listbox(root, width=90, fg="darkblue")
lb_tasks.pack()

c.execute("SELECT * FROM student2")
t = c.fetchall()
for task in t:
    lb_tasks.insert("end", task)


#Start the main events loop
root.mainloop()


