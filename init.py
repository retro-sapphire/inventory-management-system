import tkinter as tk
from tkinter import ttk
import pymysql as pym
from dotenv import load_dotenv
import os

load_dotenv(override=True) 

db_con = pym.connect(
    host=os.getenv("DB_DOMAIN"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    db=os.getenv("DB_NAME")
)
cursor = db_con.cursor()

def getInventory():
    cursor.execute(f"SELECT * FROM INVENTORY")
    return cursor.fetchall()

def main():
    root = tk.Tk()
    root.title("Inventory Management System")
    root.geometry("640x480")

    notebook = ttk.Notebook(root)

    tab1 = ttk.Frame(notebook)
    label1 = ttk.Label(tab1, text="Inventory")
    label1.pack()
    notebook.add(tab1, text="Tab 1")

    tab2 = ttk.Frame(notebook)
    label2 = ttk.Label(tab2, text="Orders")
    label2.pack()
    notebook.add(tab2, text="Tab 2")

    notebook.pack(expand = 1, fill ="both")

    # for i in getInventory():
    #     tkinter.Label(root, text=i).pack()

    root.mainloop()

if __name__ == "__main__":
    main()