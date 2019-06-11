from tkinter import *
from tkinter import messagebox
import os


jan = Tk()
jan.title("PharmView")
jan.geometry("1366x700+0+0")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="icons/icon.ico")

#MENU DA JANELA (EXTRA TOP)

class Sistema:
    def __init__(self, box):
        self.frame = Frame(box)#Crio o box top-level
        self.frame.pack()
        self.menu = Menu(box)#crio o menu
        
        self.menuFile = Menu(self.menu)#Primeiro Menu
        self.menuFile.add_command(label="Adicionar Medicamento", command=self.AddMedicamento)
        self.menuFile.add_command(label="Editar Medicamento", command=self.EdtMedicamento)
        self.menuFile.add_command(label="Excluir Medicamento", command=self.DelMedicamento)
        self.menuFile.add_command(label="Visualizar Medicamentos", command=self.VerMedicamentos)
        self.menu.add_cascade(label="Menu", menu=self.menuFile)
        self.menuHelp = Menu(self.menu)#Segundo Menu
        self.menuHelp.add_command(label="Dicas", command=self.dicas)
        self.menuHelp.add_command(label="Suporte", command=self.suporte)
        self.menuHelp.add_command(label="Sair", command=self.sair)
        self.menu.add_cascade(label="Ajuda", menu=self.menuHelp)
        box.config(menu=self.menu)

    #===== Menus =========
    def AddMedicamento(self):
        os.system('python AddRemedio.py')
    def EdtMedicamento(self):
        os.system('python EditRemedio.py')
    def DelMedicamento(self):
        os.system('python DeleteRemedio.py')
    def VerMedicamentos(self):
        os.system('python ProcurarRemedios.py')
    #===== Ajuda ===========
    def dicas(self):
        messagebox.showinfo(title="Dicas", message="• Add Remedio/Medicamento - Abre uma janela para cadastro de medicamentos no sistema \n • Editar Remedio/Medicamento - Abre uma janela para edição de dados de determinado medicamento ja salvo no sistema \n • Excluir Remedio - Abre uma janela para exclusão de determinado remedio/medicamento se já salvo no sistema \n • Procurar/ver Remedios - Abre uma Janela de Navegação que permite a visualização Tabelada de todos os remedios do sistema  Também permite a busca por determinado remedio")
    def suporte(self):
        messagebox.showinfo(title="Suporte", message="Algum problema com o sistema? \n Envie um e-mail para: devpysupport@gmail.com")
    def sair(self):
        exit()





#========= Photo Images / Arquivo de Imagens =====================================#
#======= Botoes ===============
add_remedio = PhotoImage(file="icons/add_remedio.png")
edit_remedio = PhotoImage(file="icons/edit_remedio.png")
del_remedio = PhotoImage(file="icons/del_remedio.png")
search_remedio = PhotoImage(file="icons/search_remedio.png")
notifications = PhotoImage(file="icons/notificacao.png")
notifications_active = PhotoImage(file="icons/notificacao_ativa.png")
settings = PhotoImage(file="icons/settings.png")
exitimg = PhotoImage(file="icons/exit.png")

#========= Icones =============
remedio_plus = PhotoImage(file="icons/remedioplus.png")
remedio_edit = PhotoImage(file="icons/remedioedit.png")
remedio_delet = PhotoImage(file="icons/remediodelet.png")
remedio_search = PhotoImage(file="icons/remediosearch.png")


#======== Init Frames / Primeiros Frames  =======================================#
TitleTopFrame = Frame(jan, width=1366, height=50, bg="red", relief="raise")
TitleTopFrame.pack(side=TOP)

#====================== SLIDE TOP ======================
#=================== Slide News ====================================================

box = Frame(jan, width=1366, height=100, bg="orange")
box.pack(side=TOP)

news = Label(jan,bg="orange", fg="white", text="PharmView - Sistema para Farmacia Popular Brasileira", 
font=("Century Gothic", 20))
news.place(x=300, y=50)




pg1 = Frame(box, width=10, height=10, bg="white")
pg1.place(x=50, y=80)
def onp1(self):
    box["bg"] = "darkblue"
    news["text"] = "Adicionar Remedios ao Sistema"
    news["bg"] = "darkblue"
    news.place(x=450)

pg1.bind("<Enter>", onp1)
pg2 = Frame(box, width=10, height=10, bg="white")
pg2.place(x=680, y=80)
def onp2(self):
    box["bg"] = "darkgreen"
    news["text"] = "Editar Remedios do Sistema Ex. Nomes, valores..."
    news["bg"] = "darkgreen"
    news.place(x=350)
pg2.bind("<Enter>", onp2)

pg3 = Frame(box, width=10, height=10, bg="white")
pg3.place(x=700, y=80)
def onp3(self):
    box["bg"] = "darkred"
    news["text"] = "Remover Remedios do Sistema"
    news["bg"] = "darkred"
    news.place(x=450)
    
pg3.bind("<Enter>", onp3)

pg4 = Frame(box, width=10, height=10, bg="white")
pg4.place(x=1300, y=80)
def onp4(self):
    box["bg"] = "#938900"
    news["text"] = "Procurar Remedios do Sistema"
    news["bg"] = "#938900"
    news.place(x=450)
    
pg4.bind("<Enter>", onp4)




#===================== SLIDE END TOP ========================



TitleTopLabel = Label(
    TitleTopFrame, text="PharmView - Sistema para Farmacia Popular Brasileira",
    font=("Times New Roman", 20), fg="white", bg="red"
)
TitleTopLabel.place(x=350, y=5)

