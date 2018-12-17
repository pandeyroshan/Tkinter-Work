from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
def mainWindow():
	root.destroy()
	n=Tk()
	def exit():
		n.destroy()
	def resetData():
		e1.delete(0,END)
		e2.delete(0,END)
	def addData():
		amount=e1.get()
		note=e2.get()
		con=sqlite3.Connection('mysqlite')
		cur=con.cursor()
		if amount:
			if note:
				cur.execute("create table if not exists extra(amount varchar(30),note varchar(30))")
				sqlText="insert into extra values('"+amount+"','"+note+"')"
				cur.execute(sqlText)
				messagebox.showerror("STATUS", "Expenses Added.")
				e1.delete(0,END)
				e2.delete(0,END)
				con.commit()
			else:
				messagebox.showerror("STATUS", "Enter Note.")
		else:
			messagebox.showerror("STATUS", "Enter Amount.")
	def showAll():
		def resetTable():
			con=sqlite3.Connection('mysqlite')
			cur=con.cursor()
			cur.execute("delete from extra")
			messagebox.showerror("STATUS", "Expences Reset, SAVE MONEY")
			lastRoot.destroy()
			con.commit()
		con=sqlite3.Connection('mysqlite')
		cur=con.cursor()
		cur.execute("select * from extra")
		a=cur.fetchall()
		lastRoot=Tk()
		lastRoot.configure(background='#222022')
		Label(lastRoot,text="HISTORY",bg='#222022',fg='#1ed2f4',font='Arial 20 bold',width=50).grid(row=0,column=0,columnspan=2)
		Label(lastRoot,text='',bg='#222022').grid(row=1,column=0)
		Label(lastRoot,text='NOTE',bg='#222022',fg='#FF5620',font='Arial 15',width=25).grid(row=2,column=0)
		Label(lastRoot,text='AMOUNT',bg='#222022',fg='#FF5620',font='Arial 15',width=25).grid(row=2,column=1)
		Label(lastRoot,text='',bg='#222022').grid(row=3,column=0)
		j=4
		i=0
		total=0
		for data in a:
			m=a[i][0]
			n=a[i][1]
			total+=int(m)
			Label(lastRoot,text=n,font='Arial 12',bg='#222022',fg='#ffffff').grid(row=j,column=0)
			Label(lastRoot,text=m,font='Arial 12',bg='#222022',fg='#ffffff').grid(row=j,column=1)
			j+=1
			i+=1
		Label(lastRoot,text='',bg='#222022').grid(row=j,column=0)
		Label(lastRoot,text='TOTAL',font='Arial 15',bg='#222022',fg='#FF5620').grid(row=j+1,column=0)
		Label(lastRoot,text=total,font='Arial 15',bg='#222022',fg='#FF5620').grid(row=j+1,column=1)
		Label(lastRoot,text='',bg='#222022').grid(row=j+2,column=0)
		Button(lastRoot,text='RESET',bg='#1ed2f4',width=15,font='Arial 10 bold',command=resetTable).grid(row=j+3,column=1,ipady=4)
		Label(lastRoot,text='',bg='#222022').grid(row=j+4,column=0)
		lastRoot.mainloop()
	n.configure(background='#222022')
	Label(n,text="MANAGE MONEY",bg='#222022',fg='#1ed2f4',font='Arial 20 bold',width=50).grid(row=0,column=0,columnspan=2)
	Label(n,text='',bg='#222022').grid(row=1,column=0)
	Label(n,text="AMOUNT",bg='#222022',fg='#ffffff',font='Arial 15').grid(row=2,column=0)
	e1=Entry(n,font='Arial 15',bg='#222022',fg='#ffffff')
	e1.grid(row=2,column=1,ipady=2)

	Label(n,text='',bg='#222022').grid(row=3,column=0)
	Label(n,text="NOTE",bg='#222022',fg='#ffffff',font='Arial 15').grid(row=4,column=0)
	e2=Entry(n,font='Arial 15',bg='#222022',fg='#ffffff')
	e2.grid(row=4,column=1,ipady=2)
	Label(n,text='',bg='#222022').grid(row=5,column=0)

	Button(n,text='RESET',bg='#1ed2f4',width=20,font='Arial 10 bold',command=resetData).grid(row=6,column=0,ipady=4)
	Button(n,text='ADD',bg='#1ed2f4',width=20,font='Arial 10 bold',command=addData).grid(row=6,column=1,ipady=4)
	Label(n,text='',bg='#222022').grid(row=7,column=0)
	Button(n,text='SHOW',bg='#1ed2f4',width=20,font='Arial 10 bold',command=showAll).grid(row=8,column=0,ipady=4)
	Button(n,text='EXIT',bg='#1ed2f4',width=20,font='Arial 10 bold',command=exit).grid(row=8,column=1,ipady=4)
	Label(n,text='',bg='#222022').grid(row=9,column=0)

	n.mainloop()
def resetData():
	e1.delete(0,END)
	e2.delete(0,END)
def loginUser():
	uname=e1.get()
	pwd=e2.get()
	if uname:
		if pwd:
			if uname  == 'roshan172':
				if pwd == 'unstructure_data':
					mainWindow()
				else:
					messagebox.showerror("STATUS", "Wrong Password.")
			else:
				messagebox.showerror("STATUS", "Wrong Username")
		else:
			messagebox.showerror("STATUS", "Enter Password")
	else:
		messagebox.showerror("STATUS", "Enter Username")
root.configure(background='#222022')
Label(root,text="MONTHLY MONEY EXPENSES RECORDS",bg='#222022',fg='#1ed2f4',font='Arial 20 bold',width=50).grid(row=0,column=0,columnspan=2)
Label(root,text='',bg='#222022').grid(row=1,column=0)
Label(root,text='USERNAME',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=2,column=0)
e1=Entry(root,font='Arial 15',bg='#222022',fg='#ffffff')
e1.grid(row=2,column=1,ipady=2)
Label(root,text='',bg='#222022').grid(row=3,column=0)
Label(root,text='PASSWORD',font='Arial 15',bg='#222022',fg='#ffffff').grid(row=4,column=0)
e2=Entry(root,font='Arial 15',bg='#222022',fg='#ffffff',show='*')
e2.grid(row=4,column=1,ipady=2)
Label(root,text='',bg='#222022').grid(row=5,column=0)
Button(root,text='RESET',bg='#1ed2f4',width=15,font='Arial 10 bold',command=resetData).grid(row=6,column=0,ipady=4)
Button(root,text='LOGIN',bg='#1ed2f4',width=15,font='Arial 10 bold',command=loginUser).grid(row=6,column=1,ipady=4)
Label(root,text='',bg='#222022').grid(row=7,column=0)

root.mainloop()