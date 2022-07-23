from tkinter import *

#check float
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#click function
def click(event):
	global string
	text = event.widget.cget("text")

	#equal operator
	if text == "=":
		#replace X with *
		string.set(str(string.get()).replace("X","*"))
		#replace ÷ with /
		string.set(str(string.get()).replace("÷","/"))

		if string.get().isdigit():
			val = int(string.get())
		else:
			try:
				val = round(eval(screen.get()),5)
			except Exception as e:
				string.set("Error")
				screen.update()

		string.set(val)
		screen.update()

	#clear screen
	elif text == "AC":
		string.set("")
		screen.update()

	#opposite sign
	elif text == "+/-":
		if screen.get().isdigit():
			val=int(screen.get())
			string.set(-val)
			screen.update()

		elif isfloat(screen.get()):
			val=float(screen.get())
			string.set(-val)
			screen.update()

	#visible in screen
	else:
		string.set(string.get()+text)
		screen.update()

#initialize
root = Tk()

#title
root.title("Calculator")

#size
root.geometry("250x300")
root.maxsize(250,320)
root.minsize(250,320)

#screen
string=StringVar()
string.set("")
screen=Entry(root,textvar=string, font="comicsansm 35 bold", bg="grey", borderwidth=2, fg="white")
screen.pack(fill="x")

#frame1
frame1=Frame(root)
frame1.pack()
#button1
button1=Button(frame1, text="AC", font="comicsansm 15 bold", padx=3, pady=12)
button1.pack(side=LEFT)
button1.bind("<Button-1>",click)
#button2
button2=Button(frame1, text="+/-", font="comicsansm 15 bold", padx=3, pady=12)
button2.pack(side=LEFT)
button2.bind("<Button-1>",click)
#button3
button3=Button(frame1, text="%", font="comicsansm 15 bold", padx=3.5, pady=12)
button3.pack(side=LEFT)
button3.bind("<Button-1>",click)
#button4
button4=Button(frame1, text="÷", font="comicsansm 15 bold", padx=4.5, pady=12)
button4.pack(side=LEFT)
button4.bind("<Button-1>",click)

#frame2
frame2=Frame(root)
frame2.pack()
#button5
button5=Button(frame2, text="7", font="comicsansm 15 bold", padx=8, pady=12)
button5.pack(side=LEFT)
button5.bind("<Button-1>",click)
#button6
button6=Button(frame2, text="8", font="comicsansm 15 bold", padx=8, pady=12)
button6.pack(side=LEFT)
button6.bind("<Button-1>",click)
#button7
button7=Button(frame2, text="9", font="comicsansm 15 bold", padx=8, pady=12)
button7.pack(side=LEFT)
button7.bind("<Button-1>",click)
#button8
button8=Button(frame2, text="X", font="comicsansm 15 bold", padx=8, pady=12, bg="orange")
button8.pack(side=LEFT)
button8.bind("<Button-1>",click)

#frame3
frame3=Frame(root)
frame3.pack()
#button9
button9=Button(frame3, text="4", font="comicsansm 15 bold", padx=8, pady=12)
button9.pack(side=LEFT)
button9.bind("<Button-1>",click)
#button10
button10=Button(frame3, text="5", font="comicsansm 15 bold", padx=8, pady=12)
button10.pack(side=LEFT)
button10.bind("<Button-1>",click)
#button11
button11=Button(frame3, text="6", font="comicsansm 15 bold", padx=8, pady=12)
button11.pack(side=LEFT)
button11.bind("<Button-1>",click)
#button12
button12=Button(frame3, text="-", font="comicsansm 15 bold", padx=8, pady=12)
button12.pack(side=LEFT)
button12.bind("<Button-1>",click)

#frame4
frame4=Frame(root)
frame4.pack()
#button9
button13=Button(frame4, text="1", font="comicsansm 15 bold", padx=8, pady=12)
button13.pack(side=LEFT)
button13.bind("<Button-1>",click)
#button10
button14=Button(frame4, text="2", font="comicsansm 15 bold", padx=8, pady=12)
button14.pack(side=LEFT)
button14.bind("<Button-1>",click)
#button11
button15=Button(frame4, text="3", font="comicsansm 15 bold", padx=8, pady=12)
button15.pack(side=LEFT)
button15.bind("<Button-1>",click)
#button12
button16=Button(frame4, text="+", font="comicsansm 15 bold", padx=8, pady=12)
button16.pack(side=LEFT)
button16.bind("<Button-1>",click)

#frame5
frame5=Frame(root)
frame5.pack()
#button17
button17=Button(frame5, text="0", font="comicsansm 15 bold", padx=38, pady=12)
button17.pack(side=LEFT)
button17.bind("<Button-1>",click)
#button18
button18=Button(frame5, text=".", font="comicsansm 15 bold", padx=8, pady=12)
button18.pack(side=LEFT)
button18.bind("<Button-1>",click)
#button11
button19=Button(frame5, text="=", font="comicsansm 15 bold", padx=8, pady=12)
button19.pack(side=LEFT)
button19.bind("<Button-1>",click)

root.mainloop()