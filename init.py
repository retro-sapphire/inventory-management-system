import tkinter
import pymysql as pym
from dotenv import load_dotenv
import os

load_dotenv(override=True) 

def main():
    root = tkinter.Tk()

    db_con = pym.connect(
        host=os.getenv("DB_DOMAIN"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        db=os.getenv("DB_NAME")
    )
    cursor = db_con.cursor()

    cursor.execute(f"select * from test_table")
    for i in cursor.fetchall():
        tkinter.Label(root, text=i).pack()

    root.mainloop()

if __name__ == "__main__":
    main()