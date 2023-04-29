from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
#------------------------------file--------------------------

f = open("C:/Users/VEERA/Documents/number_base_converter/Num_Base_Cnvrt.txt","a")


#-----------------------------Config-------------------------------------------
root.title("Base Convertor")
root.geometry("600x500")
root.config(bg = "lightgreen")
OptValue1 = "Select"
OptValue2 = "Select"
global res
res = ''

Ans = Label(text="",font = ("Cambria 15 bold"),bg ="lemon chiffon",relief = GROOVE,bd = 2,width = 15,height=2)
Ans.place(x=400,y=210)
#--------------------------------------------Base Convert Funs-----------------------------------#


def dec_to_dec(n):
    return int(n)
def dec_to_bin(n):
    return bin(int(n))
def dec_to_hex(n):
    return hex(int(n))
def dec_to_oct(n):
    return oct(int(n))
def bin_to_dec(n):
    return int(str(n),2)
def bin_to_bin(n):
    return bin(int(str(n),2))
def bin_to_hex(n):
    return hex(int(str(n),2))
def bin_to_oct(n):
    return oct(int(str(n),2))
def hex_to_dec(n):
    return int(str(n),16)
def hex_to_bin(n):
    return bin(int(str(n),16))
def hex_to_hex(n):
    return hex(int(str(n),16))
def hex_to_oct(n):
    return oct(int(str(n),16))
def oct_to_dec(n):
    return int(str(n),8)
def oct_to_bin(n):
    return bin(int(str(n),8))
def oct_to_hex(n):
    return hex(int(str(n),8))
def oct_to_oct(n):
    return oct(int(str(n),8))



#--------------------------------------------------------------------------------------------
def OptVal1(Cnvrt1):
    global OptValue1
    OptValue1 = Cnvrt1
#-----------------------------------Enable/Disable the keyboard Buttons--------------------------
    Entrykeytype.set(" ")
    Ans.config(text = "")

    if(OptValue1 == list1[0]):
        btna.config(state= DISABLED)
        btnb.config(state= DISABLED)
        btnc.config(state= DISABLED)
        btnd.config(state= DISABLED)
        btne.config(state= DISABLED)
        btnf.config(state= DISABLED)
        btn0.config(state= NORMAL)
        btn1.config(state= NORMAL)
        btn2.config(state= NORMAL)
        btn3.config(state= NORMAL)
        btn4.config(state= NORMAL)
        btn5.config(state= NORMAL)
        btn6.config(state= NORMAL)
        btn7.config(state= NORMAL)
        btn8.config(state= NORMAL)
        btn9.config(state= NORMAL)
    elif(OptValue1==list1[1]):
        btn0.config(state= NORMAL)
        btn1.config(state= NORMAL)
        btn2.config(state= DISABLED)
        btn3.config(state= DISABLED)
        btn4.config(state= DISABLED)
        btn5.config(state= DISABLED)
        btn6.config(state= DISABLED)
        btn7.config(state= DISABLED)
        btn8.config(state= DISABLED)
        btn9.config(state= DISABLED)
        btna.config(state= DISABLED)
        btnb.config(state= DISABLED)
        btnc.config(state= DISABLED)
        btnd.config(state= DISABLED)
        btne.config(state= DISABLED)
        btnf.config(state= DISABLED)
    elif(OptValue1 == list1[3]):
        btn0.config(state= NORMAL)
        btn1.config(state= NORMAL)
        btn2.config(state= NORMAL)
        btn3.config(state= NORMAL)
        btn4.config(state= NORMAL)
        btn5.config(state= NORMAL)
        btn6.config(state= NORMAL)
        btn7.config(state= NORMAL)
        btn8.config(state= DISABLED)
        btn9.config(state= DISABLED)
        btna.config(state= DISABLED)
        btnb.config(state= DISABLED)
        btnc.config(state= DISABLED)
        btnd.config(state= DISABLED)
        btne.config(state= DISABLED)
        btnf.config(state= DISABLED)
    else:
        btn0.config(state= NORMAL)
        btn1.config(state= NORMAL)
        btn2.config(state= NORMAL)
        btn3.config(state= NORMAL)
        btn4.config(state= NORMAL)
        btn5.config(state= NORMAL)
        btn6.config(state= NORMAL)
        btn7.config(state= NORMAL)
        btn8.config(state= NORMAL)
        btn9.config(state= NORMAL)
        btna.config(state= NORMAL)
        btnb.config(state= NORMAL)
        btnc.config(state= NORMAL)
        btnd.config(state= NORMAL)
        btne.config(state= NORMAL)
        btnf.config(state= NORMAL)  
                
