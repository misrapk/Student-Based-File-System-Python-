from tkinter import*
from tkinter import ttk, messagebox
import time,os

class FileApp:
    def __init__(self,root):
        self.root=root
        self.root.title("File Based Record System")
        self.root.geometry("1330x700+0+0")


        title=Label(self.root, text ="File Based Reord System",bd =10, 
        	relief=GROOVE, pady =10, font=("times new roman", 30,"bold")).pack(fill=X)
        studentFrame = Frame(self.root,bd=10, relief=GROOVE)
        studentFrame.place(x=20, y=100, height=450)

        stitle = Label(studentFrame, text='Student Details', 
        		font=("times new roman",30, "bold")).grid(row=0, columnspan=4, pady=20)

        sid = Label(studentFrame, text='Std ID', 
        		font=("times new roman",28, "bold")).grid(row=1, column=0, padx=10)
        txtSid = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=1, column=1, padx=10,pady=10)

        sPhone = Label(studentFrame, text='Contact No.', 
        		font=("times new roman",20, "bold")).grid(row=1, column=2, padx=10)
        txtsPhone = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=1, column=3, padx=10,pady=10)

        sName = Label(studentFrame, text='Name', 
        		font=("times new roman",20, "bold")).grid(row=2, column=0, padx=10)
        txtsName = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 	
        		font="arial 15 bold").grid(row=2, column=1, padx=10,pady=10)

        sDOB = Label(studentFrame, text='D.O.B.(dd/mm/yyyy)', 
        		font=("times new roman",20, "bold")).grid(row=2, column=2, padx=10)
        txtSDOb = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=2, column=3, padx=10,pady=10)

        sCourse = Label(studentFrame, text='Course', 
        		font=("times new roman",20, "bold")).grid(row=3, column=0, padx=10)
        txtSCourse = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=3, column=1, padx=10,pady=10)

        
        saddress = Label(studentFrame, text='Address', 
        		font=("times new roman",20, "bold")).grid(row=4, column=0, padx=10)
        txtSaddress = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=4, column=1, padx=10,pady=10)

        sCity = Label(studentFrame, text='City',
        		font=("times new roman",20, "bold")).grid(row=5,column=0,padx=10,pady=20)
        txtcCity = Entry(studentFrame, bd=7,relief=GROOVE, width=20, 
        		font="arial 15 bold").grid(row=5, column=1, padx=10,pady=10)

        sIDProof = Label(studentFrame, text='ID Proof', 
        		font=("times new roman",20, "bold")).grid(row=4, column=2, padx=10)
        sDegree = Label(studentFrame, text='Department', 
        		font=("times new roman",20, "bold")).grid(row=3, column=2, padx=10)
        sPaymentMode = Label(studentFrame, text='Payment Mode',
        		font=("times new roman",20, "bold")).grid(row=5, column=2, padx=10)


        #combo boxes
        degreeCombo = ttk.Combobox(studentFrame,width=20, state="readonly", font="arial 15 bold")
        degreeCombo['values'] =("BCA","MCA","B.Tech", "MBA", "HM")
        degreeCombo.grid(row=3,column=3,padx=10,pady=10)


        paymentCombo = ttk.Combobox(studentFrame,width=20, state="readonly", font="arial 15 bold")
        paymentCombo['values'] =("PayTM", "G Pay", "PhonePay","UPI", "NEFT")
        paymentCombo.grid(row=5,column=3,padx=10,pady=10)

        proofCombo = ttk.Combobox(studentFrame,width=20, state="readonly", font="arial 15 bold")
        proofCombo['values'] =("aadhar Card","Voter ID", "Driving License", "College ID")
        proofCombo.grid(row=4,column=3,padx=10,pady=10)


        #creating buttons
        btnframe=Frame(self.root, bd=10, relief=GROOVE)
        btnframe.place(x=10,y=570)

        btnSave = Button(btnframe, text="Save", font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=0,padx=10,pady=10)

        btnDelete = Button(btnframe, text="Delete", font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=1,padx=10,pady=10)
        btnClear = Button(btnframe, text="Clear", font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=2,padx=10,pady=10)
        btnLogout = Button(btnframe, text="Log Out", font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=3,padx=10,pady=10)
        btnExit = Button(btnframe, text="Exit/Quit", font = "arial 15 bold",
        		bd=7,width=18).grid(row=0,column=4,padx=10,pady=10)



        #file frame
        fileFrame = Frame(self.root, bd=10, relief=GROOVE)
        fileFrame.place(x=970, y=100, width=340, height=450)

        fileTitle=Label(fileFrame, text="All Files",
         font = "arial 20 bold", bd=5, relief=GROOVE).pack(side=TOP , fill=X)




root=Tk()
ob=FileApp(root)
root.mainloop()