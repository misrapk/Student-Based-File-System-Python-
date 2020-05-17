from tkinter import *
from tkinter import messagebox     #to provide popup message box
class Login:
    def __init__(self,root):
        self.root = root
        self.root.title("File based Record System")
        self.root.geometry("1350x700+0+0")

        F1=Frame(self.root,bd=10, relief=GROOVE)
        F1.place(x = 450, y=150,  height =400)

        #TODO: define variables
        self.user = StringVar()
        self.password=StringVar()

        title = Label (F1, text="Login Please", font =("times new roman", 30, "bold")).grid(row=0, columnspan =2, pady=20)  

        labelUserName= Label(F1, text="Username",font=("times new roman", 25, "bold")).grid(row=1, column=0, pady=10, padx=10)
        txtUser = Entry(F1, bd=7, relief = GROOVE,textvariable=self.user, width=25, font=("arial 15 bold")).grid(row=1, column=1,padx =10, pady=10)

        labelPass= Label(F1, text="Password", font=("times new roman", 25, "bold")).grid(row=2, column=0, pady=10, padx=10)
        txtPass = Entry(F1, bd=7, relief = GROOVE,show = "*",textvariable = self.password, width=25, font=("arial 15 bold")).grid(row=2, column=1,padx =10, pady=10)

        #button
        btnlog = Button(F1, text="Login", font ="arial 15 bold", bd =7, width =10, command=self.loginFunc).place(x=10,y=250)
        btnrest = Button(F1, text="Clear", font ="arial 15 bold", bd =7, width =10, command = self.clrFunc).place(x=170,y=250)
        btnExt = Button(F1, text="Exit", font ="arial 15 bold", bd =7, width =10, command = self.exitFunc).place(x=330,y=250)

    #for login functionality
    def loginFunc(self):
        if(self.user.get() =='Peeyush' and self.password.get() == "11111111"):
            messagebox.showinfo("Info", f"welcome {self.user.get()} and your password is : {self.password.get()}")
            self.root.destroy()
            import software
            software.FileApp()
        else:
            messagebox.showerror("OOOOPPSSSS!!!"," Its an error!! You are an UNKNOWN person")


    #for clear
    def clrFunc(self):
        self.user.set("")
        self.password.set("")

    #for exit
    def exitFunc(self):
        option = messagebox.askyesno("Exit", "Do you reaaly want to exit????")
        if option>0:
            self.root.destroy()


root = Tk()
ob = Login(root)
root.mainloop()