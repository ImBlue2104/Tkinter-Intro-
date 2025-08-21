from tkinter import Tk, Label, Button, Entry, Frame, Text, END
from datetime import date 

#creates window
root = Tk() 
root.title('Getting Started with widgets!')
root.geometry('400x300')
#Add widgets
#Add Label
lbl = Label(text = "Hey There!", fg="white", bg="#072F5F", height=1, width=3)

#Add Label for getting name as input from user
#Use ENtry Widget to create a text box for userto enter details
name_lbl = Label(text ="Full name", bg="#045dc9")
name_entry = Entry()

#function to display a Message
def display():

    #Read input given by the user
    name = name_entry.get()

    #Declaring a global variable
    global message
    message = "Welcome to the Application! \n Today's date is: "
    greet = "Hello"+name+"\n"

    #Display details in a text box
    # Specify where to add the detils inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

#Add a Text Widget to display information/messages
text_box = Text(height=3)

#Add buttn and give value as name of the function
#Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#4D7BDD", fg="white")

#Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

root.mainloop() #updates all changes