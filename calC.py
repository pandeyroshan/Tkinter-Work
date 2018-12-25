from tkinter import *
root = Tk()
root.title("Calculator")
e = Entry(root,font='Arial 25 bold',width=16,bd=5,bg='light gray',justify='right')
e.grid(row=0,column=0,columnspan=4)

def add(x):
	e.insert(16,x)
def canc():
	e.delete(0,END)
def result():	
	r = eval(e.get())
	e.delete(0,END)
	e.insert(0,r)
	

Button(root,text='7',width=5,height=2,command=lambda:add(7)).grid(row=1,column=0,sticky=N+S+E+W)
Button(root,text='8',width=5,height=2,command=lambda:add(8)).grid(row=1,column=1,sticky=N+S+E+W)
Button(root,text='9',width=5,height=2,command=lambda:add(9)).grid(row=1,column=2,sticky=N+S+E+W)
Button(root,text='+',width=5,height=2,command=lambda:add('+')).grid(row=1,column=3,sticky=N+S+E+W)
Button(root,text='4',width=5,height=2,command=lambda:add(4)).grid(row=2,column=0,sticky=N+S+E+W)
Button(root,text='5',width=5,height=2,command=lambda:add(5)).grid(row=2,column=1,sticky=N+S+E+W)
Button(root,text='6',width=5,height=2,command=lambda:add(6)).grid(row=2,column=2,sticky=N+S+E+W)
Button(root,text='-',width=5,height=2,command=lambda:add('-')).grid(row=2,column=3,sticky=N+S+E+W)
Button(root,text='1',width=5,height=2,command=lambda:add(1)).grid(row=3,column=0,sticky=N+S+E+W)
Button(root,text='2',width=5,height=2,command=lambda:add(2)).grid(row=3,column=1,sticky=N+S+E+W)
Button(root,text='3',width=5,height=2,command=lambda:add(3)).grid(row=3,column=2,sticky=N+S+E+W)
Button(root,text='*',width=5,height=2,command=lambda:add('*')).grid(row=3,column=3,sticky=N+S+E+W)
Button(root,text='C',width=5,height=2,command=canc).grid(row=4,column=0,sticky=N+S+E+W)
Button(root,text='0',width=5,height=2,command=lambda:add(0)).grid(row=4,column=1,sticky=N+S+E+W)
Button(root,text='=',width=5,height=2,command=result).grid(row=4,column=2,sticky=N+S+E+W)
Button(root,text='/',width=5,height=2,command=lambda:add('/')).grid(row=4,column=3,sticky=N+S+E+W)

root.mainloop()

