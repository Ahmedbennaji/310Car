from tkinter import *

import socket
import threading

# Main Tk window instantiation
root = Tk()
root.title('Control GUI')
root.iconbitmap(r'suv.ico')



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 host = '10.200.0.112'
 hostCharter = '192.168.1.3'

connectCharter = '192.168.1.11'
connectMSU = '10.152.163.151'

port = 9999

s.connect((connectMSU, port))


def back(event):
    msg = "back"
    s.send(msg.encode('ascii'))
    statusbar['text'] = "Reverse"

def forward(event):
    msg = "forward"
    s.send(msg.encode('ascii'))
    statusbar['text']= "Forward"

def right(event):
    msg = "right"
    s.send(msg.encode('ascii'))
    statusbar['text']="Right"

def left(event):
    msg = "left"
    s.send(msg.encode('ascii'))
    statusbar['text'] = "Left"

def stop(event):
    msg = "stop"
    s.send(msg.encode('ascii'))
    statusbar['text'] = "Stop"

def stopFast(event):
    msg = "stopFast"
    s.send(msg.encode('ascii'))


def setSpeed(event):
    if (event.char == '1'):
        msg = "speed1"
        s.send(msg.encode('ascii'))
    if (event.char == '2'):
        msg = "speed2"
        s.send(msg.encode('ascii'))
    if (event.char == '3'):
        msg = "speed3"
       s.send(msg.encode('ascii'))

def disconnect(event):
    s.close()


# bind key to call back function using tkinter
root.bind('<Up>', forward)
root.bind('<KeyRelease-Up>', stop)

root.bind('<Down>', back)
root.bind('<KeyRelease-Down>', stop)

root.bind('<Left>', left)
root.bind('<KeyRelease-Left>', stop)

root.bind('<Right>', right)
root.bind('<KeyRelease-Right>', stop)

root.bind('1', setSpeed)
root.bind('2', setSpeed)
root.bind('3', setSpeed)

root.bind('<BackSpace>', stopFast)
root.bind('<Escape>', disconnect)

middleFrame = Frame(root)
middleFrame.pack(padx=10, pady=30)

leftPhoto=PhotoImage(file='left-arrow.png')
leftButton = Button(middleFrame, image=leftPhoto, command = left)
leftButton.pack(side=LEFT, padx= 10)


rightPhoto=PhotoImage(file='right-arrow.png')
rightButton = Button(middleFrame, image=rightPhoto, command = right)
rightButton.pack(side=RIGHT, padx= 10)

upPhoto = PhotoImage(file='up-arrow.png')
upButton = Button(middleFrame, image=upPhoto, command = forward)
upButton.pack(side=TOP ,padx= 10, pady=10)

downPhoto = PhotoImage(file='down-arrow.png')
downButton = Button(middleFrame, image=downPhoto, command = back)
downButton.pack(side=BOTTOM, padx= 10, pady=10)

buttomFrame = Frame(root)
buttomFrame.pack(padx=15, pady=15)

breakPhoto = PhotoImage(file='brake.png')
breakButton = Button(buttomFrame, image=breakPhoto, command = stop)
breakButton.pack(side=TOP, padx= 10)

#speed scale
scale = Scale(buttomFrame, from_ = 0, to=3, command=setSpeed, orient=HORIZONTAL)
scale.set(70)
scale.pack( side=LEFT, pady = 15)


statusbar = Label(root, text= " Status Bar: ", relief= SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill= X)


# call tkinter mainloop() to start process
root.mainloop()


root.geometry("380x380")

