from Maestro import Controller
# from tkinter import *
import time
import os
import socket
import threading
import Maestro

# don't forget this part
os.system('xset r on')

x = Maestro.Controller()

# print(x.getPosition(0))

# set all channels to neutral
for chan in range(len(x.Targets)):
    x.setTarget(chan, 6000)
    x.setAccel(chan, 20)



# Main Tk window instantiation
# root = Tk()
# root.title('Control GUI')



HOST = ''                 # Symbolic name meaning the local host
PORT = 9999              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)


# conn, addr = s.accept()
# print ('Connected by', addr)
# while 1:
#     data = conn.recv(1024)
#     if not data: break
#     print(data.decode("ascii"))
# conn.close()


# listen for connection
# Function to initiate the socket
def init_socket():
    while True:
        print('Listening')
        # listen for ip to accept on socket
        s_2, ip = s.accept()
        print('Got a connection from %s' % str(ip))
        # create thread that runs function receive using accepted socket
        rt = threading.Thread(target=receive(s_2))
        # start thread
        rt.start()


# listen for incoming messages
# Function to receive STT commands
def receive(s_2):
    while True:
        r = s_2.recv(1024)
        msg = r.decode('ascii')
        print('Received: ' + msg)
        if(msg == "forward"):
            forward()
        elif(msg == "back"):
            back()
        elif (msg == "left"):
            back()
        elif (msg == "right"):
            back()
        elif (msg == "stop"):
            stopFast()
        elif (msg == "speed1"):
            setSpeed(1)
        elif (msg == "speed2"):
            setSpeed(2)
        elif (msg == "speed3"):
            setSpeed(3)



## Insert control program code here ##


# Socket thread init
init_socket_thread = threading.Thread(target=init_socket)
init_socket_thread.start()

# Main tk loop and geometry
# root.geometry('800x450')
# root.mainloop()

global forwardSpeed
global backSpeed

forwardSpeed = 6250
backSpeed = 5750


def back():
    # print("pressed forward")
    x.setTarget(1, forwardSpeed)
    x.setTarget(3, forwardSpeed)
    x.setTarget(0, backSpeed)
    x.setTarget(2, backSpeed)


def forward():
    # print("pressed backwards")
    x.setTarget(1, backSpeed)
    x.setTarget(3, backSpeed)
    x.setTarget(0, forwardSpeed)
    x.setTarget(2, forwardSpeed)


def right():
    # print("pressed backwards")
    x.setTarget(1, forwardSpeed)
    x.setTarget(3, forwardSpeed)
    x.setTarget(0, forwardSpeed)
    x.setTarget(2, forwardSpeed)


def left():
    # print("pressed backwards")
    x.setTarget(1, backSpeed)
    x.setTarget(3, backSpeed)
    x.setTarget(0, backSpeed)
    x.setTarget(2, backSpeed)


def stop():
    # print("released key")
    for i in range(len(x.Targets)):
        x.setTarget(i, 6000)


def stopFast():
    for chan in range(len(x.Targets)):
        x.setAccel(chan, 0)
        x.setTarget(chan, 6000)

    for i in range(len(x.Targets)):
        x.setAccel(i, 20)


def setSpeed(char):
    global forwardSpeed
    global backSpeed
    if (char == '1'):
        forwardSpeed = 6300
        backSpeed = 5700
        print("speed set to low")
    if (char == '2'):
        forwardSpeed = 6400
        backSpeed = 5600
        print("speed set to med")
    if (char == '3'):
        forwardSpeed = 7000
        backSpeed = 5000
        print("speed set to high")

