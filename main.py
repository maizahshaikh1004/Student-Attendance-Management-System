from tkinter import *
from tkinter import messagebox
#Python Imaging Library
from PIL import Image,ImageTk,ImageDraw,ImageFont,ImageGrab
from tkinter.filedialog import askopenfilename,asksaveasfilename
import re
import random
import subprocess
window=Tk()
window.geometry("1250x700")
window.title("Student Attendance Management System")
bgcolor="dark blue"

locked_icon=PhotoImage(file='locked.png')
unlocked_icon=PhotoImage(file='unlocked.png')
#pink logo student login
studloginpic=PhotoImage(file='tran2.png')
# Load the image
studloginpic= Image.open('tran2.png')
# Resize the image
studloginpic=studloginpic.resize((130, 130))
# Convert the image to a Tkinter-compatible photo image
studloginpic_conv= ImageTk.PhotoImage(studloginpic)
#pink logo teacher
teacherloginpic=PhotoImage(file="teacher.png")
# Load the image
teacherloginpic= Image.open("teacher.png")
# Resize the image
teacherloginpic=teacherloginpic.resize((110, 110))
# Convert the image to a Tkinter-compatible photo image
teacherloginpic_conv= ImageTk.PhotoImage(teacherloginpic)
#pink logo
addaccntpic=PhotoImage(file="add.png")
# Load the image
addaccntpic= Image.open("add.png")
# Resize the image
addaccntpic=addaccntpic.resize((110,110))
# Convert the image to a Tkinter-compatible photo image
addaccntpic_conv= ImageTk.PhotoImage(addaccntpic)
mypic=PhotoImage(file="clg_bg_3.png")
# Load the image
mypic= Image.open("clg_bg_3.png")
# Resize the image
mypic=mypic.resize((900, 900))
# Convert the image to a Tkinter-compatible photo image
mypic_conv= ImageTk.PhotoImage(mypic)
studfm_pic=PhotoImage(file="2.png")
# Load the image
studfm_pic= Image.open("2.png")
# Resize the image
studfm_pic=studfm_pic.resize((900, 900))
# Convert the image to a Tkinter-compatible photo image
studfm_pic_conv= ImageTk.PhotoImage(studfm_pic)
teacherfm_pic=PhotoImage(file='14.png')
# Load the image
teacherfm_pic= Image.open('14.png')
# Resize the image
teacherfm_pic=teacherfm_pic.resize((900, 900))
# Convert the image to a Tkinter-compatible photo image
teacherfm_pic_conv= ImageTk.PhotoImage(teacherfm_pic)
addacntfm_pic=PhotoImage(file='addacnt2.png')
# Load the image
addacntfm_pic= Image.open('addacnt2.png')
# Resize the image
addacntfm_pic=addacntfm_pic.resize((900, 900))
# Convert the image to a Tkinter-compatible photo image
addacntfm_pic_conv= ImageTk.PhotoImage(addacntfm_pic)
genidfm_pic=PhotoImage(file='addacnt2.png')
# Load the image
genidfm_pic= Image.open('addacnt2.png')
# Resize the image
genidfm_pic=genidfm_pic.resize((540, 590))
# Convert the image to a Tkinter-compatible photo image
genidfm_pic_conv= ImageTk.PhotoImage(genidfm_pic)    
def confirm(message):
    answer=BooleanVar()
    answer.set(False)
    def action(ans):
        answer.set(ans)
        confirmbox.destroy()
    confirmbox=Frame(window,highlightbackground='dark goldenrod',highlightthickness=3,bg='misty rose')
    confirmbox.place(x=460,y=120,width=320,height=220)
    message=Label(confirmbox,text=message,font=('Times New Roman',18,'bold'),bg='misty rose',fg='dark goldenrod')
    message.pack(pady=20)
    cancel=Button(confirmbox,text='Cancel',font=('bold',15),bd=3,activebackground='saddle brown',activeforeground='misty rose',bg='saddle brown',fg='misty rose',command=lambda: action(False))
    cancel.place(x=50,y=160)
    yes=Button(confirmbox,text='Yes',font=('bold',15),bd=3,activebackground='saddle brown',activeforeground='misty rose',bg='saddle brown',fg='misty rose',command=lambda: action(True))
    yes.place(x=190,y=160,width=80)
    window.wait_window(confirmbox)
    return answer.get()
