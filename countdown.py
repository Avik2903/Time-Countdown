import time
from tkinter import * 
from tkinter import messagebox

root = Tk()
root.geometry("300x250")
root.title("timer")

hour = StringVar()
min = StringVar()
sec = StringVar()
hour.set("00")
min.set("00")
sec.set("00")

hEntry = Entry(root, width=3, font=("Arial",18,""),textvariable=hour)
hEntry.place(x=80,y=20)
mEntry = Entry(root, width=3, font=("Arial",18,""),textvariable=min)
mEntry.place(x=130,y=20)
sEntry = Entry(root, width=3, font=("Arial",18,""),textvariable=sec)
sEntry.place(x=180,y=20)

def submit():
	try:
		temp = int(hour.get())*3600 + int(min.get())*60 + int(sec.get())
	except:
		print("Please input the right value")
	while temp >-1:
		mins,secs = divmod(temp,60)
		hours=0
		if mins >60:
			hours, mins = divmod(mins, 60)
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))
		root.update()
		time.sleep(1)
		if (temp == 0):
			messagebox.showinfo("Time Countdown", "Time's up ")
		temp -= 1
btn = Button(root, text='Set Time Countdown', bd='5',command= submit)
btn.place(x = 70,y = 120)
root.mainloop()

