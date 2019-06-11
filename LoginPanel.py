from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import DataBaser
import UsersDataBase
import sys
import os

root = Tk()
root.geometry("600x330+500+200")
root.attributes('-alpha', 0.9)
root.configure(background="MidnightBlue")
root.resizable(width=False, height=False)
root.title("DP Systems - Login Panel")
root.iconbitmap(default="icons/devpy_new.ico")



logo = PhotoImage(file="icons/devpy_new.png")

LeftFrame = Frame(root, width=200, height=350, relief="raise", bg="DarkBlue")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(root, width=390, height=350, relief="raise", bg="MidnightBlue")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="DarkBlue")
LogoLabel.place(x=5, y=100)




UsernameLabel = Label(RightFrame, text="Username: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
UsernameLabel.place(x=5, y=75)

UsernameEntry = ttk.Entry(RightFrame, width=30)
UsernameEntry.place(x=150, y=83)

PasswordLabel = Label(RightFrame, text="Password: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
PasswordLabel.place(x=5, y=150)

PasswordEntry = ttk.Entry(RightFrame, width=30, show="•")
PasswordEntry.place(x=150, y=160)

def LoginAcess():
    UserLogin = UsernameEntry.get()
    PassLogin = PasswordEntry.get()
    UsersDataBase.cursor.execute("""
    SELECT * FROM Users 
    WHERE User = ? and Password = ?
    """ ,(UserLogin, PassLogin))
    VerifyLogin = UsersDataBase.cursor.fetchone()
    try:
        if (UserLogin in VerifyLogin and PassLogin in VerifyLogin):
            messagebox.showinfo(title="Aviso de Login", message="Acesso Confirmado, bem vindo!")
            root.attributes('-alpha', 0.3)
            UsersDataBase.cursor.execute("""
            UPDATE Users SET Status = 'On'
            WHERE User = ? and password = ?
            """, (UserLogin, PassLogin))
            UsersDataBase.conn.commit()
            root.destroy()
            os.system("python index.py")
        else:
            pass
    except:
        messagebox.showinfo(title="Aviso de Login", message="Acesso Negado, email ou senha incorretos!")

Login = ttk.Button(RightFrame, text="Login", width=30, command=LoginAcess)
Login.place(x=75, y=225)

def RegisterAccount():
    
    #REMOVE OS WIDGETS DE LOGIN DA TELA
    UsernameLabel.place(x=5000)
    UsernameEntry.place(x=5000)
    PasswordLabel.place(x=5000)
    PasswordEntry.place(x=5000)
    Login.place(x=5000)
    Register.place(x=5000)
    ForgotPassLabel.place(x=5000)
    ForgotPassButton.place(x=5000)
    #CRIA NOVOS WIDGETS PARA CADASTRO
    def BackToLogin():
        #REMOVE OS WIDGETS DE CADASTRO DA TELA
        NameLabelReg.place(x=5000)
        NameEntryReg.place(x=5000)
        EmailLabelReg.place(x=5000)
        EmailEntryReg.place(x=5000)
        UsernameLabelReg.place(x=5000)
        UsernameEntryReg.place(x=5000)
        PasswordLabelReg.place(x=5000)
        PasswordEntryReg.place(x=5000)
        SetorLabel.place(x=5000)
        SetorEntry.place(x=5000)
        RegisterNew.place(x=50000)
        Back.place(x=50000)
        #CARREGA OS WIDGETS DA TELA DE LOGIN
        UsernameLabel.place(x=5)
        UsernameEntry.place(x=150)
        PasswordLabel.place(x=5)
        PasswordEntry.place(x=150)
        Login.place(x=75)
        Register.place(x=105)
        ForgotPassLabel.place(x=25)
        ForgotPassButton.place(x=205)
        
        
    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=105, y=260)

    UsernameLabelReg = Label(RightFrame, text="Username: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
    UsernameLabelReg.place(x=5, y=0)

    UsernameEntryReg = ttk.Entry(RightFrame, width=30)
    UsernameEntryReg.place(x=150, y=10)

    PasswordLabelReg = Label(RightFrame, text="Password: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
    PasswordLabelReg.place(x=5, y=40)

    PasswordEntryReg = ttk.Entry(RightFrame, width=30, show="•")
    PasswordEntryReg.place(x=150, y=50)
    #
    SetorLabel = Label(RightFrame, text="Setor: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
    SetorLabel.place(x=5, y=70)

    SetorEntry = ttk.Entry(RightFrame, width=30)
    SetorEntry.place(x=150, y=80)

    #
    NameLabelReg = Label(RightFrame, text="Name: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
    NameLabelReg.place(x=5, y=100)

    NameEntryReg = ttk.Entry(RightFrame, width=30)
    NameEntryReg.place(x=150, y=110)

    EmailLabelReg = Label(RightFrame, text="Email: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
    EmailLabelReg.place(x=5, y=150)

    EmailEntryReg = ttk.Entry(RightFrame, width=30)
    EmailEntryReg.place(x=150, y=160)

    

    def RegisterNewAccount():
        Name = NameEntryReg.get()
        Email = EmailEntryReg.get()
        User = UsernameEntryReg.get()
        Password = PasswordEntryReg.get()
        Setor = SetorEntry.get()
        if (Name == "" and Email == "" and User == "" and Password == "" and Setor == ""):
            messagebox.showerror(title="Erro", message="Preencha os campos vazios")
        else:
            UsersDataBase.cursor.execute("""INSERT INTO Users (Name, Email, User, Password, Tag, Status)
            VALUES (?, ?, ?, ?, ?, ?)""", (Name, Email, User, Password, Setor, 'Off'))
            UsersDataBase.conn.commit()
            messagebox.showinfo(title="Aviso", message="Cadastro Concluído com sucesso")


    RegisterNew = ttk.Button(RightFrame, text="Register", width=30, command=RegisterNewAccount)
    RegisterNew.place(x=75, y=225)

    

Register = ttk.Button(RightFrame, text="Register", width=20, command=RegisterAccount)
Register.place(x=105, y=260)

ForgotPassLabel = Label(RightFrame, text="Esqueceu sua senha? ", font=("Verdana", 12),bd=0, bg="MIDNIGHTBLUE", fg="white")
ForgotPassLabel.place(x=25, y=308)

ForgotPassButton = Label(RightFrame, text="Recupere Aqui", bg="MIDNIGHTBLUE", bd=0, font=("Verdana", 12), fg="lightblue")
ForgotPassButton.place(x=205, y=308)
def ForgotClick(self):
    PasswordLabel.place(x=5000)
    PasswordEntry.place(x=5000)
    Login.place(x=5000)
    Register.place(x=5000)
    ForgotPassLabel.place(x=5000)
    ForgotPassButton.place(x=5000)
    EmailRecuperationLabel.place(x=5)
    EmailRecuperationEntry.place(x=150)
    
    

    

    ForgotTitle.place(x=50)

    GetPassButton.place(x=75)

    def BackToLogin():
        #REMOVE OS WIDGETS DE CADASTRO DA TELA
        ForgotTitle.place(x=5000)
        GetPassButton.place(x=5000)
        EmailRecuperationLabel.place(x=5000)
        EmailRecuperationEntry.place(x=5000)
        Back.place(x=50000)


        #CARREGA OS WIDGETS DA TELA DE LOGIN
        UsernameLabel.place(x=5)
        UsernameEntry.place(x=150)
        PasswordLabel.place(x=5)
        PasswordEntry.place(x=150)
        Login.place(x=75)
        Register.place(x=105)
        ForgotPassLabel.place(x=25)
        ForgotPassButton.place(x=205)

    Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
    Back.place(x=105, y=260)

    

ForgotPassButton.bind("<Button-1>", ForgotClick)


ForgotTitle = Label(RightFrame, text="Recuperação de Senha \n Insira os campos abaixo", bg="MIDNIGHTBLUE", fg="white", font=("Century Gothic", 16))
ForgotTitle.place(x=5000, y=5)

EmailRecuperationEntry = ttk.Entry(RightFrame, width=30)
EmailRecuperationEntry.place(x=5000, y=160)
EmailRecuperationLabel = Label(RightFrame, text="Email: ", font=("Century Gothic", 18), bg="MidnightBlue", fg="white")
EmailRecuperationLabel.place(x=5000, y=150)

def GetPass():
    User = UsernameEntry.get()
    Email = EmailRecuperationEntry.get()
    UsersDataBase.cursor.execute("""
    SELECT * FROM Users 
    WHERE User = ? and Email = ?
    """ ,(User, Email))
    VerifyResgate = UsersDataBase.cursor.fetchone()
    SenhaGet = UsersDataBase.cursor.execute("""
    SELECT Password FROM Users 
    WHERE User = ? and Email = ?
    """ ,(User, Email))
    MostraSenha = UsersDataBase.cursor.fetchone()
    if (User in VerifyResgate and Email in VerifyResgate):
        messagebox.showinfo(title="Aviso de Login", message=("Recuperação de Senha Aceita", "Senha:", MostraSenha))
    else:
        messagebox.showinfo(title="Aviso de Login", message="Falha ao Recuperar, Dados Incorretos")

GetPassButton = ttk.Button(RightFrame, text="Resgatar Senha", width=30, command=GetPass)
GetPassButton.place(x=5000, y=225)

root.mainloop()