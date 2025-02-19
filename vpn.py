from tkinter import Tk, Frame, Button, Label, Entry, Checkbutton, IntVar, END, StringVar
import server
import client

def switchMode():
    #TODO: implement ui switching
    global inClientMode
    if 'client' in modeLabel["text"]:
        modeLabel.config(text = "VPN in server mode")
        hostDetails.config(state='disabled')
        nameOrIP.config(state='disabled')
        inClientMode = False
    else:
        modeLabel.config(text = "VPN in client mode")
        hostDetails.config(state='active')
        nameOrIP.config(state='active')
        inClientMode= True
    print('switching', inClientMode)

def connectStep():
    #TODO:
    print('step')

def connectSubmit():
    #TODO:
    print(inClientMode)
    
    if inClientMode:
        client.connectClient(int(ss_field.get()), hostField.get(), nameIPState.get(), int(portField.get()))
    else: 
        server.openServer(int(ss_field.get()), int(portField.get()))

    print(hostField.get(), nameIPState.get(), portField.get())

def sendData():
    #TODO:
    if inClientMode:
        print('send client')
    else:
        server.encryptAndSend(sendField.get())
    print(sendField.get())

def nextStep():
    #TODO:
    print('stepping')

def executeFull():
    #TODO:
    print('running')


# initialize GUI area
root = Tk()
root.title('Team AMAZ VPN')
frame = Frame(root, width=500)
frame.pack()
inClientMode = True

# create Toggle button
labelText="VPN in client mode"
toggleText="Toggle mode"
modeLabel = Label(root, text=labelText)
toggle_button = Button(root, text=toggleText, command=switchMode)

modeLabel.pack()
toggle_button.pack()

# connection details
connectInfo = Label(root, text='Enter host name/IP (client only) and port number')
hostDetails = Label(root, text='Host Name/IP')
hostField = Entry(root)
nameIPState = IntVar()
nameOrIP = Checkbutton(root, text='Check if submitting IP address', variable=nameIPState)
portLabel = Label(root, text='Enter port number:')
portField = Entry(root)

connectInfo.pack()
hostDetails.pack()
hostField.pack()
nameOrIP.pack()
portLabel.pack()
portField.pack()

# shared secret field
ss_label = Label(root, text="Shared Secret Values: ")
ss_field = Entry(root)

ss_label.pack()
ss_field.pack()

# submit connection details
connectStep = Button(root, text='Step Through Connection', command=connectStep)
connectSubmit = Button(root, text='Submit Connection Details', command=connectSubmit)

connectStep.pack()
connectSubmit.pack()

# data to send
sendLabel = Label(root, text="Data to send: ")
sendField = Entry(root)

sendLabel.pack()
sendField.pack()

# received data
recLabel = Label(root, text="Received data: ")
recText = StringVar()
recData = Entry(root, textvariable=recText)

recLabel.pack()
recData.pack()

# Continue button
continueButton = Button(root, text='Step Through Send', command=nextStep)
continueButton.pack()

# Automatic Run
runButton = Button(root, text='Send Automatically', command=executeFull)
runButton.pack()

# program status
statusText = StringVar()
statusText.set('program state')
status = Label(root, textvariable=statusText)
status.pack()

root.mainloop()
