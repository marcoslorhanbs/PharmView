from tkinter import *
from tkinter import messagebox

jan = Tk()
jan.title("PharmView")
jan.geometry("1366x700+0+0")
jan.resizable(width=False, height=False)

#========= Photo Images / Arquivo de Imagens =====================================#
add_remedio = PhotoImage(file="icons/add_remedio.png")
edit_remedio = PhotoImage(file="icons/edit_remedio.png")
del_remedio = PhotoImage(file="icons/del_remedio.png")
remedio_plus = PhotoImage(file="icons/remedioplus.png")
remedio_edit = PhotoImage(file="icons/remedioedit.png")
remedio_delet = PhotoImage(file="icons/remediodelet.png")


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
pg2.place(x=700, y=80)
def onp2(self):
    box["bg"] = "darkgreen"
    news["text"] = "Editar Remedios do Sistema Ex. Nomes, valores..."
    news["bg"] = "darkgreen"
    news.place(x=350)
pg2.bind("<Enter>", onp2)

pg3 = Frame(box, width=10, height=10, bg="white")
pg3.place(x=1300, y=80)
def onp3(self):
    box["bg"] = "darkred"
    news["text"] = "Remover Remedios do Sistema"
    news["bg"] = "darkred"
    news.place(x=450)
    
pg3.bind("<Enter>", onp3)




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
RemedioPlusLabel.place(x=370, y=100)
RemedioPlusLabel.bind("<Enter>", onp1)

AddRemedioButton = Button(InitMainFrame, image=add_remedio, bd=0)
AddRemedioButton.place(x=300, y=200)
AddRemedioButton.bind("<Enter>", onp1)
#
RemedioEditLabel = Label(InitMainFrame, image=remedio_edit, bd=0)
RemedioEditLabel.place(x=670, y=100)
RemedioEditLabel.bind("<Enter>", onp2)

EditRemedioButton = Button(InitMainFrame, image=edit_remedio, bd=0)
EditRemedioButton.place(x=600, y=200)
EditRemedioButton.bind("<Enter>", onp2)
#
RemedioDelLabel = Label(InitMainFrame, image=remedio_delet, bd=0)
RemedioDelLabel.place(x=970, y=100)
RemedioDelLabel.bind("<Enter>", onp3)

DelRemedioButton = Button(InitMainFrame, image=del_remedio, bd=0)
DelRemedioButton.place(x=900, y=200)
DelRemedioButton.bind("<Enter>", onp3)


#============= BOTTOM FRAME ===========

BotFrame = Frame(InitMainFrame, width=1366, height=300, bg="darkgray", relief="raise")
BotFrame.place(x=0, y=300)

BotTitleLabel = Label(BotFrame, text="PharmView", font=("Century Gothic", 16), bg="darkgray")
BotTitleLabel.place(x=5, y=5)

BotInfo1Label = Label(BotFrame, text="♦ Adiciona Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo1Label.place(x=5, y=45)

BotInfo2Label = Label(BotFrame, text="♦ Edita Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo2Label.place(x=5, y=75)

BotInfo3Label = Label(BotFrame, text="♦ Remove Remedios", font=("Century Gothic", 16), bg="darkgray")
BotInfo3Label.place(x=5, y=105)



jan.mainloop()