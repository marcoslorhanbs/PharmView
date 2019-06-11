from tkinter import *
from tkinter import messagebox
import DataBaser
from tkinter import ttk

jan = Tk()
jan.title("Deletar Remedios No Sistema")
jan.geometry("500x150+350+150")

#========== PHOTO IMAGES ====================
search = PhotoImage(file="icons/search.png")
delet = PhotoImage(file="icons/del_remedio_remove.png")

#=========== TOP FRAME =======================
SuperTop = Frame(jan, width=500, height=25, bg="#880200", relief="raise")
SuperTop.pack(side=TOP)

SuperTopTitle = ttk.Label(SuperTop, text="Remover Remedios do Sistema", font=("Century Gothic", 14))
SuperTopTitle.place(x=100, y=0)

#============ WIDGETS ============================

AskNomeLabel = ttk.Label(jan, text="Nome do Remedio:", font=("Times New Roman", 16, "bold"))
AskNomeLabel.place(x=5, y=30)

AskNomeEntry = ttk.Entry(jan, width=20, font=("Times New Roman", 16, "bold"))
AskNomeEntry.place(x=200, y=30)

def ProcurarParaEditar():
    # lendo os dados
    remedynome = AskNomeEntry.get()
    DataBaser.cursor.execute("""
    Select Nome, Categoria, Preco, QuantidadeRemedio, Horario, QuantidadeUso, Receita, Validade FROM Remedios
    WHERE nome = ?
    """, (remedynome,))
    InfoLabel = ttk.Label(jan, text="Remédio Encontrado")
    InfoLabel.place(x=160, y=60)

    RemedioLabel = ttk.Label(jan, text= DataBaser.cursor.fetchmany(1))
    RemedioLabel.place(x=50, y=75)

    def DeletarRemedio():
        # excluindo um registro da tabela
        DataBaser.cursor.execute("""
        DELETE FROM Remedios
        WHERE nome = ?
        """, (remedynome,))

        DataBaser.conn.commit()
        print('Registro excluido com sucesso.')
        messagebox.showinfo(title="Aviso", message="Remédio Excluido Com Sucesso.")
        InfoLabel["text"] = "Remédio Deletado Com Sucesso"
        RemedioLabel.place(x=5000)
        DeleteButton.forget()

    DeleteButton = ttk.Button(jan, text="Apagar Remédio", command=DeletarRemedio)
    DeleteButton.pack(side=BOTTOM)
    
   

SearchButton = ttk.Button(jan, text="Procurar", command=ProcurarParaEditar)
SearchButton.place(x=430, y=30)



jan.mainloop()