def OptVal2(Cnvrt2):
    global OptValue2
    OptValue2 = Cnvrt2
def Convert():
    num = Entrykey.get()
    global res
    res = ""
    if(OptValue1=="Select" or OptValue2 =="Select"):
        messagebox.showerror("Select Convert","please select correct option")
    elif(OptValue1 == list1[0] and OptValue2 ==list1[0]):
        try:
            res = dec_to_dec(num)
        except:
            messagebox.showerror("Error!","Input value should be Interger")
    elif(OptValue1 == list1[0] and OptValue2 ==list1[1]):
        try:
            res = dec_to_bin(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be Interger")
    elif(OptValue1 == list1[0] and OptValue2 ==list1[2]):
        try:
            res = dec_to_hex(num)
            res = res[2:]

        except:
            messagebox.showerror("Error!","Input value should be Interger")
    elif(OptValue1 == list1[0] and OptValue2 ==list1[3]):
        try:
            res = dec_to_oct(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be Interger")
    elif(OptValue1 == list1[1] and OptValue2 ==list1[0]):
        try:
            res = bin_to_dec(num)
        except:
            messagebox.showerror("Error!","Input value should be in 0's and 1's")

    elif(OptValue1 == list1[1] and OptValue2 ==list1[1]):
        try:
            res = bin_to_bin(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be in 0's and 1's")
    elif(OptValue1 == list1[1] and OptValue2 ==list1[2]):
        try:
            res = bin_to_hex(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be in 0's and 1's")
    elif(OptValue1 == list1[1] and OptValue2 ==list1[3]):
        try:
            res = bin_to_oct(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be in 0's and 1's")
    elif(OptValue1 == list1[2] and OptValue2 ==list1[0]):
        try:
            res = hex_to_dec(num)
        except:
            messagebox.showerror("Error!","Input value should be 0-9 and A to f")
    elif(OptValue1 == list1[2] and OptValue2 ==list1[1]):
        try:
            res = hex_to_bin(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be 0-9 and A to f")
    elif(OptValue1 == list1[2] and OptValue2 ==list1[2]):
        try:
            res = hex_to_hex(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be 0-9 and A to f")
    elif(OptValue1 == list1[2] and OptValue2 ==list1[3]):
        try:
            res = hex_to_oct(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be 0-9 and A to f")

    elif(OptValue1 == list1[3] and OptValue2 ==list1[0]):
        try:
            res = oct_to_dec(num)
        except:
            messagebox.showerror("Error!","Input value should be 0-8")

    elif(OptValue1 == list1[3] and OptValue2 ==list1[1]):
        try:
            res = oct_to_bin(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be 0-8")
    elif(OptValue1 == list1[3] and OptValue2 ==list1[2]):
        try:
            res = oct_to_hex(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be 0-8")

    elif(OptValue1 == list1[3] and OptValue2 ==list1[3]):
        try:
            res = oct_to_oct(num)
            res = res[2:]
        except:
            messagebox.showerror("Error!","Input value should be 0-8")

    
    Ans.config(text = res)
    if(res!=''):
        f = open("C:/Users/VEERA/Documents/number_base_converter/Num_Base_Cnvrt.txt","a")
        f.write("\n"+OptValue1+" - "+OptValue2+" | "+str(num)+"  |  "+str(res)+" |")
        f.close()
#--------------------------------------filereading histroy--------------------------------------------

def History():
    f = open("C:/Users/VEERA/Documents/number_base_converter/Num_Base_Cnvrt.txt","r")
    messagebox.showinfo("HISTORY",f.read())
    f.close()

#-----------------------------------------------EXIT----------------------
def Exit():
    a = messagebox.askokcancel("Close","Are You Sure\nYou Want to Exit?")
    if a:
        f.seek(0)
        f.truncate()
        root.destroy()

#----------------------------------------Reset------------------------
def Reset1():
    Entrykeytype.set(" ")
    Cnvrt1.set("Select")
    Cnvrt2.set("Select")
    Ans.config(text = "")
    res = ""
    
    btn0.config(state= NORMAL)
    btn1.config(state= NORMAL)
    btn2.config(state= NORMAL)
    btn3.config(state= NORMAL)
    btn4.config(state= NORMAL)
    btn5.config(state= NORMAL)
    btn6.config(state= NORMAL)
    btn7.config(state= NORMAL)
    btn8.config(state= NORMAL)
    btn9.config(state= NORMAL)
    btna.config(state= NORMAL)
    btnb.config(state= NORMAL)
    btnc.config(state= NORMAL)
    btnd.config(state= NORMAL)
    btne.config(state= NORMAL)
    btnf.config(state= NORMAL)
#--------------------------------------------keyboard Funcs---------------------
def btn_0():
    Entrykey.insert(Entrykey.index(INSERT),"0")
def btn_1():
    Entrykey.insert(Entrykey.index(INSERT),"1")
def btn_2():
    Entrykey.insert(Entrykey.index(INSERT),"2")
def btn_3():
    Entrykey.insert(Entrykey.index(INSERT),"3")
def btn_4():
    Entrykey.insert(Entrykey.index(INSERT),"4")
def btn_5():
    Entrykey.insert(Entrykey.index(INSERT),"5")
def btn_6():
    Entrykey.insert(Entrykey.index(INSERT),"6")
def btn_7():
    Entrykey.insert(Entrykey.index(INSERT),"7")
def btn_8():
    Entrykey.insert(Entrykey.index(INSERT),"8")
def btn_9():
    Entrykey.insert(Entrykey.index(INSERT),"9")
def btn_a():
    Entrykey.insert(Entrykey.index(INSERT),"a")
def btn_b():
    Entrykey.insert(Entrykey.index(INSERT),"b")
def btn_c():
    Entrykey.insert(Entrykey.index(INSERT),"c")
def btn_d():
    Entrykey.insert(Entrykey.index(INSERT),"d")
def btn_e():
    Entrykey.insert(Entrykey.index(INSERT),"e")
def btn_f():
    Entrykey.insert(Entrykey.index(INSERT),"f")
    
Label(text = "           Number Base Convertor",font = ("Cambria 30 bold"),
      fg = "yellow",bg = "blue",height = 2,width = 200).pack()
Cnvrt1 = StringVar()
Cnvrt2 = StringVar()
Entrykeytype = StringVar()
#inserting image
canvas = Canvas(root,width = 100,height=50)
canvas.config(bg = "blue")
canvas.place(x = 10,y=30)
image = Image.open("C:/Users/VEERA/Documents/number_base_converter/base.png")
resize_img = image.resize((100,80))
img = ImageTk.PhotoImage(resize_img)
canvas.create_image(50,30,anchor=CENTER, image=img)
Label(text = "Convert Base From :",bg = "lightgreen",font = "Arial 12 bold").place(x = 50,y=110)
Label(text = "Convert Base To :",bg = "lightgreen",font = "Arial 12 bold").place(x = 400,y=110)
Label(text = "--->",font = ("Cambria 20 bold"),bg = "lightgreen").place(x=250,y=150)
list1 = ["Decimal","Binary","Hexadecimal","Octadecimal"]
CnvrtOpt1 = OptionMenu(root,Cnvrt1,*list1,command = OptVal1)
CnvrtOpt1.place(x = 50 ,y=150)
CnvrtOpt1.config(bg = "cyan",font = ("Courier 14 bold"),bd= 4,relief=RAISED,cursor="hand2",width = 10)
Cnvrt1.set("Select")
CnvrtOpt2 = OptionMenu(root,Cnvrt2,*list1,command = OptVal2)
CnvrtOpt2.place(x = 400 ,y=150)
CnvrtOpt2.config(bg = "cyan",font = ("Courier 14 bold"),bd= 4,relief=RAISED,cursor="hand2",width = 10)
Cnvrt2.set("Select")
Entrykey = Entry(root,textvariable = Entrykeytype,font = ("Cambria 13 bold"),bd = 4,width=15)
Entrykey.place(x = 50,y=210)
Label(text = "Output:",font = ("Cambria 15 bold"),bg = "lightgreen",fg = "black").place(x = 310,y=210)
Button(text = "Convert",command = Convert,font = ("Arial", 13 ,"bold"),bg = "navy",fg = "white",
       bd = 5,cursor = "hand2").place(x=480,y = 280)
Button(text = "Reset",command = Reset1,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 5,relief = RAISED,width = 7,cursor = "hand2").place(x = 480,y=330)
Button(text = "Histroy",command = History,font = ("Arial 12 bold"),bg = "cyan4",fg = "white",
       bd = 5,width = 7,relief = RAISED,cursor = "hand2").place(x = 480,y=380)
Button(text = "Exit",command = Exit,font = ("Arial 13 bold"),bg = "blue",fg = "white",
       bd = 5,relief = RAISED,width = 7,cursor = "hand2").place(x = 480,y=430)


#--------------------------------------Keyboard Buttons----------------------------------
Label(text = "KEYBOARD",font = ("cambria 20 bold"),fg = "blue",bg = "wheat",
      relief = GROOVE,anchor = N,width=22,height=7,bd=5).place(x = 24,y=250)
n=5
btn0=Button(text = "0",command = btn_0,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn0.place(x=n*10,y=300)
btn1=Button(text = "1",command = btn_1,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn1.place(x=n*22,y=300)
btn2=Button(text = "2",command = btn_2,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height = 2,cursor = "hand2")
btn2.place(x=n*34,y=300)
btn3=Button(text = "3",command = btn_3,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn3.place(x=n*46,y=300)
btn4=Button(text = "4",command = btn_4,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn4.place(x=n*58,y=300)
btn5=Button(text = "5",command = btn_5,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn5.place(x=n*10,y=352)
btn6=Button(text = "6",command = btn_6,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn6.place(x=n*22,y=352)
btn7=Button(text = "7",command = btn_7,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn7.place(x=n*34,y=352)
btn8=Button(text = "8",command = btn_8,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn8.place(x=n*46,y=352)
btn9=Button(text = "9",command = btn_9,font = ("Arial 13 bold"),bg = "gray30",fg = "white",
       bd = 1,relief = RAISED,width=5,height=2,cursor = "hand2")
btn9.place(x=n*58,y=352)
btna=Button(text = "a",command = btn_a,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 1,relief = RAISED,width=4,height=2,cursor = "hand2")
btna.place(x=n*10,y=404)
btnb=Button(text = "b",command = btn_b,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 1,relief = RAISED,width=4,height=2,cursor = "hand2")
btnb.place(x=n*20,y=404)
btnc=Button(text = "c",command = btn_c,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 1,relief = RAISED,width=4,height=2,cursor = "hand2")
btnc.place(x=n*30,y=404)
btnd=Button(text = "d",command = btn_d,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 1,relief = RAISED,width=4,height=2,cursor = "hand2")
btnd.place(x=n*40,y=404)
btne=Button(text = "e",command = btn_e,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 1,relief = RAISED,width=4,height=2,cursor = "hand2")
btne.place(x=n*50,y=404)
btnf=Button(text = "f",command = btn_f,font = ("Arial 13 bold"),bg = "green",fg = "white",
       bd = 1,relief = RAISED,width=4,height=2,cursor = "hand2")
btnf.place(x=n*60,y=404)

mainloop() 
