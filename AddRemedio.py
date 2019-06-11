#:python 3.5.2
#:AddRemedio.py
#:indexProgram.py
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import sqlite3
import DataBaser

JanelaAddRemedio = Tk()
JanelaAddRemedio.title("Adicionar Novo Remédio - Nao deixe aberta sem ultilização")
JanelaAddRemedio.geometry("500x350+350+150")
#===================== Photo Images / Arquivo de Fotos ========================
add_remedio_cadastro = PhotoImage(file="icons/add_remedio_cadastro.png")


#===============================================================================

InfoFrame = Frame(JanelaAddRemedio, width=500, height=50, bg="darkblue", relief="raise")
InfoFrame.pack(side=TOP)

InfoFrameLabel = Label(InfoFrame, text="Adicionar Novo Remédio \n Feche a janela quando terminar.",
font=("Century Gothic", 14), bg="darkblue", fg="white")
InfoFrameLabel.place(x=75, y=0)

MainFrame = Frame(JanelaAddRemedio, width=500, height=450, bg="#f0f0f0", relief="raise")
MainFrame.pack()

#=============== Layout Grid Cadastro Remedios =====================================
RemedioFrame = ttk.LabelFrame(MainFrame, text="Informações do Remédio", labelanchor="n")
RemedioFrame.pack(side=TOP)

RemedioNomeLabel = ttk.Label(RemedioFrame, text="Nome do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioNomeLabel.grid(row=0, column=0)

RemedioNomeEntry = ttk.Entry(RemedioFrame, width=30)
RemedioNomeEntry.grid(row=0, column=1)



#

RemedioTagLabel = ttk.Label(RemedioFrame, text="Categoria do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioTagLabel.grid(row=1, column=0)

RemedioTagEntry = ttk.Entry(RemedioFrame, width=30)
RemedioTagEntry.grid(row=1, column=1)



#

RemedioPrecoLabel = ttk.Label(RemedioFrame, text="Preço do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioPrecoLabel.grid(row=2, column=0)

RemedioPrecoEntry = ttk.Entry(RemedioFrame, width=30)
RemedioPrecoEntry.grid(row=2, column=1)



#

RemedioQuantidadeLabel = ttk.Label(RemedioFrame, text="Quantidade Disponível:", font=("Times New Roman", 14, "bold"))
RemedioQuantidadeLabel.grid(row=3, column=0)

RemedioQuantidadeEntry = ttk.Entry(RemedioFrame, width=30)
RemedioQuantidadeEntry.grid(row=3, column=1)

RemedioValidadeLabel = ttk.Label(RemedioFrame, text="Validade do Remédio:", font=("Times New Roman", 14, "bold"))
RemedioValidadeLabel.grid(row=4, column=0)

RemedioValidadeEntry = DateEntry(RemedioFrame, width=28, background='darkblue', foreground='white', borderwidth=2)
RemedioValidadeEntry.grid(row=4, column=1)



#=========== Informaçoes ao Paciente ====================
PacienteFrame = ttk.LabelFrame(MainFrame, text="Informações ao Paciente", labelanchor="n")
PacienteFrame.pack(side=TOP)

RemedioHorarioLabel = ttk.Label(PacienteFrame, text="Horário para Uso:", font=("Times New Roman", 14, "bold"))
RemedioHorarioLabel.grid(row=0, column=0)

RemedioHorarioEntry = ttk.Entry(PacienteFrame, width=30)
RemedioHorarioEntry.grid(row=0, column=1)



#

PacienteQuantidadeLabel = ttk.Label(PacienteFrame, text="Quantidade para Uso:", font=("Times New Roman", 14, "bold"))
PacienteQuantidadeLabel.grid(row=1, column=0)

PacienteQuantidadeEntry = ttk.Entry(PacienteFrame, width=30)
PacienteQuantidadeEntry.grid(row=1, column=1)



#

ReceitaMedicaLabel = ttk.Label(PacienteFrame, text="Necessita Receita: ", font=("Times New Roman", 14, "bold"))
ReceitaMedicaLabel.grid(row=2, column=0)

ReceitaVariavel = StringVar()
ReceitaVariavel.set(None)

ReceitaMedicaSim = ttk.Radiobutton(PacienteFrame, text="Sim", variable=ReceitaVariavel, value="Necessita Receita")
ReceitaMedicaSim.grid(row=2, columnspan=2)
ReceitaMedicaNao = ttk.Radiobutton(PacienteFrame, text="Não", variable=ReceitaVariavel, value="Nao Necessita Receita")
ReceitaMedicaNao.grid(row=2, column=2)



#

def CadastrarRemedio():
    RemedioNome = RemedioNomeEntry.get()
    RemedioTag = RemedioTagEntry.get()
    RemedioPreco = RemedioPrecoEntry.get()
    RemedioQuantidade = RemedioQuantidadeEntry.get()
    RemedioHorario = RemedioHorarioEntry.get()
    PacienteQuantidade = PacienteQuantidadeEntry.get()
    ReceitaMedica = ReceitaVariavel.get()
    RemedioValidade = RemedioValidadeEntry.get()
    DataBaser.cursor.execute("""
    INSERT INTO Remedios (Nome, Categoria, Preco, QuantidadeRemedio, Horario, QuantidadeUso, Receita, Validade)
    VALUES (?,?,?,?,?,?,?,?)
    """, (RemedioNome, RemedioTag, RemedioPreco, RemedioQuantidade, RemedioHorario, PacienteQuantidade, ReceitaMedica, RemedioValidade))
    RemedioNomeEntry.delete(0, 'end')
    RemedioTagEntry.delete(0, 'end')
    RemedioPrecoEntry.delete(0, 'end')
    RemedioQuantidadeEntry.delete(0, 'end')
    RemedioHorarioEntry.delete(0, 'end')
    PacienteQuantidadeEntry.delete(0, 'end')
    ReceitaVariavel.set(None)
    RemedioValidadeEntry.delete(0, 'end')

    # gravando no bd
    DataBaser.conn.commit()

    print('Dados inseridos com sucesso.')
    messagebox.showinfo(title="Aviso de Cadastro de Remedio", message="Remedio Adicionado(Salvo) com Sucesso \n Ja pode fechar a aplicação")
    

CadastrarButton = ttk.Button(MainFrame,text="Adicionar Remedio" , command=CadastrarRemedio, width=30, state="active")
CadastrarButton.pack(side=BOTTOM)


JanelaAddRemedio.mainloop()
#image=add_remedio_cadastro