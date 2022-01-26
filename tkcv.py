from tkinter import *
import turtle, time, random
from tkinter.font import BOLD
from PIL import Image,ImageTk
from playsound import playsound
from tkinter import ttk
from tkinter import ttk,messagebox
import cv2
import subprocess as sp
def press():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
    #root.destroy()
    vid = cv2.VideoCapture(0)
    while(True):
	    ret, frame = vid.read()
	    cv2.imshow('YOUR MIRROR', frame)
	
	    if cv2.waitKey(1) & 0xFF == ord('q'):
		    break
    vid.release()
    cv2.destroyAllWindows()
def song():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
    import colour  
def canvas():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
    import aircanvas 
def arduino():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
     #tell python we need 3 different modules
    turtle.speed(0) #set draw speed to the fastest
    turtle.colormode(255) #special colormode
    turtle.pensize(4) #size of the lines that will be drawn
    def triangle(size): #This is our own function, in the parenthesis is a variable we have defined that

        turtle.forward(size) #to begin this function we go forward, the amount to go forward by is the
        turtle.right(90) #turn right by 90 degree
        turtle.forward(size) #go forward, again with variable
        turtle.right(135) #turn right again
        turtle.forward(size * 1.5) 
    while(1): #INFINITE LOOP
        turtle.setpos(random.randint(-200, 200), random.randint(-200, 200)) #set the draw point to a
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
#randomize the RGB color
        triangle(random.randint(5, 55)) #use our function, because it has only one variable we can
    
        turtle.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
def hello():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
    messagebox.showinfo("INFO","Connect arduino ")
    import ardcam   

def graph():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3')   
    ninja = turtle.Turtle()
    ninja.speed(10)
    for i in range(180):
      ninja.forward(100)
      ninja.right(30)
      ninja.forward(20)
      ninja.left(60)
      ninja.forward(50)
      ninja.right(30)
 
      ninja.penup()
      ninja.setposition(0, 0)
      ninja.pendown()
 
      ninja.right(2)
 
    turtle.done() 
def play():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
    #root.destroy()
    x=random.randint(1,6)
    if x==1:
        playsound('C:\\Users\Rajib Kr paul\\Music\\bengali\\Keno Barle boyosh chotto belar bondhu hariye jay By Shayan.mp3')
    elif x==2: 
        playsound('C:\\Users\Rajib Kr paul\\Music\\bengali\\Sei Raate Raat chilo purnima.mp3')
    elif x==3:
        playsound('C:\\Users\Rajib Kr paul\\Music\\hindi song\\Chaha Hai Tujhko Song Cover By Debolinaa NandyMannAamir Khan, ManishaOld Songs Renditions.mp3')
    elif x==4:
        playsound('C:\\Users\Rajib Kr paul\\Music\\hindi song\\Ya Ali Reham Ali Cover By Yumna Ajin.mp3')   
    elif x==5:
        playsound('C:\\Users\Rajib Kr paul\\Music\\hindi song\\maya chali maya chali payar ki gali.mp3')   
    elif x==6:
        playsound('C:\\Users\\Rajib Kr paul\\Music\\english song\\FROZEN Let It Go Sing-along Official Disney UK.mp3')   
def show():
    playsound('C:\\Users\\Rajib Kr paul\\Music\\Video Project music\\click.mp3') 
    programName = "notepad.exe"
    fileName = "info.txt"
    sp.Popen([programName, fileName])           
root=Tk()
photo=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\python practice\\favicon.ico")
root.iconphoto(False,photo)
root.geometry("1600x900")
root.title("YOUR MIRROR")
f1=Frame(root,bg="cyan")
f1.place(x=0,y=0,width=1600,height=100)
l1=Label(f1,text="YOUR MIRROR",fg="yellow",font=("Times New Roman",20,"bold"),bg="blue")
l1.place(x=700,y=40)
f2=Frame(root,bg="yellow")
f2.place(x=0,y=100,width=800,height=100)
b1=Button(f2,bg="green",text="press",command=press,font=100)
b1.place(x=360,y=35)
l2=Label(f2,text="press for see your face(press q for exit)",fg="black",font=20)
l2.place(x=240,y=12)
f3=Frame(root,bg="orange")
f3.place(x=800,y=100,height=100,width=800)
l3=Label(f3,text="press e for close",fg="black",font=20)
l3.place(x=280,y=10)
b2=Button(f3,bg="pink",text="Press for colour detection",command=song,font=100)
b2.place(x=240,y=35)
f4=Frame(root,bg="light green")
f4.place(x=0,y=190,width=1600,height=670)
bg=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\\Attachments\\Desktop\\Pictures\\Video Projects\\dream.png")
bglb=Label(f4,image=bg)
bglb.place(x=1000,y=0,width=600,height=300)
f5=Frame(f4,bg="red",borderwidth=2)
f5.place(x=600,y=0,width=500,height=300)
l4=Label(f5,text="press q for quit \n aircanvas ",fg="black",font=BOLD)
l4.place(x=180,y=10)
b3=Button(f4,bg="light blue",text="air canvas",command=canvas,font=100)
b3.place(x=800,y=100)
b4=Button(f4,text="creat random",command=arduino,bg="yellow",fg="black",font=20)
b4.place(x=792,y=150)
f6=Frame(f4,bg="brown")
f6.place(x=0,y=300,width=1600,height=100)
b5=Button(f6,text=" random graphics",command=graph,bg="green",font=20)
b5.place(x=800,y=40)
f7=Frame(f4,bg="grey")
f7.place(x=0,y=400,width=1600,height=100)
b6=Button(f7,text="play random song",bg="red",font=20,command=play)
b6.place(x=797,y=40)
f8=Frame(f4,bg="gold")
f8.place(x=0,y=500,height=200,width=1600)
b7=Button(f8,text="connect arduino",command=hello,bg="green",font=20)
b7.place(x=800,y=40)
b8=Button(f4,text="keep information",command=show,bg="cyan",font=15)
b8.place(x=400,y=200)
l5=Label(f4,text="Instruction: \n 1.To close all window you have to keep cursur on specific window \n 2.You are not allowed to use mutliple button at single time\n 3.Don't do any thing when a song is playing",font=20,fg="blue")
l5.place(x=60,y=30)
root.mainloop()