from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import DataBaser
import sqlite3

jan = Tk()
jan.title("Editar Remedios do Sistema")
jan.geometry("500x450+350+150")

#==== PHOTO IMAGES =============
search = PhotoImage(file="icons/search.png")
editar = PhotoImage(file="icons/edit_remedio_editor.png")

#=========== TOP FRAME ==============
SuperTop = Frame(jan, width=500, height=25, bg="#088809", relief="raise")
SuperTop.pack(side=TOP)

SuperTopTitle = Label(SuperTop, text="Editar Remedios do Sistema", font=("Century Gothic", 14), bg="#088809", fg="white")
SuperTopTitle.place(x=125, y=0)

Top = Frame(jan, width=500, height=50, bg="#088809", relief="raise")
Top.pack(side=TOP)



MainFrame = Frame(jan, width=500, height=450, bg="#f0f0f0", relief="raise")
MainFrame.pack()

#=================== TOP ITEMS =======================

AskNomeLabel = Label(Top, text="Nome do Remedio:", bg="#088809", font=("Times New Roman", 16, "bold"))
AskNomeLabel.place(x=5, y=5)

AskNomeEntry = ttk.Entry(Top, width=20, font=("Times New Roman", 16, "bold"))
AskNomeEntry.place(x=200, y=5)

