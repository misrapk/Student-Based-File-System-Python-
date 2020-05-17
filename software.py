from tkinter import*
from tkinter import ttk, messagebox
import time,os

class FileApp:
    def __init__(self):
        self.root=Tk()
        self.root.title("File Based Record System")
        self.root.geometry("1330x700+0+0")


        title=Label(self.root, text ="File Based Reord System",bd =10, 
        	relief=GROOVE, pady =10, font=("times new roman", 30,"bold")).pack(fill=X)
        studentFrame = Frame(self.root,bd=10, relief=GROOVE)
        studentFrame.place(x=20, y=100, height=450)

        stitle = Label(studentFrame, text='Student Details', 
        		font=("times new roman",30, "bold")).grid(row=0, columnspan=4, pady=20)


        # --------------ALL Variables---------------------
        self.sid=StringVar()
        self.name=StringVar()
        self.course=StringVar()
        self.address=StringVar()
        self.city=StringVar()
        self.contact=StringVar()
        self.date=StringVar()
        self.degree=StringVar()
        self.proof=StringVar()
        self.payment=StringVar()



        labelsid = Label(studentFrame, text='Std ID', 
        		font=("times new roman",20, "bold")).grid(row=1, column=0, padx=10)
        txtSid = Entry(studentFrame, bd=7,textvariable=self.sid,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=1, column=1, padx=10,pady=10)

        sPhone = Label(studentFrame, text='Contact No.', 
        		font=("times new roman",20, "bold")).grid(row=1, column=2, padx=10)
        txtsPhone = Entry(studentFrame, bd=7,textvariable=self.contact,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=1, column=3, padx=10,pady=10)

        sName = Label(studentFrame, text='Name', 
        		font=("times new roman",20, "bold")).grid(row=2, column=0, padx=10)
        txtsName = Entry(studentFrame, bd=7,textvariable=self.name,relief=GROOVE, width=20, 	
        		font="arial 15 bold").grid(row=2, column=1, padx=10,pady=10)

        sDOB = Label(studentFrame, text='D.O.B.(dd/mm/yyyy)', 
        		font=("times new roman",20, "bold")).grid(row=2, column=2, padx=10)
        txtSDOb = Entry(studentFrame, bd=7, textvariable=self.date,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=2, column=3, padx=10,pady=10)

        sCourse = Label(studentFrame, text='Course', 
        		font=("times new roman",20, "bold")).grid(row=3, column=0, padx=10)
        txtSCourse = Entry(studentFrame, bd=7,textvariable=self.course,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=3, column=1, padx=10,pady=10)

        
        saddress = Label(studentFrame, text='Address', 
        		font=("times new roman",20, "bold")).grid(row=4, column=0, padx=10)
        txtSaddress = Entry(studentFrame, bd=7, textvariable=self.address,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=4, column=1, padx=10,pady=10)

        sCity = Label(studentFrame, text='City',
        		font=("times new roman",20, "bold")).grid(row=5,column=0,padx=10,pady=20)
        txtcCity = Entry(studentFrame, bd=7,textvariable=self.city,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=5, column=1, padx=10,pady=10)

        sIDProof = Label(studentFrame, text='ID Proof', 
        		font=("times new roman",20, "bold")).grid(row=4, column=2, padx=10)
        sDegree = Label(studentFrame, text='Department', 
        		font=("times new roman",20, "bold")).grid(row=3, column=2, padx=10)
        sPaymentMode = Label(studentFrame, text='Payment Mode',
        		font=("times new roman",20, "bold")).grid(row=5, column=2, padx=10)


        #combo boxes
        degreeCombo = ttk.Combobox(studentFrame,textvariable=self.degree,width=20, state="readonly", font="arial 15 bold")
        degreeCombo['values'] =("BCA","MCA","B.Tech", "MBA", "HM")
        degreeCombo.grid(row=3,column=3,padx=10,pady=10)


        paymentCombo = ttk.Combobox(studentFrame,textvariable=self.payment,width=20, state="readonly", font="arial 15 bold")
        paymentCombo['values'] =("PayTM", "Google Pay", "PhonePay","UPI", "NEFT")
        paymentCombo.grid(row=5,column=3,padx=10,pady=10)

        proofCombo = ttk.Combobox(studentFrame,textvariable=self.proof,width=20, state="readonly", font="arial 15 bold")
        proofCombo['values'] =("aadhar Card","Voter ID", "Driving License", "College ID")
        proofCombo.grid(row=4,column=3,padx=10,pady=10)


        #creating buttons
        btnframe=Frame(self.root, bd=10, relief=GROOVE)
        btnframe.place(x=10,y=570)

        btnSave = Button(btnframe, text="Save", font = "arial 15 bold",
        		bd=7,width=18,  command=self.saveData).grid(row=0,column=0,padx=10,pady=10)
 
        btnDelete = Button(btnframe, text="Delete",command=self.delete, font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=1,padx=10,pady=10)
        btnClear = Button(btnframe, text="Clear",command=self.fClear, font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=2,padx=10,pady=10)
        btnLogout = Button(btnframe, text="Log Out",command = self.logout,font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=3,padx=10,pady=10)
        btnExit = Button(btnframe, text="Exit/Quit",command = self.exitFun,font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=4,padx=10,pady=10)



        #file frame
        fileFrame = Frame(self.root, bd=10, relief=GROOVE)
        fileFrame.place(x=970, y=100, width=340, height=450)

        fileTitle=Label(fileFrame, text="All Files",
         font = "arial 20 bold", bd=5, relief=GROOVE).pack(side=TOP , fill=X)

        #scroll bar
        scroll_y = Scrollbar(fileFrame, orient=VERTICAL)
        self.fileList=Listbox(fileFrame,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.fileList.yview)
        self.fileList.pack(fill=BOTH, expand=1)
        self.fileList.bind("<ButtonRelease-1>",self.getData)
        self.showFiles()
        self.root.mainloop()


    def saveData(self):
        present="no"
        if self.sid.get() =="":
            messagebox.showerror("Error","Student ID Must be required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    #split because 101.txt is file name
                    if i.split(".")[0]==self.sid.get():
                        present ="yes"
                if present =="yes":
                    ask = messagebox.askyesno("Update","File already present \nDo you really want to")
                    if ask>0:
                        self.saveFiles()
                        messagebox.showinfo("Update","Record has updated successfully.")
                        self.showFiles()
                        
                else:
                    self.saveFiles()
                    messagebox.showinfo("Saved","Record has saved successfully.")
                    self.showFiles()
            else:
                self.saveFiles()
                messagebox.showinfo("Saved","Record has saved successfully.")
                self.showFiles()
                
        

    #function to show the files
    def showFiles(self):
        files=os.listdir("files/")
        if(len(files)>0):
            self.fileList.delete(0,END);   #delete the previous list
            for i in files:
                self.fileList.insert(END,i)


    def getData(self,ev):
        getCursor=self.fileList.curselection()
        # print(self.fileList.get(getCursor))
        f1=open("files/"+self.fileList.get(getCursor))
        value=[]
        for f in f1:
            value=f.split(",")

        self.sid.set(value[0])
        self.name.set(value[1])
        self.course.set(value[2])
        self.address.set(value[3])
        self.city.set(value[4])
        self.contact.set(value[5])
        self.date.set(value[6])
        self.degree.set(value[7])
        self.proof.set(value[8])
        self.payment.set(value[9])




    def fClear(self):
        self.sid.set("")
        self.name.set("")
        self.course.set("")
        self.address.set("")
        self.city.set("")
        self.contact.set("")
        self.date.set("")
        self.degree.set("")
        self.proof.set("")
        self.payment.set("")


    def delete(self):
        present="no"
        if self.sid.get() =="":
            messagebox.showerror("Error","Student ID Must be required")
        else:
            f=os.listdir("files/")
            if len(f)>0:
                for i in f:
                    #split because 101.txt is file name
                    if i.split(".")[0]==self.sid.get():
                        present ="yes"
                if present =="yes":
                    ask = messagebox.askyesno("Delete","Do You want to confirm?")
                    if ask>0:
                        os.remove("files/" + self.sid.get()+".txt")
                        messagebox.showinfo("","Success!")
                        self.showFiles()

                    else:
                        messagebox.showerror("Error","File Not Found")


    def saveFiles(self):
        f=open("files/"+str(self.sid.get())+".txt","w")
        f.write(

                str(self.sid.get())+","+
                str(self.name.get())+","+
                str(self.course.get())+","+
                str(self.address.get())+","+
                str(self.city.get())+","+
                str(self.contact.get())+","+
                str(self.date.get())+","+
                str(self.degree.get())+","+
                str(self.proof.get())+","+
                str(self.payment.get())
                )

        f.close()
        self.showFiles()


    #for exit

    def exitFun(self):
        ask = messagebox.askyesno("Exit", "Do you really want to Exit?")
        if ask>0:
            self.root.destroy()

    #for logout
    def logout(self):
        self.root.destroy()
        import login


