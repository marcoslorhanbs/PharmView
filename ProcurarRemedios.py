from tkinter import *
from tkinter import messagebox
from tkinter import Listbox
from tkinter import ttk
import tkinter as tk
import DataBaser
import sqlite3

def connect():
    import DataBaser

global IdClicado
global PrecoClicado
global QuantidadeRemedioClicado
global ValidadeClicado
IdClicado = 1
PrecoClicado = 1
QuantidadeRemedioClicado = 1
ValidadeClicado = 1


def View():
    #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
    tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
    #SE A COLUNA PRECO FOI CLICADA:
    DataBaser.conn = sqlite3.connect("Data/Remedios.db")
    DataBaser.cur = DataBaser.conn.cursor()
    DataBaser.cur.execute("SELECT * FROM Remedios")
    rows = DataBaser.cur.fetchall()
    for row in rows:
        print(row) # Printa Todos os Registors do Banco De Dados
        tree.insert("", tk.END, values=row)
    #DataBaser.conn.close()
    global IdClicado
    global PrecoClicado
    global QuantidadeRemedioClicado
    global ValidadeClicado
    IdClicado = 1
    PrecoClicado = 1
    QuantidadeRemedioClicado = 1
    ValidadeClicado = 1

def Procurar():
    tree2.delete(*tree2.get_children()) #Apaga Todas As Linhas da TreeView
    remnome = RemedioNomeEntry.get()
    Procurador = DataBaser.cursor.execute("""
    Select * FROM Remedios
    WHERE nome = ?
    """, (remnome,))

    #VARIAVEIS PARA PEGAR OS DADOS DA MESMA LINHA SEPARADOS
    #1
    nome = DataBaser.cursor.execute("""
    Select Nome FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item in DataBaser.cursor.fetchone():
        print(item)
    #2
    categoria = DataBaser.cursor.execute("""
    Select Categoria FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item2 in DataBaser.cursor.fetchone():
        print(item2)
    #3
    preco = DataBaser.cursor.execute("""
    Select Preco FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item3 in DataBaser.cursor.fetchone():
        print(item3)
    #4
    quant = DataBaser.cursor.execute("""
    Select QuantidadeRemedio FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item4 in DataBaser.cursor.fetchone():
        print(item4)
    #5
    horario = DataBaser.cursor.execute("""
    Select Horario FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item5 in DataBaser.cursor.fetchone():
        print(item5)
    #6
    quantuser = DataBaser.cursor.execute("""
    Select QuantidadeUso FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item6 in DataBaser.cursor.fetchone():
        print(item6)
    #7
    receita = DataBaser.cursor.execute("""
    Select Receita FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item7 in DataBaser.cursor.fetchone():
        print(item7)
    #8
    Validade = DataBaser.cursor.execute("""
    Select Validade FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    for item8 in DataBaser.cursor.fetchone():
        print(item8)

    #===========AJUSTANDO A JANELA==========
    root.geometry("1150x590")
    BotFrame["height"] = 125
    VerticalScrollBar.place(height=468)
    tree2.place(y=40)
    
    #======INSERINDO BANCO DE DADOS NA NOVA TREEVIEW=====
    DataBaser.conn = sqlite3.connect("Data/Remedios.db")
    DataBaser.cur = DataBaser.conn.cursor()
    DataBaser.cur.execute("""SELECT * FROM Remedios 
    WHERE nome == ?
    """,(remnome,))
    rows = DataBaser.cur.fetchall()
    for row in rows:
        print(row) # Printa Todos os Registors do Banco De Dados
        tree2.insert("", 0, values=row)
    
    

root = Tk()
root.title("Visualizar Remedios do Sistema")
root.geometry("1150x500+0+100")
root.configure(background="darkgray")
root.resizable(width=False, height=False)


#============ PHOTO IMAGES ==============
ver_remedios = PhotoImage(file="icons/ver_remedios.png")
procurar_remedios = PhotoImage(file="icons/search_remedio_busca.png")

#VARIAVEIS PREDEFINIDAS



style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
#============ FUNÇÕES DE COMANDO DAS COLUNAS ======================
def OrganizaPorId(): #FUNÇAO DE QUANDO CLICA NA COLUNA TITULO ID
    if IdClicado == 1:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY ID DESC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        global IdClicado
        IdClicado = 2   
    elif IdClicado == 2:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY ID ASC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        global IdClicado
        IdClicado = 1
    elif IdClicado == 0:
        print("Janela Vazia")

#
def OrganizaPorQntd(): #FUNÇAO DE QUANDO CLICA NA COLUNA TITULO ID
    global QuantidadeRemedioClicado
    if QuantidadeRemedioClicado == 1:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY QuantidadeRemedio DESC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        QuantidadeRemedioClicado = 2
    elif QuantidadeRemedioClicado == 2:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY QuantidadeRemedio ASC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        QuantidadeRemedioClicado = 1
    elif QuantidadeRemedioClicado == 0:
        print("Janela Vazia")



#
def OrganizaPorPreco(): #FUNÇAO DE QUANDO CLICA NA COLUNA TITULO PREÇO
    global PrecoClicado
    if PrecoClicado == 1:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY Preco ASC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        PrecoClicado = 2
    elif PrecoClicado == 2:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY Preco DESC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        PrecoClicado = 1
    elif PrecoClicado == 0:
        print("Janela Vazia")
#

def OrganizaPorValidade(): #FUNÇAO DE QUANDO CLICA NA COLUNA TITULO PREÇO
    global ValidadeClicado
    if ValidadeClicado == 1:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY Validade ASC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        ValidadeClicado = 2
    elif ValidadeClicado == 2:
        #SEMPRE LIMPA A TREEVIEW ANTES DE ADD
        tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
        #SE A COLUNA PRECO FOI CLICADA:
        DataBaser.conn = sqlite3.connect("Data/Remedios.db")
        DataBaser.cur = DataBaser.conn.cursor()
        DataBaser.cur.execute("SELECT * FROM Remedios  ORDER BY Validade DESC")
        rows = DataBaser.cur.fetchall()
        for row in rows:
            print(row) # Printa Todos os Registors do Banco De Dados
            tree.insert("", tk.END, values=row)
        #DataBaser.conn.close()
        ValidadeClicado = 1
    elif ValidadeClicado == 0:
        print("Janela Vazia")
#
        
    


tree = ttk.Treeview(root, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show='headings', height=22)
tree.heading("#1", text="ID", command=OrganizaPorId)
tree.column("#1",minwidth=20,width=25, anchor=tk.CENTER)
tree.heading("#2", text="Remédio")
tree.column("#2",minwidth=200,width=200, anchor=tk.CENTER)
tree.heading("#3", text="Preço", command = OrganizaPorPreco)
tree.column("#3",minwidth=50,width=65, anchor=tk.CENTER)
tree.heading("#4", text="Categoria")
tree.column("#4",minwidth=200,width=200, anchor=tk.CENTER)
tree.heading("#5", text="Qntd Disponível", command=OrganizaPorQntd)
tree.column("#5",minwidth=120,width=120, anchor=tk.CENTER)
tree.heading("#6", text="Horario P/ Uso")
tree.column("#6",minwidth=100,width=100, anchor=tk.CENTER)
tree.heading("#7", text="Qntd Para Uso")
tree.column("#7",minwidth=100,width=100, anchor=tk.CENTER)
tree.heading("#8", text="Receita")
tree.column("#8",minwidth=180,width=180, anchor=tk.CENTER)
tree.heading("#9", text="Validade", command=OrganizaPorValidade)
tree.column("#9",minwidth=180,width=180, anchor=tk.CENTER)
tree.place(x=0, y=0)

VerticalScrollBar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
VerticalScrollBar.place(x=1135, y=0, height=450)

tree.configure(yscrollcommand=VerticalScrollBar.set)

#==========BOT FRAME===========================

BotFrame = Frame(root, width=1150, height=50, bg="darkgray", relief="raise")
BotFrame.pack(side=BOTTOM)

Visualizar = Button(BotFrame,image=ver_remedios, command=View, bg="darkgray")
Visualizar.place(x=1000, y=0)

RemedioNomeLabel = Label(BotFrame, text="Nome do Remédio:", bg="darkgray")
RemedioNomeLabel.place(x=0, y=0)



RemedioNomeEntry = ttk.Entry(BotFrame, width=30)
RemedioNomeEntry.place(x=120, y=0)

RemedioNomeEntryGet = RemedioNomeEntry.get()

ProcurarRemedio = Button(BotFrame, image=procurar_remedios, command=Procurar, bg="darkgray")
ProcurarRemedio.place(x=315, y=0)


tree2= ttk.Treeview(BotFrame, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8", "column9"), show='headings', height=20)
tree2.heading("#1", text="ID")
tree2.column("#1",minwidth=20,width=25, anchor=tk.CENTER)
tree2.heading("#2", text="Remédio")
tree2.column("#2",minwidth=200,width=200, anchor=tk.CENTER)
tree2.heading("#3", text="Preço")
tree2.column("#3",minwidth=50,width=65, anchor=tk.CENTER)
tree2.heading("#4", text="Categoria")
tree2.column("#4",minwidth=200,width=200, anchor=tk.CENTER)
tree2.heading("#5", text="Qntd Disponível")
tree2.column("#5",minwidth=120,width=120, anchor=tk.CENTER)
tree2.heading("#6", text="Horario P/ Uso")
tree2.column("#6",minwidth=100,width=100, anchor=tk.CENTER)
tree2.heading("#7", text="Qntd Para Uso")
tree2.column("#7",minwidth=100,width=100, anchor=tk.CENTER)
tree2.heading("#8", text="Receita")
tree2.column("#8",minwidth=180,width=180, anchor=tk.CENTER)
tree2.heading("#9", text="Validade")
tree2.column("#9",minwidth=180,width=180, anchor=tk.CENTER)
tree2.place(x=0, y=4000)

#ADICIONANDO PRODUTOS AO ABRIR JANELA:
#SEMPRE LIMPA A TREEVIEW ANTES DE ADD
tree.delete(*tree.get_children()) #Apaga Todas As Linhas da TreeView
#SE A COLUNA PRECO FOI CLICADA:
DataBaser.conn = sqlite3.connect("Data/Remedios.db")
DataBaser.cur = DataBaser.conn.cursor()
DataBaser.cur.execute("SELECT * FROM Remedios")
rows = DataBaser.cur.fetchall()
for row in rows:
    print(row) # Printa Todos os Registors do Banco De Dados
    tree.insert("", tk.END, values=row)
#DataBaser.conn.close()

root.mainloop()