InitMainFrame = Frame(jan, width=1366, height=650, bg="#f0f0f0", relief="raise")
InitMainFrame.pack(side=LEFT)



#======= Botoes Iniciais =================

RemedioPlusLabel = Label(InitMainFrame, image=remedio_plus, bd=0)
RemedioPlusLabel.place(x=170, y=100)
RemedioPlusLabel.bind("<Enter>", onp1)

def AdicionarRemedio():
    os.system("python AddRemedio.py")

AddRemedioButton = Button(InitMainFrame, image=add_remedio, bd=0, command=AdicionarRemedio)
AddRemedioButton.place(x=100, y=200)
AddRemedioButton.bind("<Enter>", onp1)
#
RemedioEditLabel = Label(InitMainFrame, image=remedio_edit, bd=0)
RemedioEditLabel.place(x=470, y=100)
RemedioEditLabel.bind("<Enter>", onp2)

def EditarRemedio():
    os.system("python EditRemedio.py")

EditRemedioButton = Button(InitMainFrame, image=edit_remedio, bd=0, command=EditarRemedio)
EditRemedioButton.place(x=400, y=200)
EditRemedioButton.bind("<Enter>", onp2)
#
RemedioDelLabel = Label(InitMainFrame, image=remedio_delet, bd=0)
RemedioDelLabel.place(x=770, y=100)
RemedioDelLabel.bind("<Enter>", onp3)

def DeletarRemedio():
    os.system("python DeleteRemedio.py")

DelRemedioButton = Button(InitMainFrame, image=del_remedio, bd=0, command=DeletarRemedio)
DelRemedioButton.place(x=700, y=200)
DelRemedioButton.bind("<Enter>", onp3)
#
RemedioSearchLabel = Label(InitMainFrame, image=remedio_search, bd=0)
RemedioSearchLabel.place(x=1070, y=100)
RemedioSearchLabel.bind("<Enter>", onp4)

def ProcurarRemedio():
    os.system("python ProcurarRemedios.py")

SearchRemedioButton = Button(InitMainFrame, image=search_remedio, bd=0, command=ProcurarRemedio)
SearchRemedioButton.place(x=1000, y=200)
SearchRemedioButton.bind("<Enter>", onp4)

#============= BOTTOM FRAME ===========

BotFrame = Frame(InitMainFrame, width=650, height=300, bg="darkgray", relief="raise")
BotFrame.place(x=0, y=300)

def DownBotFrame():
    if (BotFrameMin["text"] == "▼"):
        BotFrame.place(x=5000)
        BotFrameMin.place(y=490)
        BotFrameMin["text"] = "▲"
    elif (BotFrameMin["text"] == "▲"):
        BotFrame.place(x=0)
        BotFrameMin.place(y=280)
        BotFrameMin["text"] = "▼"

BotFrameMin = Button(InitMainFrame, text="▼", font=("Times New Roman", 16), bg="gray", command=DownBotFrame)
BotFrameMin.place(x=5, y=280)

BotTitle = Label(BotFrame, text="Desenvolvido por Devpy - Todos os direitos reservados",
font=("Century Gothic", 16), bg="darkgray")
BotTitle.place(x=0, y=200)


BotTitleLabel = Label(BotFrame, text="PharmView", font=("Century Gothic", 16), bg="darkgray")
BotTitleLabel.place(x=0, y=45)

BotInfo1Label = Label(BotFrame, text="♦ Adiciona Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo1Label.place(x=5, y=75)

BotInfo2Label = Label(BotFrame, text="♦ Edita Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo2Label.place(x=5, y=105)

BotInfo3Label = Label(BotFrame, text="♦ Remove Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo3Label.place(x=5, y=135)

BotInfo4Label = Label(BotFrame, text="♦ Procura Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo4Label.place(x=5, y=165)

#========== SOBRE A DEVPY ===================

BotTitleLabel = Label(BotFrame, text="Devpy", font=("Century Gothic", 16), bg="darkgray")
BotTitleLabel.place(x=300, y=45)

BotInfo1Label = Label(BotFrame, text="♦ Desenvolvimento Mobile", font=("Century Gothic", 16), bg="darkgray")
BotInfo1Label.place(x=305, y=75)

BotInfo2Label = Label(BotFrame, text="♦ Desenvolvimento de Software", font=("Century Gothic", 16), bg="darkgray")
BotInfo2Label.place(x=305, y=105)

BotInfo3Label = Label(BotFrame, text="♦ Desenvolvimento Web", font=("Century Gothic", 16), bg="darkgray")
BotInfo3Label.place(x=305, y=135)

BotInfo4Label = Label(BotFrame, text="♦ Social Media - Designer", font=("Century Gothic", 16), bg="darkgray")
BotInfo4Label.place(x=305, y=165)

#========== BOTOES FLUTUANTES INFERIOR DIREITO =============================
FloatFrame = Frame(InitMainFrame, width=710, height=300, bg="#f0f0f0", relief="raise")
FloatFrame.place(x=650, y=300)

def notificator():
    os.system("python Notifications.py")

notificador = Button(FloatFrame, image=notifications, bd=0, command=notificator)
notificador.place(x=650, y=150)

def configurar():
    pass
    

configurador = Button(FloatFrame, image=settings, bd=0, command=configurar)
configurador.place(x=595, y=150)

def sair():
    pass

sair = Button(FloatFrame, image=exitimg, bd=0, command=sair)
sair.place(x=540, y=150)

Sistema(jan)
jan.mainloop()