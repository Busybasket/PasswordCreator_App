from tkinter import *
import random
Font_Button = ("Arial",8,)
Font_Text = ("Arial Black",20)
Font_Text2 = ("Arial",15)
padx_main = 80
pady_main = 400
padx2 = 400
pady2 = 400

root = Tk()
root.geometry("1280x720")
root.attributes("-fullscreen",True)
#root.iconbitmap('Your Icon')
root.configure(bg="#bdbdbd")
def Menu(): #Creating Password Menu
    C_Password_Label = Label(frame,text="Create a Password",font=Font_Text)
    C_Password_Label.place(relx=0.5,rely=-2.8,anchor=CENTER)
    C_Password_Title = Label(frame,text="Your Password Title :",font=Font_Text2)
    C_Password_Title.place(relx=0.2,rely=-1.8,anchor=CENTER)
    C_Password_Title_Input = Entry(frame)
    C_Password_Title_Input.place(relx=0.317,rely=-1.8)
    C_Password = Label(frame,text="Password :",font=Font_Text2)
    C_Password.place(relx=0.247,rely=-0.8,anchor=CENTER)
    C_Password_Input = Entry(frame)
    C_Password_Input.place(relx=0.38,rely=-0.8,anchor=CENTER)
    C_Password_Submit = Button(frame,text="Submit",command=lambda: Click_Submit(C_Password_Title_Input.get(),C_Password_Input.get()))
    C_Password_Submit.place(relx=0.5,rely=0.5,anchor=CENTER,)
def Menu2(): #Listing Password Menu
    M_Title_Label = Label(frame,text="Title ",font=Font_Text)
    M_Title_Label.place(relx=0.3,rely=-2.5,anchor=CENTER)
    M_Password_Label = Label(frame,text="Password",font=Font_Text)
    M_Password_Label.place(relx=0.7,rely=-2.5,anchor=CENTER)
    with open("passwords.txt","r") as dosya:
        output1 = dosya.readline()
        output2 = dosya.readline()
        output3 = dosya.readline()
        

    M_Label1 = Label(frame,text=output1,font=Font_Text2)
    M_Label1.place(relx=0.5,rely=-1.8,anchor=CENTER)
    M_Label2 = Label(frame,text=output2,font=Font_Text2)
    M_Label2.place(relx=0.5,rely=-1.3,anchor=CENTER)
    M_Label3 = Label(frame,text=output3,font=Font_Text2)
    M_Label3.place(relx=0.5,rely=-0.8,anchor=CENTER)  

def Click_Submit(Title_input,Password_input):  #when clicked submit
    dosya = open("passwords.txt","a",encoding="utf-8")
    pLetters = []
    for i in range(0,len(Password_input)):
        pLetters.append(Password_input[i])
    random.shuffle(pLetters)
    i = 0
    fLetter = pLetters[0]
    while i+1 != len(pLetters):
        newPassword = fLetter + pLetters[i+1]
        i = i + 1
        fLetter = newPassword
    print("New Password : "+fLetter)
    dosya.write(Title_input+"                                                        "+fLetter+"\n")
    dosya.close()
    s_Submit = Label(frame,text=Title_input + " saved Succesfully",font=Font_Text2)
    s_Submit.place(relx=0.5,rely=0.2,anchor=CENTER,)
    
    
def C_Password_F():
    if C_Password_Button['state'] == NORMAL:  #Disabling-Enabling Button 
        C_Password_Button['state'] = DISABLED
        C_Password_Button['bg'] = "white"
        if L_Password_Button['state'] == DISABLED:
            L_Password_Button['state'] = NORMAL
            L_Password_Button['bg'] = "#333333"
    for widget in frame.winfo_children():
        widget.destroy()
    Menu()

def L_Password_F():
    if L_Password_Button['state'] == NORMAL:  #Disabling-Enabling Button
        L_Password_Button['state'] = DISABLED
        L_Password_Button['bg'] = "white"
        if C_Password_Button['state'] == DISABLED:
            C_Password_Button['state'] = NORMAL
            C_Password_Button['bg'] = "#333333"    
    for widget in frame.winfo_children():
        widget.destroy()
    Menu2()

frame = LabelFrame(root,padx=padx_main,pady=pady_main)
frame.place(relx=0.5,rely=0.5,anchor = CENTER)
Menu_text = Label(frame, text="Welcome!\nthis is an application that generates and stores password for you",font = Font_Text)
Menu_text.pack(padx=10,pady=10)
C_Password_Button = Button(root, text="Create a password",padx=50,pady=120,command=C_Password_F,fg="white",bg="#333333",borderwidth="5")
C_Password_Button.place(relx = 0.05, rely = 0.32 ,anchor = CENTER)
L_Password_Button = Button(root, text="Your password list",padx=50,pady=120,command=L_Password_F,fg="white",bg="#333333",borderwidth="5")
L_Password_Button.place(relx = 0.05, rely = 0.65 ,anchor = CENTER)
C_Password_Button.configure(font = Font_Button)
L_Password_Button.configure(font = Font_Button)
root.mainloop()
