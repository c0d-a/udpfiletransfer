import socket                                                          #module to establish connection
import tkinter as tk

def transmitFile(hostAddress, fileName):
    #function to transmit the file. Contains the code copy/pasted from phase1
    #takes as input the host address to send the file to and the name for the file upon arrival

    socketVar = socket.socket()  # initialization of the socket object
    port = 8090  # set client port to 8090
    socketVar.connect((hostAddress, port))  # connect to host address

    file = open(fileName, 'wb')  # open file in write-binary
    data = socketVar.recv(500000)  # read the data from the file
    file.write(data)  # write the data into a new file
    file.close()

    return

def sendFile(event):
    #event to send the file once the user has clicked the "Send file" button
    window.quit()
    # transmitFile(hostAddress, fileName)

    return


#Get the name of this machine to use as a default address
defaultServerName = socket.gethostname()

window = tk.Tk()

#introductory message
lbl_introduction = tk.Label(text = "Networking Design Project Phase 2. \n"
                             "EECE.4830 201. Professor Vokkarane. \n"
                             "By: Julie Dawley, Ricardo Candanedo, and Mohammad Musawer \n \n"
                             "Destination Computer: Defaults to this machine. \n"
                             "Change to the address in serverClient if running client and server on seperate machines")
lbl_introduction.pack()

#Get the destination name from the user, default to defaultServerName
ent_destination = tk.Entry()
ent_destination.pack()
ent_destination.insert(0,defaultServerName)
hostAddress = ent_destination.get()

#get the file name from the user. Default to receivedFile.jpg
lbl_getFileName = tk.Label(text = "\n Enter the name the file should have at the destination")
ent_fileName = tk.Entry()
lbl_getFileName.pack()
ent_fileName.pack()
ent_fileName.insert(0,"receivedFile.jpg")
fileName =  ent_fileName.get()

btn_confirmEntry = tk.Button(text = "Transmit File", height = 2, width = 10)
btn_confirmEntry.pack()
btn_confirmEntry.bind('<Button-1>', sendFile)


window.mainloop()