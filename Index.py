#======== Libraries
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import UsersDataBase


jan = Tk()
jan.title("PharmView")
jan.geometry("800x600+250+50")
jan.iconbitmap(default="icons/icone.ico")

#============ Photos
Cadd = PhotoImage(file="icons/Cadd.png")
Cdel = PhotoImage(file="icons/Cdel.png")
Cedt = PhotoImage(file="icons/Cedt.png")
Csrc = PhotoImage(file="icons/Csrc.png")
Conf = PhotoImage(file="icons/settings.png")
Ext  = PhotoImage(file="icons/exit.png")
logo = PhotoImage(file="icons/logoApp.png")
venda = PhotoImage(file="icons/venda.png")



#============ Frames
LeftFrame = Frame(jan, width=100, height=600, bg="#0000ff", relief="raise")
LeftFrame.pack(side=LEFT)

#============ Buttons Names
AddDrug = Label(LeftFrame, text="Adicionar Medicamento", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
AddDrug.place(x=5000, y=40)

DelDrug = Label(LeftFrame, text="Remover Medicamento", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
DelDrug.place(x=5000, y=125)

EdtDrug = Label(LeftFrame, text="Editar Medicamento", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
EdtDrug.place(x=5000, y=210)

SrcDrug = Label(LeftFrame, text="Procurar Medicamento", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
SrcDrug.place(x=5000, y=295)

SellDrug = Label(LeftFrame, text="Vender Medicamento", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
SellDrug.place(x=5000, y=380)

SetApp = Label(LeftFrame, text="Configurações", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
SetApp.place(x=5000, y=485)

ExtApp = Label(LeftFrame, text="Sair/Log Out", font=("Eras Light ITC", 16), bg="#0000ff", bd=0, fg="white")
ExtApp.place(x=5000, y=545)

def MouseOn(self):
    LeftFrame["width"] = 310
    AddDrug.place(x=90)
    DelDrug.place(x=90)
    EdtDrug.place(x=90)
    SrcDrug.place(x=90)
    SellDrug.place(x=90)
    SetApp.place(x=90)
    ExtApp.place(x=90)
    LogoApp.place(x=325)

LeftFrame.bind("<Enter>", MouseOn)
def MouseOff(self):
    LeftFrame["width"] = 100
    AddDrug.place(x=5000)
    DelDrug.place(x=5000)
    EdtDrug.place(x=5000)
    SrcDrug.place(x=5000)
    SellDrug.place(x=5000)
    SetApp.place(x=5000)
    ExtApp.place(x=5000)
    LogoApp.place(x=250)
LeftFrame.bind("<Leave>", MouseOff)

#============ Buttons
def AddMedicamento():
    os.system("python AddRemedio.py")

Add = Button(LeftFrame, bg="#0000ff", bd=0, image=Cadd, command=AddMedicamento, state="normal")
Add.place(x=10, y=15)

def DelMedicamento():
    os.system("python DeleteRemedio.py")

Del = Button(LeftFrame, bg="#0000ff", bd=0, image=Cdel, command=DelMedicamento, state="normal")
Del.place(x=10, y=100)

def EdtMedicamento():
    os.system("python EditRemedio.py")

Edt = Button(LeftFrame, bg="#0000ff", bd=0, image=Cedt, command=EdtMedicamento, state="normal")
Edt.place(x=10, y=185)

def SrcMedicamento():
    os.system("python ProcurarRemedios.py")

Src = Button(LeftFrame, bg="#0000ff", bd=0, image=Csrc, command=SrcMedicamento, state="normal")
Src.place(x=10, y=270)

def SellMedicamento():
    pass

Sell = Button(LeftFrame, bg="#0000ff", bd=0, image=venda, command=SellMedicamento, state="normal")
Sell.place(x=10, y=355)

def settings():
    setjan = Tk()
    setjan.title("Configuração")
    setjan.geometry("220x50")
    setjan.iconbitmap(default="icons/icone.ico")

    def vermelho():
        LeftFrame["bg"] = "red"
        Add["bg"] = "red"
        Del["bg"] = "red"
        Edt["bg"] = "red"
        Src["bg"] = "red"
        Sell["bg"] = "red"
        Confg["bg"] = "red"
        Sair["bg"] = "red"
        AddDrug["bg"] = "red"
        DelDrug["bg"] = "red"
        EdtDrug["bg"] = "red"
        SrcDrug["bg"] = "red"
        SellDrug["bg"] = "red"
        SetApp["bg"] = "red"
        ExtApp["bg"] = "red"
        VersionInfoFrame["bg"] = "red"
        VersionInfoLabel["bg"] = "red"

    red = Button(setjan, text="Vermelho", bg="red", fg="white", command=vermelho)
    red.pack(side=LEFT)

    def azul():
        LeftFrame["bg"] = "#0000ff"
        Add["bg"] = "#0000ff"
        Del["bg"] = "#0000ff"
        Edt["bg"] = "#0000ff"
        Src["bg"] = "#0000ff"
        Sell["bg"] = "#0000ff"
        Confg["bg"] = "#0000ff"
        Sair["bg"] = "#0000ff"
        AddDrug["bg"] = "#0000ff"
        DelDrug["bg"] = "#0000ff"
        EdtDrug["bg"] = "#0000ff"
        SrcDrug["bg"] = "#0000ff"
        SellDrug["bg"] = "#0000ff"
        SetApp["bg"] = "#0000ff"
        ExtApp["bg"] = "#0000ff"
        VersionInfoFrame["bg"] = "#0000ff"
        VersionInfoLabel["bg"] = "#0000ff"

    blue = Button(setjan, text="Azul(Padrão)", bg="#0000ff", fg="white", command=azul)
    blue.pack(side=LEFT)

    def verde():
        LeftFrame["bg"] = "green"
        Add["bg"] = "green"
        Del["bg"] = "green"
        Edt["bg"] = "green"
        Src["bg"] = "green"
        Sell["bg"] = "green"
        Confg["bg"] = "green"
        Sair["bg"] = "green"
        AddDrug["bg"] = "green"
        DelDrug["bg"] = "green"
        EdtDrug["bg"] = "green"
        SrcDrug["bg"] = "green"
        SellDrug["bg"] = "green"
        SetApp["bg"] = "green"
        ExtApp["bg"] = "green"
        VersionInfoFrame["bg"] = "green"
        VersionInfoLabel["bg"] = "green"

    green = Button(setjan, text="Verde", bg="green", fg="black", command=verde)
    green.pack(side=LEFT)

    def cinza():
        LeftFrame["bg"] = "gray"
        Add["bg"] = "gray"
        Del["bg"] = "gray"
        Edt["bg"] = "gray"
        Src["bg"] = "gray"
        Sell["bg"] = "gray"
        Confg["bg"] = "gray"
        Sair["bg"] = "gray"
        AddDrug["bg"] = "gray"
        DelDrug["bg"] = "gray"
        EdtDrug["bg"] = "gray"
        SrcDrug["bg"] = "gray"
        SellDrug["bg"] = "gray"
        SetApp["bg"] = "gray"
        ExtApp["bg"] = "gray"
        VersionInfoFrame["bg"] = "gray"
        VersionInfoLabel["bg"] = "gray"

    gray = Button(setjan, text="Cinza", bg="gray", fg="black", command=cinza)
    gray.pack(side=LEFT)
    

    setjan.mainloop()

Confg = Button(LeftFrame, bg="#0000ff", bd=0, image=Conf, command=settings)
Confg.place(x=25, y=475)

def logout():
    messagebox.showwarning(title="Log Out - Warning", message="Todas as alterações não salvas serão excluidas!")
    UsersDataBase.cursor.execute("""
    UPDATE Users SET Status = 'Off'
    WHERE Status = 'On'
    """)
    UsersDataBase.conn.commit()
    jan.destroy()
    os.system("python LoginPanel.py")

Sair = Button(LeftFrame, bg="#0000ff", bd=0, image=Ext, command=logout)
Sair.place(x=25, y=535)

#========

LogoApp = Label(jan, image=logo, bd=0)
LogoApp.place(x=250, y=50)

VersionInfoFrame = Frame(jan, width=200, height=30, bg="#0000ff", relief="raise")
VersionInfoFrame.place(x=600, y=570)

VersionInfoLabel = Label(VersionInfoFrame, text="V2.0", font=("Eras Light ITC", 14), bg="#0000ff", fg="white")
VersionInfoLabel.place(x=0, y=0)

#========= Verificando Cargo do Usuario ==============
UsersDataBase.cursor.execute("SELECT * FROM Users WHERE Status = 'On' ")
VerifyStatus = UsersDataBase.cursor.fetchone()
print(VerifyStatus)
UsersDataBase.cursor.execute("SELECT User FROM Users WHERE Status = 'On' ")
VerifyName = UsersDataBase.cursor.fetchone()
UserLabel = Label(VersionInfoFrame, text=(VerifyName), font=("Eras Light ITC", 14), bg="#0000ff", fg="white")
UserLabel.place(x=40, y=0)
UsersDataBase.cursor.execute("SELECT Tag FROM Users WHERE Status = 'On' ")
VerifyTag = UsersDataBase.cursor.fetchone()
print(VerifyTag)

if ('Estagiario' in VerifyTag):
    Add["state"] = "disabled"
    Del["state"] = "disabled"
    Edt["state"] = "disabled"
    Sell["state"] = "normal"
else: 
    pass


jan.mainloop()