def ProcurarParaEditar():
    # lendo os dados
    remnome = AskNomeEntry.get()
    DataBaser.cursor.execute("""
    Select Nome, Categoria, Preco, QuantidadeRemedio, Horario, QuantidadeUso, Receita FROM Remedios
    WHERE nome = ?
    """, (remnome,))
    
    for linha in DataBaser.cursor.fetchmany(1):
        RemedioIdEntry["state"] = NORMAL
        RemedioNomeEntry["state"] = NORMAL
        RemedioTagEntry["state"] = NORMAL
        RemedioPrecoEntry["state"] = NORMAL
        RemedioQuantidadeEntry["state"] = NORMAL
        RemedioHorarioEntry["state"] = NORMAL
        PacienteQuantidadeEntry["state"] = NORMAL
        ReceitaMedicaSim["state"] = NORMAL
        ReceitaMedicaNao["state"] = NORMAL
        RemedioValidadeEntry["state"] = NORMAL
        #1
        nome = DataBaser.cursor.execute("""
        Select Nome FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item in DataBaser.cursor.fetchone():
            RemedioNomeEntry.insert(END, item)
        #2
        categoria = DataBaser.cursor.execute("""
        Select Categoria FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item2 in DataBaser.cursor.fetchone():
            RemedioTagEntry.insert(END, item2)
        #3
        preco = DataBaser.cursor.execute("""
        Select Preco FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item3 in DataBaser.cursor.fetchone():
            RemedioPrecoEntry.insert(END, item3)
        #4
        quant = DataBaser.cursor.execute("""
        Select QuantidadeRemedio FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item4 in DataBaser.cursor.fetchone():
            RemedioQuantidadeEntry.insert(END, item4)
        #5
        horario = DataBaser.cursor.execute("""
        Select Horario FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item5 in DataBaser.cursor.fetchone():
            RemedioHorarioEntry.insert(END, item5)
        #6
        quantuser = DataBaser.cursor.execute("""
        Select QuantidadeUso FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item6 in DataBaser.cursor.fetchone():
            PacienteQuantidadeEntry.insert(END, item6)
        #7
        receita = DataBaser.cursor.execute("""
        Select Receita FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item7 in DataBaser.cursor.fetchone():
            if (item7 == "Necessita Receita"):
                ReceitaMedicaSim.select()
            elif(item7 == "Nao Necessita Receita"):
                ReceitaMedicaNao.select()
        #8
        RemedyId = DataBaser.cursor.execute("""
        Select id FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item8 in DataBaser.cursor.fetchone():
            RemedioIdEntry.insert(END, item8)
        #9
        Validade = DataBaser.cursor.execute("""
        Select Validade FROM Remedios
        WHERE nome = ?
        """, (remnome,))
        for item9 in DataBaser.cursor.fetchone():
            RemedioValidadeEntry.insert(END, item9)
    


SearchButton = ttk.Button(Top, image=search, command=ProcurarParaEditar)
SearchButton.place(x=430, y=0)

#================== EDIT WIDGETS ===========================

RemedioFrame = LabelFrame(MainFrame, text="Informações do Remédio", labelanchor="n")
RemedioFrame.pack(side=TOP)

RemedioIdLabel = Label(RemedioFrame, text="ID do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioIdLabel.grid(row=0, column=0)

RemedioIdEntry = ttk.Entry(RemedioFrame, width=30,state=DISABLED)
RemedioIdEntry.grid(row=0, column=1)

RemedioNomeLabel = Label(RemedioFrame, text="Nome do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioNomeLabel.grid(row=1, column=0)

RemedioNomeEntry = ttk.Entry(RemedioFrame, width=30,state=DISABLED)
RemedioNomeEntry.grid(row=1, column=1)



#

RemedioTagLabel = Label(RemedioFrame, text="Categoria do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioTagLabel.grid(row=2, column=0)

RemedioTagEntry = ttk.Entry(RemedioFrame, width=30,state=DISABLED)
RemedioTagEntry.grid(row=2, column=1)



#

RemedioPrecoLabel = Label(RemedioFrame, text="Preço do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioPrecoLabel.grid(row=3, column=0)

RemedioPrecoEntry = ttk.Entry(RemedioFrame, width=30,state=DISABLED)
RemedioPrecoEntry.grid(row=3, column=1)



#

RemedioQuantidadeLabel = Label(RemedioFrame, text="Quantidade Disponível:", font=("Times New Roman", 14, "bold"))
RemedioQuantidadeLabel.grid(row=4, column=0)

RemedioQuantidadeEntry = ttk.Entry(RemedioFrame, width=30,state=DISABLED)
RemedioQuantidadeEntry.grid(row=4, column=1)

#

RemedioValidadeLabel = Label(RemedioFrame, text="Validade do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioValidadeLabel.grid(row=5, column=0)

RemedioValidadeEntry = DateEntry(RemedioFrame, width=28, background='darkblue', foreground='white', borderwidth=2, year=2019,state=DISABLED)
RemedioValidadeEntry.grid(row=5, column=1)

#=========== Informaçoes ao Paciente ====================
PacienteFrame = LabelFrame(MainFrame, text="Informações ao Paciente", labelanchor="n")
PacienteFrame.pack(side=TOP)

RemedioHorarioLabel = Label(PacienteFrame, text="Horário para Uso:", font=("Times New Roman", 14, "bold"))
RemedioHorarioLabel.grid(row=0, column=0)

RemedioHorarioEntry = ttk.Entry(PacienteFrame, width=30,state=DISABLED)
RemedioHorarioEntry.grid(row=0, column=1)



#

PacienteQuantidadeLabel = Label(PacienteFrame, text="Quantidade para Uso:", font=("Times New Roman", 14, "bold"))
PacienteQuantidadeLabel.grid(row=1, column=0)

PacienteQuantidadeEntry = ttk.Entry(PacienteFrame, width=30,state=DISABLED)
PacienteQuantidadeEntry.grid(row=1, column=1)



#

ReceitaMedicaLabel = Label(PacienteFrame, text="Necessita Receita: ", font=("Times New Roman", 14, "bold"))
ReceitaMedicaLabel.grid(row=2, column=0)

ReceitaVariavel = StringVar()
ReceitaVariavel.set(None)

ReceitaMedicaSim = Radiobutton(PacienteFrame, text="Sim", variable=ReceitaVariavel, value="Necessita Receita",state=DISABLED)
ReceitaMedicaSim.grid(row=2, columnspan=2)
ReceitaMedicaNao = Radiobutton(PacienteFrame, text="Não", variable=ReceitaVariavel, value="Nao Necessita Receita",state=DISABLED)
ReceitaMedicaNao.grid(row=2, column=2)

def LimparCampos():
    AskNomeEntry.delete(0, 'end')
    RemedioNomeEntry.delete(0, 'end')
    RemedioTagEntry.delete(0, 'end')
    RemedioPrecoEntry.delete(0, 'end')
    RemedioQuantidadeEntry.delete(0, 'end')
    RemedioValidadeEntry.delete(0, 'end')
    RemedioHorarioEntry.delete(0, 'end')
    PacienteQuantidadeEntry.delete(0, 'end')
    ReceitaVariavel.set(None)
    RemedioNomeEntry["state"] = DISABLED
    RemedioTagEntry["state"] = DISABLED
    RemedioPrecoEntry["state"] = DISABLED
    RemedioQuantidadeEntry["state"] = DISABLED
    RemedioHorarioEntry["state"] = DISABLED
    PacienteQuantidadeEntry["state"] = DISABLED
    ReceitaMedicaSim["state"] = DISABLED
    ReceitaMedicaNao["state"] = DISABLED
    RemedioValidadeEntry["state"] = DISABLED

LimparButton = ttk.Button(MainFrame, text="Limpar Campos", command=LimparCampos)
LimparButton.pack(side=BOTTOM)


def EditarRemedio():
    RemedioNome = RemedioNomeEntry.get()
    RemedioTag = RemedioTagEntry.get()
    RemedioPreco = RemedioPrecoEntry.get()
    RemedioQuantidade = RemedioQuantidadeEntry.get()
    RemedioHorario = RemedioHorarioEntry.get()
    PacienteQuantidade = PacienteQuantidadeEntry.get()
    ReceitaMedica = ReceitaVariavel.get()
    PegaId = RemedioIdEntry.get()
    Validade = RemedioValidadeEntry.get()
    DataBaser.cursor.execute("""
    UPDATE Remedios
    SET Nome = ?, Categoria = ?, Preco = ?, QuantidadeRemedio = ?, Horario = ?, QuantidadeUso = ?, Receita = ?, Validade = ?
    WHERE id = ?
    """, (RemedioNome, RemedioTag, RemedioPreco, RemedioQuantidade, RemedioHorario, PacienteQuantidade, ReceitaMedica,Validade, PegaId))

    DataBaser.conn.commit()

    print('Dados atualizados com sucesso.')
    messagebox.showinfo(title="PharmView Aviso", message="Dados Atualizados Com Sucesso, Ja pode fechar a aplicação.")
    AskNomeEntry.delete(0, 'end')
    RemedioIdEntry.delete(0, 'end')
    RemedioNomeEntry.delete(0, 'end')
    RemedioTagEntry.delete(0, 'end')
    RemedioPrecoEntry.delete(0, 'end')
    RemedioQuantidadeEntry.delete(0, 'end')
    RemedioHorarioEntry.delete(0, 'end')
    PacienteQuantidadeEntry.delete(0, 'end')
    RemedioValidadeEntry.delete(0, 'end')
    ReceitaVariavel.set(None)
    RemedioIdEntry["state"] = DISABLED
    RemedioNomeEntry["state"] = DISABLED
    RemedioTagEntry["state"] = DISABLED
    RemedioPrecoEntry["state"] = DISABLED
    RemedioQuantidadeEntry["state"] = DISABLED
    RemedioHorarioEntry["state"] = DISABLED
    PacienteQuantidadeEntry["state"] = DISABLED
    ReceitaMedicaSim["state"] = DISABLED
    ReceitaMedicaNao["state"] = DISABLED
    RemedioValidadeEntry["state"] = DISABLED

EditarButton = ttk.Button(MainFrame, image=editar, command=EditarRemedio)
EditarButton.pack(side=BOTTOM)



jan.mainloop()