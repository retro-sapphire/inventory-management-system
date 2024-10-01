# Python Libraries
import customtkinter as ctk
import mysql.connector as con
from dotenv import load_dotenv
import os

# App modules
from modules.sidebar import Sidebar
from modules.inventory import InventoryFrame
from modules.orders import OrdersFrame
from modules.settings import SettingsFrame

load_dotenv(override=True) 

cnx = con.connect(
    host=os.getenv("DB_DOMAIN"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    db=os.getenv("DB_NAME")
)
cur = cnx.cursor()

def getInventory():
    cur.execute(f"SELECT * FROM INVENTORY")
    return cur.fetchall()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Grocery Management System")
        self.geometry("1000x700")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self, self.inventoryFn, self.ordersFn, self.settingsFn)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.configure(fg_color="transparent")

        self.inventory = InventoryFrame(self)
        self.orders = OrdersFrame(self)
        self.settings = SettingsFrame(self)

        self.switch_frames("inventory")
    
    def switch_frames(self, name):
        self.sidebar.inventoryButton.configure(fg_color=("gray75", "gray25") if name == "inventory" else "transparent")
        self.sidebar.ordersButton.configure(fg_color=("gray75", "gray25") if name == "orders" else "transparent")
        self.sidebar.settingsButton.configure(fg_color=("gray75", "gray25") if name == "settings" else "transparent")

        if name == "inventory":
            self.inventory.grid(row=0, column=1, sticky="nsew")
        else:
            self.inventory.grid_forget()
        
        if name == "orders":
            self.orders.grid(row=0, column=1, sticky="nsew")
        else:
            self.orders.grid_forget()
        
        if name == "settings":
            self.settings.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings.grid_forget()

    def inventoryFn(self):
        self.switch_frames("inventory")

    def ordersFn(self):
        self.switch_frames("orders")

    def settingsFn(self):
        self.switch_frames("settings")

def main():
    # Styles
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')

    # Run the app
    root = App()
    root.mainloop()

if __name__ == "__main__":
    main()