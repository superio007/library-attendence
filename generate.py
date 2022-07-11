import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
from tkinter import*

class Qr_Generator:
    def __init__(self,root):
       self.root=root
       self.root.geometry("900x500+200+50")
       self.root.title("QR Generator")
       self.root.resizable(False,False)

       title=Label(self.root,text="   Qr Code Generator ",font=("times new roman",40),bg='#000066',fg='#ffffff',anchor='w').place(x=0,y=0,relwidth=1)

       #======Student details window ==========
       #==== variable========
       self.var_stu_code=StringVar()
       self.var_Name=StringVar()
       self.var_Deparment=StringVar()
       self.var_DIV=StringVar()

       stu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='White')
       stu_Frame.place(x=50,y=100,width=500,height=380)

       title=Label(stu_Frame,text="Students Details ",font=("goudy old style",20),bg='#000066',fg='#ffffff').place(x=0,y=0,relwidth=1)

       lbl_stu_code=Label(stu_Frame,text="Students ID *",font=("times new romen",15,'bold'),bg='#ffffff').place(x=20,y=60)

       lbl_stu_code=Label(stu_Frame,text="Student Name *",font=("times new romen",15,'bold'),bg='#ffffff').place(x=20,y=100)

       lbl_stu_code=Label(stu_Frame,text="Deparment* ",font=("times new romen",15,'bold'),bg='#ffffff').place(x=20,y=140)

       lbl_stu_code=Label(stu_Frame,text="Div* ",font=("times new romen",15,'bold'),bg='#ffffff').place(x=20,y=180)

       txt_stu_code=Entry(stu_Frame,text="StudentID",textvariable=self.var_stu_code,font=("times new romen",15,),bg='#ffffcc').place(x=200,y=60)

       txt_Name=Entry(stu_Frame,text="StudentName",textvariable=self.var_Name,font=("times new romen",15),bg='#ffffcc').place(x=200,y=100)

       txt_Deparment=Entry(stu_Frame,text="Deparment",textvariable=self.var_Deparment,font=("times new romen",15),bg='#ffffcc').place(x=200,y=140)

       txt_DIV=Entry(stu_Frame,text="DIV",textvariable=self.var_DIV,font=("times new romen",15),bg='#ffffcc').place(x=200,y=180)


       btn_generate=Button(stu_Frame,text='QR Generate',command=self.generate,font=('times new roman',18,'bold'),bg='#66ccff',fg='#ffffff').place(x=90,y=250,width=180,height=30)

       btn_Clear=Button(stu_Frame,text='Clear',command=self.clear,font=('times new roman',18,'bold'),bg='#666699',fg='#ffffff').place(x=280,y=250,width=120,height=30)

       self.msg=''
       self.lbl_msg=Label(stu_Frame,text=self.msg,font=("times new romen",20,),bg='#ffffff',fg='#66ff33')
       self.lbl_msg.place(x=0,y=320,relwidth=1)

        #======Qr Code  window ==========
       qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='White')
       qr_Frame.place(x=600,y=100,width=250,height=380)

       stu_title=Label(qr_Frame,text="Students QR Code ",font=("goudy old style",20),bg='#000066',fg='#ffffff').place(x=0,y=0,relwidth=1)

       self.qr_code=Label(qr_Frame,text='No QR\n Avaliable',font=('times new romen',15),bg='#000066',fg='#ffffff',bd=1,relief=RIDGE) 
       self.qr_code.place(x=35,y=100,width=180,height='180')
    def clear(self):
       self.var_stu_code.set('')
       self.var_Name.set('')
       self.var_Deparment.set('')
       self.var_DIV.set('')

       self.msg=''
       self.lbl_msg.config(text=self.msg,)
    def generate(self):
       if self.var_DIV.get()=='' or self.var_Deparment.get()=='' or self.var_Name.get()=='' or self.var_stu_code.get()=='':
            self.msg='All Fields are Required!!!!'
            self.lbl_msg.config(text=self.msg,fg='#ff3300')
       else:
            qr_data=(self.var_stu_code.get(), self.var_Name.get(),self.var_Deparment.get(),self.var_DIV.get())
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Students_QR/STU_"+str(self.var_Name.get())+'.png')
            #======Qr code image update========
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)
            #======updating notification
            self.msg='QR Generated Sucessfully!!!!'
            self.lbl_msg.config(text=self.msg,fg='#66ff33')

root=Tk()
obj = Qr_Generator(root)
root.mainloop()