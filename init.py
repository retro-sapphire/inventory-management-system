# Python Libraries
import customtkinter as ctk
import mysql.connector as con
from dotenv import load_dotenv
import os

# App modules
from modules.sidebar import Sidebar
from modules.inventory import InventoryFrame
from modules.orders import OrdersFrame

load_dotenv(override=True)

cnx = con.connect(
    host=os.getenv("DB_DOMAIN"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    db=os.getenv("DB_NAME")
)
cur = cnx.cursor()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Grocery Management System")
        self.geometry("1200x800")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self, self.inventory_fn, self.orders_fn)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.configure(fg_color="transparent")

        self.inventory = InventoryFrame(self, cnx, cur)
        self.orders = OrdersFrame(self, cnx, cur)

        self.switch_frames("inventory")

    def switch_frames(self, name):
        self.sidebar.inventoryBtn.configure(fg_color=("gray75", "gray25") if name == "inventory" else "transparent")
        self.sidebar.ordersBtn.configure(fg_color=("gray75", "gray25") if name == "orders" else "transparent")

        if name == "inventory":
            self.inventory.grid(row=0, column=1, sticky="nsew")
        else:
            self.inventory.grid_forget()

        if name == "orders":
            self.orders.grid(row=0, column=1, sticky="nsew")
        else:
            self.orders.grid_forget()

    def inventory_fn(self):
        self.switch_frames("inventory")

    def orders_fn(self):
        self.switch_frames("orders")

def main():
    # Styles
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')

    # Run the app
    root = App()
    root.mainloop()


if __name__ == "__main__":
    main()
