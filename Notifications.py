


from tkinter import *
import DataBaser
from datetime import datetime

jan = Tk()
jan.title("Notificações")
jan.geometry("500x600")

NotificationsBox = Listbox(jan, width=83, height=38, bg="black", fg="white", font=("Century Gothic", 20))
NotificationsBox.pack()

now = datetime.now()
mes = str(now.month)
newmes = ("0" + mes)
print(newmes)
fim = 30



Validade = DataBaser.cursor.execute("""
Select Nome,Validade FROM Remedios WHERE Validade >= ?
""", ('31/05/2019',))
for item9 in DataBaser.cursor.fetchone():
    NotificationsBox.insert(END, item9)

jan.mainloop()
