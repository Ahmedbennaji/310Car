from tkinter import *
import socket
import threading

# Main Tk window instantiation
root = Tk()
root.title('Control GUI')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host = '10.200.0.112'
# hostCharter = '192.168.1.3'

connectCharter = '192.168.1.11'
connectMSU = '10.152.163.151'

port = 9999

s.connect((connectMSU, port))


def back():
    msg = "back"
    s.send(msg.encode('ascii'))


def forward():
    msg = "forward"
    s.send(msg.encode('ascii'))


def right():
    msg = "right"
    s.send(msg.encode('ascii'))


def left():
    msg = "left"
    s.send(msg.encode('ascii'))


def stop():
    msg = "stop"
    s.send(msg.encode('ascii'))


def stopFast():
    msg = "stopFast"
    s.send(msg.encode('ascii'))


def setSpeed(event):
    if (event.char == '1'):
        msg = "setSpeed1"
        s.send(msg.encode('ascii'))
    if (event.char == '2'):
        msg = "setSpeed2"
        s.send(msg.encode('ascii'))
    if (event.char == '3'):
        msg = "setSpeed3"
        s.send(msg.encode('ascii'))

def disconnect():
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

root.bind('<Esc>', disconnect)


# call tkinter mainloop() to start process
root.mainloop()