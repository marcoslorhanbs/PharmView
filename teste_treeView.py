from tkinter import ttk
import tkinter as tk
import sqlite3


def connect():
    import DataBaser


def View():
    conn = sqlite3.connect("Remedios.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Remedios")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tk.END, values=row)
    conn.close()


connect()  #  this to create the db

root = tk.Tk()
root.geometry("400x400")

tree= ttk.Treeview(root, column=("column1", "column2", "column3"), show='headings')
tree.heading("#1", text="NUMBER")
tree.heading("#2", text="FIRST NAME")
tree.heading("#3", text="SURNAME")
tree.pack()

b2 = tk.Button(text="view data", command=View)
b2.pack()

root.mainloop()