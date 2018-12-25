from tkinter import *
import sqlite3
from tkinter import messagebox
root=Tk()
def registerRoot():
	def resetRegister():
		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
	def isEmpty(text):
		if not text:
			return 0
		else:
			return 1
	def submit():
		name=e1.get()
		uname=e2.get()
		pwd=e3.get()
		cpwd=e4.get()
		if isEmpty(name):
			if isEmpty(uname):
				if isEmpty(pwd):
					if isEmpty(cpwd):
						if pwd==cpwd:
							try:
								con=sqlite3.Connection('logReg')
								cur=con.cursor()
								try:
									cur.execute("create table if not exists user(name varchar(20),uname varchar(20) primary key,pwd varchar(20))")
									#cur.execute("delete from user")   #Discomment it to drop the table
									sqlText="insert into user values('"+name+"','"+uname+"','"+pwd+"')"
									cur.execute(sqlText)
									registerRoot.destroy()
									messagebox.showinfo("STATUS", "Successfully Registered, login to continue.")
								except:
									messagebox.showinfo("STATUS", "Try with a different username.")
							except:
								messagebox.showinfo("STATUS", "Something went wrong.")
							finally:
								con.commit()
						else:
							messagebox.showinfo("STATUS", "Password Dismatched")
					else:
						messagebox.showinfo("STATUS", "Confirm Password Required")
				else:
					messagebox.showinfo("STATUS", "Password Required")
			else:
				messagebox.showinfo("STATUS", "Username Required")
		else:
			messagebox.showinfo("STATUS", "Name Required.")
	registerRoot=Tk()
	registerRoot.configure(background='#222022')
	Label(registerRoot,text='REGISTER',width=30,font='Arial 20 bold',bg='#222022',fg='#ffffff').grid(row=0,column=0,columnspan=2)
	Label(registerRoot,text='',bg='#222022').grid(row=1,column=0)
	Label(registerRoot,text='',bg='#222022').grid(row=2,column=0)

	Label(registerRoot,text='NAME:',bg='#222022',fg='#1ed2f4',font='Arial 10').grid(row=3,column=0)
	e1=Entry(registerRoot,font='Arial 10')
	e1.grid(row=3,column=1)
	Label(registerRoot,text='',bg='#222022').grid(row=4,column=0)

	Label(registerRoot,text='USERNAME:',bg='#222022',fg='#1ed2f4',font='Arial 10').grid(row=5,column=0)
	e2=Entry(registerRoot,font='Arial 10')
	e2.grid(row=5,column=1)
	Label(registerRoot,text='',bg='#222022').grid(row=6,column=0)

	Label(registerRoot,text='PASSWORD:',bg='#222022',fg='#1ed2f4',font='Arial 10').grid(row=7,column=0)
	e3=Entry(registerRoot,font='Arial 10',show="*")
	e3.grid(row=7,column=1)
	Label(registerRoot,text='',bg='#222022').grid(row=8,column=0)

	Label(registerRoot,text='CONFIRM PASSWORD:',bg='#222022',fg='#1ed2f4',font='Arial 10').grid(row=9,column=0)
	e4=Entry(registerRoot,font='Arial 10',show="*")
	e4.grid(row=9,column=1)
	Label(registerRoot,text='',bg='#222022').grid(row=10,column=0)


	Label(registerRoot,text='',bg='#222022').grid(row=11,column=0)
	Label(registerRoot,text='',bg='#222022').grid(row=12,column=0)

	Button(registerRoot,text='RESET',bg='#1ed2f4',font='Arial 10',width=8,command=resetRegister).grid(row=13,column=0)
	Button(registerRoot,text='SUBMIT',bg='#1ed2f4',font='Arial 10',width=8,command=submit).grid(row=13,column=1)
	Label(registerRoot,text='',bg='#222022').grid(row=14,column=0)
	Label(registerRoot,text='',bg='#222022').grid(row=15,column=0)


