from tkinter import *
import sqlite3
from tkinter import messagebox
def mainProgram(e):
	s.destroy()
	root = Tk()
	root.configure(background='#f4f5f6')
	def addContact():
		addRoot=Tk()
		def isNameEmpty(name):
			if not name:
				return 0
			else:
				return 1
		def isNumberEmpty(number):
			if not number:
				return 0
			else:
				return 1
		def reset():
			addRoot.destroy()
		def addContact():
			try:
				name=e1.get()
				number=e2.get()
				con=sqlite3.Connection('file')
				cur=con.cursor()
				cur.execute("create table if not exists contact(pnum varchar(10) primary key,name varchar(20))")
				#cur.execute("delete from contact")   #Discomment it to drop the table
				if(isNameEmpty(name)):
					if(isNumberEmpty(number)): 
						sqliteText = "insert into contact values('"+number+"','"+name+"')"
						try:
							cur.execute(sqliteText)
							string = name + " has been added to your Contact list."
							messagebox.showerror("STATUS", string)
						except:
							messagebox.showerror("STATUS", "This Number is Already added.")
						finally:
							con.commit()
					else:
						messagebox.showerror("STATUS", "Phone Number Required.")
				else:
					messagebox.showerror("STATUS", "Name Required.")
			except:
				messagebox.showerror("STATUS", "Please Try Again")
		addRoot.configure(background='#f4f5f6')
		Label(addRoot,text='INSERT CONTACT',font='Arial 20 bold',bg='#f4f5f6',fg='#2b2b3a',width=40).grid(row=0,column=0,columnspan=2)
		Label(addRoot,text='',bg='#f4f5f6').grid(row=1,column=0)
		Label(addRoot,text='NAME :',bg='#f4f5f6',fg='#000000',font='Arial 10 bold').grid(row=2,column=0)
		e1 = Entry(addRoot,bg='#f4f5f6',fg='#000000')
		e1.grid(row=2,column=1,ipady=3)
		Label(addRoot,text='',bg='#f4f5f6').grid(row=3,column=0)
		Label(addRoot,text='NUMBER :',bg='#f4f5f6',fg='#000000',font='Arial 10 bold').grid(row=4,column=0)
		e2 = Entry(addRoot,bg='#f4f5f6',fg='#000000')
		e2.grid(row=4,column=1,ipady=3)
		Label(addRoot,text='',bg='#f4f5f6').grid(row=5,column=0)
		Button(addRoot,text='EXIT',font='Arial 10',fg='#000000',width=9,bg='#eafc40',command=reset).grid(row=6,column=0)
		Button(addRoot,text='INSERT',font='Arial 10',fg='#000000',width=9,bg='#eafc40',command=addContact).grid(row=6,column=1)
		Label(addRoot,text='',bg='#f4f5f6').grid(row=7,column=0)
		addRoot.mainloop()
	def searchContact():
		searchRoot=Tk()
		def reset():
			searchRoot.destroy()
		def search2():
			name = e1.get()
			con=sqlite3.Connection('file')
			cur=con.cursor()
			sqliteText="select pnum from contact where name='"+name+"'"
			cur.execute(sqliteText)
			number=cur.fetchall()
			try:
				textToBeFill=number[0]
				finalText=textToBeFill[0]
				e2.delete(0,END)
				e2.insert(0,finalText)
			except:
				messagebox.showerror("STATUS", "No contact with this name.")
		searchRoot.configure(background='#f4f5f6')
		Label(searchRoot,text='FIND CONTACT',font='Arial 20 bold',bg='#f4f5f6',fg='#2b2b3a',width=40).grid(row=0,column=0,columnspan=2)
		Label(searchRoot,text='',bg='#f4f5f6').grid(row=1,column=0)
		Label(searchRoot,text='NAME :',bg='#f4f5f6',fg='#000000',font='Arial 10 bold').grid(row=2,column=0)
		e1 = Entry(searchRoot,bg='#f4f5f6',fg='#000000')
		e1.grid(row=2,column=1,ipady=3)
		Label(searchRoot,text='',bg='#f4f5f6').grid(row=3,column=0)
		Label(searchRoot,text='NUMBER :',bg='#f4f5f6',fg='#000000',font='Arial 10 bold').grid(row=4,column=0)
		e2 = Entry(searchRoot,bg='#f4f5f6',fg='#000000')
		e2.grid(row=4,column=1,ipady=3)
		Label(searchRoot,text='',bg='#f4f5f6').grid(row=5,column=0)
		Button(searchRoot,text='EXIT',font='Arial 10',fg='#000000',width=9,bg='#eafc40',command=reset).grid(row=6,column=0)
		Button(searchRoot,text='FIND',font='Arial 10',fg='#000000',width=9,bg='#eafc40',command=search2).grid(row=6,column=1)
		Label(searchRoot,text='',bg='#f4f5f6').grid(row=7,column=0)
		searchRoot.mainloop()
	def removeContact():
		removeRoot=Tk()
		def reset():
			removeRoot.destroy()
		def remove():
			name=e1.get()
			con=sqlite3.Connection('file')
			cur=con.cursor()
			try:
				deleteText = "delete from contact where name='"+name+"'" 
				cur.execute(deleteText)
				showInfo=name+" has been Deleted from your contact list."
				messagebox.showerror("STATUS", showInfo)
				e2.delete(0,END)
				e2.insert(0,"Number Deleted")
				con.commit()
			except:
				messagebox.showerror("STATUS", "No contact with this name.")
		removeRoot.configure(background='#f4f5f6')
		Label(removeRoot,text='DELETE NUMBER',font='Arial 20 bold',bg='#f4f5f6',fg='#2b2b3a',width=40).grid(row=0,column=0,columnspan=2)
		Label(removeRoot,text='',bg='#f4f5f6').grid(row=1,column=0)
		Label(removeRoot,text='NAME :',bg='#f4f5f6',fg='#000000',font='Arial 10 bold').grid(row=2,column=0)
		e1 = Entry(removeRoot,bg='#f4f5f6',fg='#000000')
		e1.grid(row=2,column=1,ipady=3)
		Label(removeRoot,text='',bg='#f4f5f6').grid(row=3,column=0)
		Label(removeRoot,text='NUMBER :',bg='#f4f5f6',fg='#000000',font='Arial 10 bold').grid(row=4,column=0)
		e2 = Entry(removeRoot,bg='#f4f5f6',fg='#000000')
		e2.grid(row=4,column=1,ipady=3)
		Label(removeRoot,text='',bg='#f4f5f6').grid(row=5,column=0)
		Button(removeRoot,text='EXIT',font='Arial 10',fg='#000000',width=9,bg='#eafc40',command=reset).grid(row=6,column=0)
		Button(removeRoot,text='DELETE',font='Arial 10',fg='#000000',width=9,bg='#eafc40',command=remove).grid(row=6,column=1)
		Label(removeRoot,text='',bg='#f4f5f6').grid(row=7,column=0)
		removeRoot.mainloop()
	def exitRoot():
		root.destroy()
	Label(root,text='TELEPHONE DIRECTORY',font='Arial 20 bold',bg='#f4f5f6',fg='#2b2b3a',width=40).grid(row=0,column=0,columnspan=2)
	Label(root,text='',bg='#f4f5f6').grid(row=1,column=0)
	Label(root,text='',bg='#f4f5f6').grid(row=2,column=0)
	Button(root,text='INSERT',font='Arial 10 bold',fg='#000000',width=10,bg='#eafc40',command=addContact).grid(row=3,column=0,ipady=4)
	Button(root,text='FIND',font='Arial 10 bold',fg='#000000',width=10,bg='#eafc40',command=searchContact).grid(row=3,column=1,ipady=4)
	Label(root,text='',bg='#f4f5f6').grid(row=4,column=0)
	Label(root,text='',bg='#f4f5f6').grid(row=5,column=0)
	Button(root,text='DELETE',font='Arial 10 bold',fg='#000000',width=10,bg='#eafc40',command=removeContact).grid(row=6,column=0,ipady=4)
	Button(root,text='EXIT',font='Arial 10 bold',fg='#000000',width=10,bg='#eafc40',command=exitRoot).grid(row=6,column=1,ipady=4)
	Label(root,text='',bg='#f4f5f6').grid(row=7,column=0)
	Label(root,text='',bg='#f4f5f6').grid(row=8,column=0)
	root.mainloop()
s=Tk()
s.configure(background='#f4f5f6')
Label(s,text='Roshan Pandey',font='Arial 30 bold',width=40,bg='#f4f5f6',fg='#2b2b3a').grid(row=0,column=0,columnspan=2)
Label(s,text='',bg='#f4f5f6').grid(row=1,column=0)
Label(s,text='Enrollment Number',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=2,column=0)
Label(s,text='171B102',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=2,column=1)

Label(s,text='Batch',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=3,column=0)
Label(s,text='BX(B3)',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=3,column=1)

Label(s,text='Gmail Address',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=4,column=0)
Label(s,text='pandeyroshan556@gmail.com',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=4,column=1)

Label(s,text='Contact No',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=5,column=0)
Label(s,text='+91-9479752851',font='Arial 15',bg='#f4f5f6',fg='#000000').grid(row=5,column=1)

Label(s,text='',bg='#f4f5f6').grid(row=6,column=0)
s.bind('<Motion>',mainProgram)
s.mainloop()