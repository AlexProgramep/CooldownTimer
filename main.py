import time
from tkinter import Tk, StringVar, Entry, Button, CENTER
from pygame import mixer

root = Tk()
SIZE = 500
root.geometry(F"{SIZE}x{SIZE}")
root.minsize(SIZE, SIZE)
root.maxsize(SIZE, SIZE)
root.title("Будильник")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourTextbox = Entry(root, width=3, font=("Calibri", 20, ""), textvariable=hour)
minuteTextbox = Entry(root, width=3, font=("Calibri", 20, ""), textvariable=minute)
secondTextbox = Entry(root, width=3, font=("Calibri", 20, ""), textvariable=second)

hourTextbox.place(x=170, y=180)
minuteTextbox.place(x=220, y=180)
secondTextbox.place(x=270, y=180)

def runTimer():
	try:
		clockTime = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
	except:
		print("Некоректнi значення")

	while (clockTime > -1):

		totalMin, totalSec = divmod(clockTime, 60)

		totalHours = 0
		if totalMin > 60:
			totalHours, totalMin = divmod(totalMin, 60)

		hour.set("{0:2d}".format(totalHours))
		minute.set("{0:2d}".format(totalMin))
		second.set("{0:2d}".format(totalSec))

		root.update()
		time.sleep(1)


		if (clockTime == 0):
			mixer.init()
			mixer.music.load('sound.mp3')
			mixer.music.play()

		clockTime -= 1


setTimeButton = Button(root, text='Встановити час', bd='5', command=runTimer)
setTimeButton.place(x=242, y=250, anchor=CENTER)

if __name__ == "__main__":
	root.mainloop()