def message_box(message):
    message_fm=Frame(window,highlightbackground=bgcolor,highlightthickness=3)
    close=Button(message_fm,text='X',bd=2,font=('bold',13),fg=bgcolor,command=lambda:message_fm.destroy())
    close.place(x=290,y=5)
    message_lb=Label(message_fm,text=message,font=('bold',15))
    message_lb.pack(pady=50)
    message_fm.place(x=460,y=120,width=330,height=230)
def genidclicked(data):
    studcardfm=Frame(window,highlightbackground='dark goldenrod',highlightthickness=3)
    studcardfm.place(x=40,y=40,width=550,height=600)
    studcard_lbl=Label(studcardfm,image=genidfm_pic_conv)
    studcard_lbl.place(x=0,y=0)
    head=Label(studcardfm,text="Student Identity Card",bg='misty rose',fg='dark goldenrod',
               font=('Times New Roman',18,'bold'))
    head.place(x=0,y=0,width=540,height=40)
    main_label="""
Student_Id:

Student Full Name:

Gender:

Age:

Class:

Phone Number:

Email Address:
"""
    label=Label(studcardfm,bg='misty rose',fg='dark goldenrod',text=main_label,font=('Times New Roman',15,'bold'),justify=LEFT)
    label.place(x=50,y=160,width=200)
    closebtn=Button(studcardfm,text='X',font=('Times New Roman',15,'bold'),bg='misty rose',fg='dark goldenrod',
               bd=0,activebackground='misty rose',activeforeground='dark goldenrod',command=lambda: studcardfm.destroy())
    closebtn.place(x=470,y=4)
    labels=Label(studcardfm,text=data,bg='misty rose',fg='dark goldenrod',font=('Times New Roman',15),justify=LEFT)
    labels.place(x=250,y=160,width=240,height=351)
    gen_pic_path=StringVar()
    def open_gen_pic():
        global genimgpath
        genimgpath=askopenfilename()
        if genimgpath:
            genimg=ImageTk.PhotoImage(Image.open(genimgpath).resize((100,100)))
            gen_pic_path.set(genimgpath)
            gen_picbtn.config(image=genimg)
            gen_picbtn.image=genimg
    gen_picbtn=Button(studcardfm,text="Generate\nImage",font=('Times New Roman',15,'bold'),command=open_gen_pic,bg='saddle brown',fg='misty rose',
                      activebackground='saddle brown',activeforeground='misty rose')
    gen_picbtn.place(x=50,y=50,width=100,height=100)
    def save_id():
    # Create a new Tk root window for the dialog
        root = Tk()
        root.withdraw()
        # Prompt the user for a filename
        filename = asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG image", "*.png"), ("All files", "*.*")],
            initialfile="Untitled.png"
        )
        # Check if the user clicked "Cancel"
        if filename:
            # Get the frame's position and size
            x = studcardfm.winfo_rootx()
            y = studcardfm.winfo_rooty()
            w = studcardfm.winfo_width()
            h = studcardfm.winfo_height()
            # Capture the frame as an image
            im = ImageGrab.grab((50,100, 50+716, 100+901))
            # Save the image to the specified filename
            im.save(filename)
        # Destroy the root window
        root.destroy()
    savebtn=Button(studcardfm,text="Save Student\nId Card",bg='saddle brown',fg='misty rose',
                   font=('bold',15),bd=1,command=save_id,activebackground='saddle brown',activeforeground='misty rose')
    savebtn.place(x=200,y=520)    
