from tkinter import *
from tkinter import messagebox
from tkinter import Listbox
from tkinter import ttk
import tkinter as tk
import DataBaser
import sqlite3

def connect():
    import DataBaser

def View():
    DataBaser.conn = sqlite3.connect("Remedios.db")
    DataBaser.cur = DataBaser.conn.cursor()
    DataBaser.cur.execute("SELECT * FROM Remedios")
    rows = DataBaser.cur.fetchall()
    for row in rows:
        print(row) # Printa Todos os Registors do Banco De Dados
        tree.insert("", tk.END, values=row)
    DataBaser.conn.close()

def Procurar():
    remnome = RemedioNomeEntry.get()
    DataBaser.cursor.execute("""
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

    messagebox.showinfo(title="Aviso", message=("Nome do Remedio: ", item, " Categoria: ", item2, "\n",
     " Preço: ", item3, " Qntd Disponivel: ", item4, "\n" ," Horario de Uso: ", item5, " Qntd de Uso: ", item6, "\n", " Receita: ", item7))

root = Tk()
root.title("Visualizar Remedios do Sistema")
root.geometry("980x500+0+100")
root.configure(background="darkgray")

#============ PHOTO IMAGES ==============
ver_remedios = PhotoImage(file="icons/ver_remedios.png")
procurar_remedios = PhotoImage(file="icons/search_remedio_busca.png")


tree= ttk.Treeview(root, column=("column1", "column2", "column3", "column4", "column5", "column6", "column7", "column8"), show='headings', height=22)
tree.heading("#1", text="ID")
tree.column("#1",minwidth=20,width=25, anchor=tk.CENTER)
tree.heading("#2", text="Remédio")
tree.column("#2",minwidth=200,width=200, anchor=tk.CENTER)
tree.heading("#3", text="Categoria")
tree.column("#3",minwidth=200,width=200, anchor=tk.CENTER)
tree.heading("#4", text="Preço")
tree.column("#4",minwidth=50,width=65, anchor=tk.CENTER)
tree.heading("#5", text="Qntd Disponível")
tree.column("#5",minwidth=100,width=100, anchor=tk.CENTER)
tree.heading("#6", text="Horario P/ Uso")
tree.column("#6",minwidth=90,width=90, anchor=tk.CENTER)
tree.heading("#7", text="Qntd Para Uso")
tree.column("#7",minwidth=100,width=100, anchor=tk.CENTER)
tree.heading("#8", text="Receita")
tree.column("#8",minwidth=200,width=200, anchor=tk.CENTER)
tree.pack()

Visualizar = tk.Button(image=ver_remedios, command=View, bg="darkgray")
Visualizar.pack(side=RIGHT)

RemedioNomeLabel = Label(root, text="Nome do Remédio:", bg="darkgray")
RemedioNomeLabel.pack(side=LEFT)

RemedioNomeEntry = Entry(root, width=30, bg="darkgray")
RemedioNomeEntry.pack(side=LEFT)

ProcurarRemedio = tk.Button(image=procurar_remedios, command=Procurar, bg="darkgray")
ProcurarRemedio.pack(side=LEFT)




root.mainloop()