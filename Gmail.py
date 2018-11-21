import smtplib
from datetime import datetime
import os
import sqlite3
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import tkMessageBox
import tkFileDialog
from Tkinter import *
def mailSetup():
	splashRoot.destroy()
	root = Tk()
	def isValid(email):
		if len(email) > 7:
			if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
				return 1
			else:
				return 0
	def isEmpty(subject):
		if not subject:
			return 0
		else:
			return 1
	def mailHistory():
		root.destroy()
		mailHistoryRoot=Tk()
		mailHistoryRoot.title("GMAIL")
		mailHistoryRoot.attributes('-zoomed', True)
		mailHistoryRoot.configure(background='#222022')
		Label(mailHistoryRoot,text='HISTORY',font="Arial 40",fg='#6ead3a',bg='#222022',anchor="center",width=45).grid(row=0,column=0,columnspan=4)
		Label(mailHistoryRoot,text='',bg='#222022').grid(row=1,column=0)
		Label(mailHistoryRoot,text='',bg='#222022').grid(row=2,column=0)
		Label(mailHistoryRoot,text='SENDER',font="Arial 15",fg='#6ead3a',bg='#222022',anchor="center").grid(row=3,column=0)
		Label(mailHistoryRoot,text='RECIEVER',font="Arial 15",fg='#6ead3a',bg='#222022',anchor="center").grid(row=3,column=1)
		Label(mailHistoryRoot,text='SUBJECT',font="Arial 15",fg='#6ead3a',bg='#222022',anchor="center").grid(row=3,column=2)
		Label(mailHistoryRoot,text='DATE/TIME',font="Arial 15",fg='#6ead3a',bg='#222022',anchor="center").grid(row=3,column=3)
		Label(mailHistoryRoot,text='',bg='#222022').grid(row=4,column=0)
		Label(mailHistoryRoot,text='',bg='#222022').grid(row=5,column=0)
		con=sqlite3.Connection('mysqlite')
		cur=con.cursor()
		cur.execute("select * from recordnew")
		a = cur.fetchall()
		i=0
		j=6
		for data in a:
			sender=a[i][0]
			receiver=a[i][1]
			subject=a[i][2]
			dateTime=a[i][3]
			Label(mailHistoryRoot,text=sender,font="Arial 15",fg='#ffffff',bg='#222022',anchor="center").grid(row=j,column=0)
			Label(mailHistoryRoot,text=receiver,font="Arial 15",fg='#ffffff',bg='#222022',anchor="center").grid(row=j,column=1)
			Label(mailHistoryRoot,text=subject,font="Arial 15",fg='#ffffff',bg='#222022',anchor="center").grid(row=j,column=2)
			Label(mailHistoryRoot,text=dateTime,font="Arial 15",fg='#ffffff',bg='#222022',anchor="center").grid(row=j,column=3)
			i=i+1
			j=j+1
		mailHistoryRoot.mainloop()
	def sendWithFile():
		try:
			senderEmail = e1.get()
			receiver = e2.get()
			password = e3.get()
			subject = e4.get()
			message = t.get("1.0","end-1c")
			filepath = tkFileDialog.askopenfilename()
			head,filename = os.path.split(filepath)
			e5.delete(0,END)
			e5.insert(0,filename)
			if(isValid(senderEmail)):
				if(isValid(receiver)):
					if(isEmpty(filepath)):
						if(isEmpty(filepath)):
							if(isEmpty(subject)):
								msg = MIMEMultipart()    
								msg['From'] = senderEmail	    
								msg['To'] = receiver 
								msg['Subject'] = subject
								msg.attach(MIMEText(message, 'plain'))
								filepath = open(filepath, "rb") 
								p = MIMEBase('application', 'octet-stream')
								p.set_payload((filepath).read()) 
								encoders.encode_base64(p) 
								p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
								msg.attach(p) 
								s = smtplib.SMTP('smtp.gmail.com', 587) 
								s.starttls() 
								s.login(senderEmail, password) 
								text = msg.as_string() 
								s.sendmail(senderEmail,receiver,text)
								s.quit()
								con=sqlite3.Connection('mailHistory')
								cur=con.cursor()
								cur.execute("create table if not exists mailHistory(sender varchar(30),reciever varchar(30),pwd varchar(20),subject varchar(50),time varchar(20))")
								dateTime= str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
								cur.execute("insert into mailHistory values(?,?,?,?,?)",(senderEmail,receiver,password,subject,dateTime))
								con.commit()
								tkMessageBox.showinfo("STATUS", "Email delivered Successfully with attached file.")
							else:
								tkMessageBox.showerror("STATUS", "Subject Field Empty")
						else:
							tkMessageBox.showerror("STATUS", "Mention the FilePath Name")
					else:
						tkMessageBox.showerror("STATUS", "Mention the File Name")
				else:
					tkMessageBox.showerror("STATUS", "Invalid Receiver's Email")
			else:
				tkMessageBox.showerror("STATUS", "Invalid Sender's Email")
		except:
				tkMessageBox.showerror("STATUS", "Something went Wrong")
	def send():
		try:
			senderEmail = e1.get()
			receiver = e2.get()
			password = e3.get()
			subject = e4.get()
			message = t.get("1.0","end-1c")
			if(isValid(senderEmail)):
				if(isValid(receiver)):
					server = smtplib.SMTP('smtp.gmail.com:587')
					server.ehlo()
					server.starttls()
					if(isEmpty(subject)):
						server.login(senderEmail, password)
						message = 'Subject: {}\n\n{}'.format(subject, message)
						server.sendmail(senderEmail, receiver, message)
						server.quit()
						try:
							con=sqlite3.Connection('mysqlite')
							cur=con.cursor()
							cur.execute("create table if not exists recordnew(sender varchar(30),reciever varchar(30),subject varchar(50),time varchar(20))")
							dateTime= str(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
							cur.execute("insert into recordnew values(?,?,?,?)",(senderEmail,receiver,subject,dateTime))
							con.commit()
						except:
							tkMessageBox.showinfo("STATUS", "History of this mail is not saved due to some internal Errors.")
						tkMessageBox.showinfo("STATUS", "Email delivered Successfully.")
					else:
						tkMessageBox.showerror("STATUS", "Subject Field Empty")
				else:
					tkMessageBox.showerror("STATUS", "Invalid Receiver's Email")
			else:
				tkMessageBox.showerror("STATUS", "Invalid Sender's Email")
		except:
				tkMessageBox.showerror("STATUS", "Something went Wrong")

	def reset():	
		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)	
		e4.delete(0,END)
		t.delete(1.0, END)
		e5.delete(0,END)
	root.title("GMAIL")
	root.attributes('-zoomed', True)
	root.configure(background='#222022')
	Label(root,text="EMAIL SENDING SETUP",font="Arial 40",fg='#6ead3a',bg='#222022',width=45).grid(row=0,column=0,columnspan=2)
	Label(root,text="",bg='#222022').grid(row=1,column=0)
	Label(root,text="",bg='#222022').grid(row=2,column=0)
	Label(root,text="YOUR EMAIL :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=3,column=0)
	e1 = Entry(root,bd=3,width=30,bg='#222022',fg='#ffffff',font='Arial 15')
	e1.grid(row=3,column=1,ipady=3)
	Label(root,text="",bg='#222022').grid(row=4,column=0)
	Label(root,text="RECEIVER'S EMAIL :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=5,column=0)
	e2 = Entry(root,bd=3,width=30,bg='#222022',fg='#ffffff',font='Arial 15')
	e2.grid(row=5,column=1,ipady=3)
	Label(root,text="",bg='#222022').grid(row=6,column=0)
	Label(root,text="PASSWORD :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=7,column=0)
	e3 = Entry(root,bd=3,show="*",width=30,bg='#222022',fg='#ffffff',font='Arial 15')
	e3.grid(row=7,column=1,ipady=3)
	Label(root,text="",bg='#222022').grid(row=8,column=0)
	Label(root,text="SUBJECT :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=9,column=0)
	e4 = Entry(root,bd=3,width=30,bg='#222022',fg='#ffffff',font='Arial 15')
	e4.grid(row=9,column=1,ipady=3)
	Label(root,text="",bg='#222022').grid(row=10,column=0)
	Label(root,text="MESSAGE :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=11,column=0)
	t = Text(root, height=5, width=30,bd=3,bg='#222022',fg='#ffffff',font='Arial 15')
	t.grid(row=11,column=1)
	Label(root,text="",bg='#222022').grid(row=12,column=0)
	Label(root,text="FILE NAME :",fg='#f4f5f6',bg='#222022',font='Arial 15').grid(row=13,column=0)
	e5 = Entry(root,bd=3,width=30,bg='#222022',fg='#ffffff',font='Arial 15')
	e5.grid(row=13,column=1,ipady=3)
	Label(root,text="",bg='#222022').grid(row=14,column=0)
	Label(root,text="",bg='#222022').grid(row=15,column=0)
	Button(root,text="RESET",borderwidth=3,bg='#1ed2f4',width=30,font='Arial 15',command=reset).grid(row=16,column=0,ipady=5)
	Button(root,text="SEND",borderwidth=3,bg='#1ed2f4',width=30,font='Arial 15',command=send).grid(row=16,column=1,ipady=5)
	Label(root,text="",bg='#222022').grid(row=17,column=0)
	Label(root,text="",bg='#222022').grid(row=18,column=0)
	Button(root,text="SEND WITH FILE",borderwidth=3,bg='#1ed2f4',width=30,font='Arial 15',command=sendWithFile).grid(row=19,column=0,ipady=5)
	Button(root,text="HISTORY",borderwidth=3,bg='#1ed2f4',width=30,font='Arial 15',command=mailHistory).grid(row=19,column=1,ipady=5)
	Label(root,text="",bg='#222022').grid(row=20,column=0)
	root.mainloop()
splashRoot=Tk()
splashRoot.title('SPLASH SCREEN')

splashRoot.after(3000,mailSetup)

splashRoot.attributes('-zoomed', True)
splashRoot.configure(background='#222022')
Label(splashRoot,text="",bg='#222022').grid(row=0,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=1,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=2,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=3,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=4,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=5,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=6,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=7,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=8,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=9,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=10,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=11,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=12,column=0)
Label(splashRoot,text='ROSHAN PANDEY',width=46,font='Arial 40 bold',bg='#222022',fg='#6ead3a').grid(row=13,column=0,columnspan=2)
Label(splashRoot,text="",bg='#222022').grid(row=14,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=15,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=16,column=0)
Label(splashRoot,text="",bg='#222022').grid(row=17,column=0)
Label(splashRoot,text='Enrollment No',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=18,column=0)
Label(splashRoot,text='171B102',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=18,column=1)
Label(splashRoot,text="",bg='#222022').grid(row=19,column=0)

Label(splashRoot,text='Batch',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=20,column=0)
Label(splashRoot,text='B3',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=20,column=1)
Label(splashRoot,text="",bg='#222022').grid(row=21,column=0)

Label(splashRoot,text='Email Id',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=22,column=0)
Label(splashRoot,text='pandeyroshan556@gmail.com',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=22,column=1)
Label(splashRoot,text="",bg='#222022').grid(row=23,column=0)

Label(splashRoot,text='Phone No',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=24,column=0)
Label(splashRoot,text='9479752851',font='Arial 20 bold',bg='#222022',fg='#ceccce').grid(row=24,column=1)
splashRoot.mainloop()