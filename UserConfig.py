#utf-8
import sqlite3
from tkinter import *

conn = sqlite3.Connection('UserConfiguration.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS UserConfig(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    BotFrameOff INTEGER NOT NULL
);
""")


print("Configuraçoes do Usuario Carregadas")



ConfigRoot = Tk()
ConfigRoot.title('Configurações')
ConfigRoot.geometry("200x70")

RemoveFrameLabel = Label(ConfigRoot, text="Desativar Rodapé de Informações?")
RemoveFrameLabel.pack(side=TOP)

RemoveFrame = StringVar()
RemoveFrame.set(None)

RemoveFrameSim = Radiobutton(ConfigRoot, text="Sim", variable=RemoveFrame, value=1)
RemoveFrameSim.place(x=0, y=20)
RemoveFrameNao = Radiobutton(ConfigRoot, text="Não", variable=RemoveFrame, value=0)
RemoveFrameNao.place(x=100, y=20)

def SalvarConfiguracao():
    print("HOUVE UM ERRO")

enviar = Button(ConfigRoot, text="OK", command=SalvarConfiguracao)
enviar.pack(side=BOTTOM)

ConfigRoot.mainloop()