def welcome():
    def frwd_to_stud():
        welcome_frame.destroy()
        window.update()
        student_login()
    def frwd_to_teacher():
        welcome_frame.destroy()
        window.update()
        teacher_login()
    def frwd_to_add_accountpage():
        welcome_frame.destroy()
        window.update()
        add_accountpage()
    front_img_lbl.destroy()
    window.config(bg='papaya whip')
    welcome_frame=Frame(window,highlightbackground='dark goldenrod',highlightthickness=2)
    my_img_lbl=Label(welcome_frame,image=mypic_conv)
    my_img_lbl.place(x=0,y=0)
    heading_label=Label(welcome_frame,text="Welcome to\nAttendance Management System", bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    heading_label.place(x=0,y=0,width=740)
    stud_login_btn=Button(welcome_frame,text="Student Login", bg="light salmon2",fg="saddle brown", font=('Times New Roman',20,'bold'),bd=0,command=frwd_to_stud)
    stud_login_btn.place(x=350,y=135,width=205,height=60)
    stud_login_pic_btn=Button(welcome_frame,image=studloginpic_conv,bd=0,command=frwd_to_stud)
    stud_login_pic_btn.place(x=150,y=100)
    teach_login_btn=Button(welcome_frame,text="Teacher Login", bg="light salmon2",fg="saddle brown", font=("Times New Roman",20,'bold'),bd=0,command=frwd_to_teacher)
    teach_login_btn.place(x=350,y=280,width=205,height=60)
    teach_login_pic_btn=Button(welcome_frame,image=teacherloginpic_conv,bd=0,command=frwd_to_teacher)
    teach_login_pic_btn.place(x=160,y=260,width=100,height=100)
    add_btn=Button(welcome_frame,text="Create Account",bg="light salmon2",fg="saddle brown", font=("Times New Roman",20,'bold'),bd=0,command=frwd_to_add_accountpage)
    add_btn.place(x=350,y=430,width=205,height=60)
    add_pic_btn=Button(welcome_frame,image=addaccntpic_conv,bd=0,command=frwd_to_add_accountpage)
    add_pic_btn.place(x=160,y=400)
    welcome_frame.place(x=260,y=0)
    welcome_frame.pack_propagate(False)
    welcome_frame.configure(width=740,height=900)
def student_login():
    def show_pswd():
        if pswd_ent["show"]=="•":
            pswd_ent.config(show="")
            show_hidebtn.config(image=unlocked_icon)
        else:
            pswd_ent.config(show="•")
            show_hidebtn.config(image=locked_icon)
    def frwd_to_welcome():
        stud_loginframe.destroy()
        window.update()
        welcome() 
    stud_loginframe=Frame(window,highlightbackground='dark goldenrod',highlightthickness=2)
    stud_loginframe.place(x=260,y=0)
    stud_loginframe.pack_propagate(False)
    stud_loginframe.configure(width=740,height=900)
    studfm_pic_lbl=Label(stud_loginframe,image=studfm_pic_conv)
    studfm_pic_lbl.place(x=0,y=0)
    heading_label=Label(stud_loginframe,text="Student Login Page",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    heading_label.place(x=0,y=0,width=740,height=60)
    back_btn=Button(stud_loginframe,text="←",bg='papaya whip',fg="dark goldenrod",font=("bold",30),command=frwd_to_welcome,bd=0)
    back_btn.place(x=5,y=70)
    id_lb=Label(stud_loginframe,text="Enter Student ID:",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    id_lb.place(x=260,y=130)
    id_ent=Entry(stud_loginframe,font=("bold",18),justify=CENTER,highlightcolor="saddle brown",highlightbackground="gray",highlightthickness=3)
    id_ent.place(x=280,y=230,width=220,height=50)
    pswd_lb=Label(stud_loginframe,text="Enter Your Password:",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    pswd_lb.place(x=235,y=330)
    pswd_ent=Entry(stud_loginframe,font=("bold",18),justify=CENTER,highlightcolor="saddle brown",highlightbackground="gray",highlightthickness=3,show="•")
    pswd_ent.place(x=277,y=420,width=220,height=50)
    show_hidebtn=Button(stud_loginframe,image=locked_icon,bd=0,fg=bgcolor,command=show_pswd)
    show_hidebtn.place(x=530,y=420,width=40,height=50)
    def chk_student():
        if (id_ent.get()=='1'or id_ent.get()=='2' or id_ent.get()=='3'or id_ent.get()=='4' or id_ent.get()=='5' or
        id_ent.get()=='6' or id_ent.get()=='7' or id_ent.get()=='8' or id_ent.get()=='9' or id_ent.get()=='10' or
        id_ent.get()=='11' or id_ent.get()=='12' or id_ent.get()=='13' or id_ent.get()=='14' or id_ent.get()=='15' or
        id_ent.get()=='16' or id_ent.get()=='17' or id_ent.get()=='18' or id_ent.get()=='19' or id_ent.get()=='20')and (pswd_ent.get()=='one' or pswd_ent.get()=='two'or pswd_ent.get()=='three' or pswd_ent.get()=='four' or pswd_ent.get()=='five' or
         pswd_ent.get()=='six' or pswd_ent.get()=='seven' or pswd_ent.get()=='eight' or pswd_ent.get()=='nine' or pswd_ent.get()=='ten' or
         pswd_ent.get()=='eleven' or pswd_ent.get()=='twelve' or pswd_ent.get()=='thirteen' or pswd_ent.get()=='fourteen' or pswd_ent.get()=='fifteen' or
         pswd_ent.get()=='sixteen' or pswd_ent.get()=='seventeen' or pswd_ent.get()=='eighteen' or pswd_ent.get()=='nineteen' or pswd_ent.get()=='twenty' ):
            messagebox.showinfo('Success','Log In Successful As Student')
            if id_ent.get()=='1' and pswd_ent.get()=='one':
                file1=open('Student Id 1.txt','r')
                for all in file1:
                    print(all)
            elif id_ent.get()=='2' and pswd_ent.get()=='two':
                file1=open('Student Id 2.txt','r')
                for all in file1:
                    print(all)
            elif id_ent.get()=='3' and pswd_ent.get()=='three':
                file1=open('Student Id 3.txt','r')
                for all in file1:
                    print(all)
            else:
                print("No file for this student")
        else:
            messagebox.showerror('Failed','Please Enter Correct Credentials')
    login_btn=Button(stud_loginframe,text="Login",bg='papaya whip',fg="dark goldenrod", font=("Times New Roman",25,'bold'),bd=0, command=chk_student)
    login_btn.place(x=275,y=530,width=215,height=80)
def teacher_login(): 
    def show_pswd():
            if pswd_ent["show"]=="•":
                pswd_ent.config(show="")
                show_hidebtn.config(image=unlocked_icon)
            else:
                pswd_ent.config(show="•")
                show_hidebtn.config(image=locked_icon)
    def frwd_to_welcome():
        teacher_loginframe.destroy()
        window.update()
        welcome()
    teacher_loginframe=Frame(window,highlightbackground='dark goldenrod',highlightthickness=2)
    teacher_loginframe.place(x=260,y=0)
    teacher_loginframe.pack_propagate(False)
    teacher_loginframe.configure(width=740,height=900)
    teacherfm_pic_lbl=Label(teacher_loginframe,image=teacherfm_pic_conv)
    teacherfm_pic_lbl.place(x=0,y=0)
    heading_label=Label(teacher_loginframe,text="Teacher Login Page",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    heading_label.place(x=0,y=0,width=740,height=60)
    back_btn=Button(teacher_loginframe,text="←",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',30,'bold'),bd=0,command=frwd_to_welcome)
    back_btn.place(x=5,y=70)
    username_lb=Label(teacher_loginframe,text="Enter Your Username:",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    username_lb.place(x=260,y=130)
    username_ent=Entry(teacher_loginframe,font=("bold",18),justify=CENTER,highlightcolor="saddle brown",highlightbackground="gray",highlightthickness=3)
    username_ent.place(x=280,y=230,width=220,height=50)
    pswd_lb=Label(teacher_loginframe,text="Enter Your Password:",bg='papaya whip',fg="dark goldenrod",font=('Times New Roman',25,'bold'))
    pswd_lb.place(x=235,y=330)
    pswd_ent=Entry(teacher_loginframe,font=("bold",18),justify=CENTER,highlightcolor="saddle brown",highlightbackground="gray",highlightthickness=3,show="•")
    pswd_ent.place(x=277,y=420,width=220,height=50)
    show_hidebtn=Button(teacher_loginframe,image=locked_icon,bd=0,fg=bgcolor,command=show_pswd)
    show_hidebtn.place(x=530,y=420,width=40,height=50)
    def chk_admin():
        if username_ent.get()=='Admin' and pswd_ent.get()=='786':
            messagebox.showinfo('Success','Log In Successful As Teacher')            
            file_path=input("Enter the name of the text file you want to open : ")
            def open_notepad(file_path):
                subprocess.run(['notepad.exe',file_path])
            open_notepad(file_path)
        else:
            messagebox.showerror('Failed','Please Enter Correct Credentials')   
    login_btn=Button(teacher_loginframe,text="Login",bg='papaya whip',fg="dark goldenrod",bd=0, font=("Times New Roman",25,'bold'),command=chk_admin)
    login_btn.place(x=275,y=530,width=215,height=80)        
student_gender=StringVar()
def add_accountpage():
    global pic_path,window,Canvas
    pic_path=StringVar()
    def open_pic():
        global path
        path=askopenfilename()
        if path:
            img=ImageTk.PhotoImage(Image.open(path).resize((100,100)))
            pic_path.set(path)
            add_picbtn.config(image=img)
            add_picbtn.image=img   
    def frwd_to_welcome():
        ans=confirm(message='Do You Want To Leave\nRegistration Form?')
        if ans:
            add_frame.destroy()
            window.update()
            welcome()
    def remove_warning(entry):
        if entry['highlightbackground']!='gray':
            if entry.get()!='':
                entry.config(highlightbackground='gray',highlightcolor=bgcolor)
    def chk_invmail(email):
        pattern="^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"
        match=re.match(pattern=pattern,string=email)
        return match
    def generate_id():
        gen_id=''
        for r in range(6):
            gen_id+=str(random.randint(0,9))
        print("Gen_id number is: ",gen_id)
        stud_ident.config(state=NORMAL)
        stud_ident.delete(0,END)
        stud_ident.insert(END,gen_id)
        stud_ident.config(state='readonly')
    def chk_valid():
        if stud_nameent.get()=='':
            stud_nameent.config(highlightbackground='red',highlightcolor='red')
            stud_nameent.focus()
            messagebox.showerror('Error','Student Full Name is Required')
        elif any(ch.isdigit() for ch in stud_nameent.get()):
            stud_nameent.config(highlightbackground='red',highlightcolor='red')
            stud_nameent.focus()
            messagebox.showerror('Error','Name Cannot Have Digits')  
        elif stud_ageent.get()=='':
            stud_ageent.config(highlightbackground='red',highlightcolor='red')
            stud_nameent.focus()
            messagebox.showerror('Error','Student Age is Required')
        elif any(ch.isalpha() for ch in stud_ageent.get()):
            stud_ageent.config(highlightbackground='red',highlightcolor='red')
            stud_ageent.focus()
            messagebox.showerror('Error','Age Cannot Have Letters')
        elif stud_noent.get()=='':
            stud_noent.config(highlightbackground='red',highlightcolor='red')
            stud_noent.focus()
            messagebox.showerror('Error','Student Contact is Required')
        elif not re.match("(0|91)?[6-9][0-9]{9}", stud_noent.get()):
            stud_noent.config(highlightbackground='red',highlightcolor='red')
            stud_noent.focus()
            messagebox.showerror('Error','Please Enter a valid Phone Number')
        
        elif stud_emailent.get()=='':
            stud_emailent.config(highlightbackground='red',highlightcolor='red')
            stud_emailent.focus()
            messagebox.showerror('Error','Student Mail ID is Required')
        elif not chk_invmail(email=stud_emailent.get().lower()):
            stud_emailent.config(highlightbackground='red',highlightcolor='red')
            stud_emailent.focus()
            messagebox.showerror('Error','Please Enter a\nvalid Email Address ')
        elif acntpaswrdent.get()=='':
            acntpaswrdent.config(highlightbackground='red',highlightcolor='red')
            acntpaswrdent.focus()
            messagebox.showerror('Error','Create Your Password')
        else:
            pic_data=b''
            if pic_path.get()!='':
                resize_pic=Image.open(pic_path.get()).resize((100,100))
                resize_pic.save('temp_pic.png')
                read_data=open('temp_pic.png','rb')
                pic_data=read_data.read()
                read_data.close()
            messagebox.showinfo('Success','Account Created Successfully')
            data=f"""
{stud_ident.get()}

{stud_nameent.get()}

{student_gender.get()}

{stud_ageent.get()}

{p.get()}

{stud_noent.get()}

{stud_emailent.get()}
"""
            genidclicked(data=data)         
    add_frame=Frame(window,highlightbackground='dark goldenrod',highlightthickness=2)
    add=Button(add_frame,text="Add Img",command=open_pic,font=('Times New Roman',20,'bold'),bg='red',fg='white',bd=0,activebackground='black',activeforeground='red')
    add.place(x=400,y=550,width=100,height=50)
    add_frame.place(x=260,y=0)
    add_frame.pack_propagate(False)
    add_frame.configure(width=740,height=900)
    addacnt_lbl=Label(add_frame,image=addacntfm_pic_conv)
    addacnt_lbl.place(x=0,y=0)
    stud_namelb=Label(add_frame, bg='misty rose',text="Enter Student's Full Name:", font=('Times New Roman',17,'bold'),fg="dark goldenrod")
    stud_namelb.place(x=15,y=35)
    stud_nameent=Entry(add_frame,font=('Times New Roman',17),highlightbackground='gray',highlightcolor='saddle brown',highlightthickness=2)
    stud_nameent.place(x=15,y=100,width=270,height=40)
    stud_nameent.bind('<KeyRelease>', lambda r:remove_warning(entry=stud_nameent))
    genderlb=Label(add_frame,bg='misty rose',text="Select Student Gender:",fg="dark goldenrod",font=('Times New Roman',17,'bold'))
    genderlb.place(x=15,y=160)
    male=Radiobutton(add_frame,bg='misty rose',text='Male',fg="saddle brown",font=('Times New Roman',15),value='male',variable=student_gender)
    male.place(x=15,y=220)
    female=Radiobutton(add_frame,bg='misty rose',text='Female',fg="saddle brown",font=('Times New Roman',15),value='female',variable=student_gender)
    female.place(x=100,y=220)
    student_gender.set('Male')
    stud_agelb=Label(add_frame,bg='misty rose',fg="dark goldenrod", text="Enter Student Age:", font=('Times New Roman',17,'bold'))
    stud_agelb.place(x=15,y=280)
    stud_ageent=Entry(add_frame,font=('Times New Roman',17),highlightbackground='gray',highlightcolor='saddle brown',highlightthickness=2)
    stud_ageent.place(x=15,y=320,width=270,height=40)
    stud_ageent.bind('<KeyRelease>', lambda r:remove_warning(entry=stud_ageent))
    stud_nolb=Label(add_frame,bg='misty rose',fg="dark goldenrod", text="Enter Student Contact:", font=('Times New Roman',17,'bold'))
    stud_nolb.place(x=15,y=380)
    stud_noent=Entry(add_frame,font=('Times New Roman',17),highlightbackground='gray',highlightcolor='saddle brown',highlightthickness=2)
    stud_noent.place(x=15,y=420,width=270,height=40)
    stud_noent.bind('<KeyRelease>', lambda r:remove_warning(entry=stud_noent))
    stud_classlb=Label(add_frame,bg='misty rose', fg="dark goldenrod",text="Select Student Class:",font=('Times New Roman',17,'bold'))
    stud_classlb.place(x=15,y=490)
    p=StringVar()
    p.set("Select Your Class:")
    drop=OptionMenu(add_frame,p,'FYCS','SYCS','TYCS')
    drop.place(x=15,y=530)
    drop.config(bg='papaya whip',fg="brown",activebackground='papaya whip',activeforeground='saddle brown',font=('Times New Roman',13))
    stud_idlb=Label(add_frame,bg='misty rose',fg="dark goldenrod",text="Student ID Number:",font=('Times New Roman',17,'bold'))
    stud_idlb.place(x=400,y=35)
    stud_ident=Entry(add_frame,bg='misty rose',fg="dark goldenrod",font=('Times New Roman',18),highlightbackground='saddle brown',highlightcolor='saddle brown',highlightthickness=2)
    stud_ident.place(x=630,y=35,width=80,height=40)
    stud_ident.config(state='readonly')
    generate_id()
    stud_idinfo=Label(add_frame,bg='misty rose',text="""Automatically Generated ID Number
! Remember this ID Number Student
will Login Accnt.""",font=('Times New Roman',12),fg="saddle brown", justify=LEFT)
    stud_idinfo.place(x=400,y=100)
    stud_email=Label(add_frame,bg='misty rose',fg="dark goldenrod",text="Enter Student's Email Address:",font=('Times New Roman',17,'bold'))
    stud_email.place(x=400,y=180)
    stud_emailent=Entry(add_frame,font=('Times New Roman',17),highlightbackground='gray',highlightcolor='saddle brown',highlightthickness=2)
    stud_emailent.place(x=400,y=220,width=270,height=40)
    stud_emailent.bind('<KeyRelease>', lambda r:remove_warning(entry=stud_emailent))
    stud_emailinfo=Label(add_frame,bg='misty rose',text="""Via Email Student
can Recover Account
! In Case Forgetting Password and Also
Student will get Future Notifications.""",font=('Times New Roman',12),fg="saddle brown", justify=LEFT)
    stud_emailinfo.place(x=400,y=270)
    acntpaswrd=Label(add_frame,bg='misty rose',fg="dark goldenrod",text="Create Account Password:",font=('Times New Roman',17,'bold'))
    acntpaswrd.place(x=400,y=365)
    acntpaswrdent=Entry(add_frame,font=('Times New Roman',17),highlightbackground='gray',highlightcolor='saddle brown',highlightthickness=2)
    acntpaswrdent.place(x=400,y=400,width=270,height=40)
    acntpaswrdent.bind('<KeyRelease>', lambda r:remove_warning(entry=acntpaswrdent))
    acntpaswrdinfo=Label(add_frame,bg='misty rose',text="""Via Student Created Password
And Provided Student ID 
Student can Login Account.""",font=('Times New Roman',12),fg="saddle brown", justify=LEFT)
    acntpaswrdinfo.place(x=400,y=445)
    home=Button(add_frame,text="Home",font=('Times New Roman',20,'bold'),bg='red',fg='white',bd=0,activebackground='black',activeforeground='red',command=frwd_to_welcome)
    home.place(x=400,y=550,width=100,height=50)
    submit=Button(add_frame,text="Submit",font=('Times New Roman',20,'bold'),command=chk_valid,bg='red',fg='white',bd=0,activebackground='black',activeforeground='red')
    submit.place(x=550,y=550,width=100,height=50)
from tkinter import PhotoImage
front_img = "front_imag.png"
front_img_icon=PhotoImage(file=front_img)
front_img_lbl=Label(window,image=front_img_icon)
front_img_lbl.place(x=0,y=0)
def dashboard():
    dash_fm=Frame(window,highlightthickness=3,bg='papaya whip',highlightbackground='dark goldenrod')
    dash_fm.place(x=0,y=0,height=700,width=260)
    abtfm=Frame(window,highlightthickness=3,bg='papaya whip',highlightbackground='dark goldenrod')
    abtfm.place(x=1000,y=0,height=700,width=400)
    def abtus():
        lbl=Label(abtfm,text="""Savitribai Phule
Institute of Engineering and
Technology (SPIET) has
pioneered India's Engineering
education, research and
training ecosystem.

Pre Independence , SPIET has
been instrumental in
driving industrial growth
throughout united India.

Post Independence, SPIET
played a pivotal role in
setting up IISCs and
strengthened technology
excellence of country.

Located in South Mumbai,
SPIET is an autonomous
institution owned by
Maharashtra State Govt.
SPIET is known for its high
quality teaching,
collaborative research,industrial connect
and strong alumni network.""",justify=LEFT,bg='papaya whip',fg='dark goldenrod2',font=('Times New Roman',15,'bold'))
        lbl.place(x=0,y=0)
        def frwd_to_attend():
            lbl.destroy()
            back.destroy()
        back=Button(abtfm,text="Exit",command=frwd_to_attend,fg='saddle brown',bg='bisque',bd=1,
                    activebackground='bisque',activeforeground='saddle brown',font=(12))
        back.place(x=50,y=600)
    def attend():
        lbl=Label(abtfm,text="""As Per the
Attendance Ordinance:

1. Candidates must
maintain atleast 75%
attendance for each
course and average
attendance.

2. If the students fail
to maintain the number,
the department or
college doesn't forward
the examination form
to the University Exam
Unit.

However, a minimum of
50% is considered in
special cases like
health issues, family losses,
etc.""",justify=LEFT,bg='papaya whip',fg='dark goldenrod2',font=('Times New Roman',18,'bold'))
        lbl.place(x=0,y=0)
        def frwd_to_abt():
            lbl.destroy()
            back.destroy()
        back=Button(abtfm,text="Exit",command=frwd_to_abt,fg='saddle brown',bg='bisque',bd=1,
                    activebackground='bisque',activeforeground='saddle brown',font=(12))
        back.place(x=50,y=600) 
    abt_btn=Button(dash_fm,text='About Us',font=('Times New Roman',25,'bold'),fg='dark goldenrod',bg='papaya whip',bd=0,
                   activebackground='papaya whip',activeforeground='dark goldenrod',command=abtus)
    abt_btn.place(x=20,y=30,width=200,height=80)
    
    att_btn=Button(dash_fm,text='Attendance\nPolicy',font=('Times New Roman',25,'bold'),fg='dark goldenrod',bg='papaya whip',bd=0,
                   activebackground='papaya whip',activeforeground='dark goldenrod',command=attend)
    att_btn.place(x=20,y=280,width=210,height=80)
    view_btn=Button(dash_fm,text='View',font=('Times New Roman',25,'bold'),fg='dark goldenrod',bg='papaya whip',bd=0,command=welcome,
                    activebackground='papaya whip',activeforeground='dark goldenrod')
    view_btn.place(x=20,y=500,width=210,height=80)
dashboard()
window.mainloop()