def loginRoot():
	def resetLogin():
		e1.delete(0,END)
		e2.delete(0,END)
	def isEmpty(text):
		if not text:
			return 0
		else:
			return 1
	def login():
		def destroy():
			newRoot.destroy()
		def isEmpty(text):
			if not text:
				return 0
			else:
				return 1
		uname=e1.get()
		pwd=e2.get()
		if isEmpty(uname):
			if isEmpty(pwd):
				try:
					con=sqlite3.Connection('logReg')
					cur=con.cursor()
					try:
						#if pwd not in ["1=1","--","'OR 1=1 --","' OR 1=1 --"]:
						if '=' not in pwd:
							sqlText="select * from user where uname='"+uname+"' and pwd='"+pwd+"'"
							cur.execute(sqlText)
							a = cur.fetchall()
							#print a
							if a:
								name=a[0][0]
								loginRoot.destroy()
								newRoot=Tk()
								newRoot.geometry("500x100")
								newRoot.configure(background='#222022')
								showMessage="   Welcome "+name
								Label(newRoot,text=showMessage,font='Arial 15 bold',bg='#222022',fg='#ffffff').grid(row=0,column=0)
								Label(newRoot,text='',bg='#222022').grid(row=1,column=0)
								Label(newRoot,text='',bg='#222022').grid(row=2,column=0)
								Button(newRoot,text='EXIT',bg='#1ed2f4',fg='#000000',command=destroy).grid(row=3,column=0)
								newRoot.mainloop()
							else:
								messagebox.showinfo("STATUS", "Not Registerd.")
						else:
							messagebox.showinfo("STATUS", "Try Again.")
					except:
						messagebox.showinfo("STATUS", "Try with a different username.")
				except:
					messagebox.showinfo("STATUS", "Something went Wrong, Try Again.")
			else:
				messagebox.showinfo("STATUS", "Password Required")
		else:
			messagebox.showinfo("STATUS", "Username Required")
	loginRoot=Tk()
	loginRoot.configure(background='#222022')
	Label(loginRoot,text='LOGIN',width=30,font='Arial 20 bold',bg='#222022',fg='#ffffff').grid(row=0,column=0,columnspan=2)
	Label(loginRoot,text='',bg='#222022').grid(row=1,column=0)
	Label(loginRoot,text='USERNAME:',bg='#222022',fg='#1ed2f4',font='Arial 10').grid(row=2,column=0)
	e1=Entry(loginRoot,font='Arial 10')
	e1.grid(row=2,column=1)
	Label(loginRoot,text='',bg='#222022').grid(row=3,column=0)
	Label(loginRoot,text='PASSWORD:',bg='#222022',fg='#1ed2f4',font='Arial 10').grid(row=4,column=0)
	e2=Entry(loginRoot,font='Arial 10',show="*")
	e2.grid(row=4,column=1)
	Label(loginRoot,text='',bg='#222022').grid(row=5,column=0)
	Button(loginRoot,text='RESET',width=7,bg='#1ed2f4',fg='#000000',command=resetLogin).grid(row=6,column=0)
	Button(loginRoot,text='LOGIN',width=7,bg='#1ed2f4',fg='#000000',command=login).grid(row=6,column=1)
	Label(loginRoot,text='',bg='#222022').grid(row=7,column=0)
	loginRoot.mainloop()
root.configure(background='#222022')
Label(root,text='REGISTER & LOGIN',width=30,font='Arial 20 bold',bg='#222022',fg='#ffffff').grid(row=0,column=0,columnspan=2)
Label(root,text='',bg='#222022').grid(row=1,column=0)
Label(root,text='',bg='#222022').grid(row=2,column=0)
Button(root,text='REGISTER',width=7,bg='#1ed2f4',fg='#000000',command=registerRoot).grid(row=3,column=0)
Button(root,text='LOGIN',width=7,bg='#1ed2f4',fg='#000000',command=loginRoot).grid(row=3,column=1)
Label(root,text='',bg='#222022').grid(row=4,column=0)
root.mainloop()