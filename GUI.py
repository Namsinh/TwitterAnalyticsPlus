from tkinter import *
from tkinter import messagebox

root = Tk()

for r in range(3):
   for c in range(4):
      Label(root, text='R%s/C%s'%(r,c),
         borderwidth=1 ).grid(row=r,column=c)
root.mainloop(  )

# Frame
root = Tk()
frame = Frame(root)
frame.pack()

# Username input field
L1 = Label(frame, text="User Name")
L1.pack(side = LEFT)
E1 = Entry(frame, bd =5)
E1.pack(side = RIGHT)


# Submit button
def helloCallBack():
   messagebox.showinfo("Connecting to Twitter", "Getting tweets from Twitter. This may take a few minutes...")

B = Button(frame, text ="Analyze", command = helloCallBack)
B.pack(side = RIGHT)
root.mainloop()
