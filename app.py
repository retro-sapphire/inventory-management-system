# Python Libraries
import customtkinter as ctk
import mysql.connector as con
from dotenv import load_dotenv
import os


# App modules
from modules.sidebar import Sidebar
from modules.inventory import InventoryFrame
from modules.orders import OrdersFrame
from modules.view_orders import ViewOrdersFrame

load_dotenv(override=True)

cnx = con.connect(
    host=os.getenv("DB_DOMAIN"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    db=os.getenv("DB_NAME")
)
cur = cnx.cursor()


class App(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self, self.inventory_fn, self.orders_fn, self.view_orders_fn)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.configure(fg_color="transparent")

        self.inventory = InventoryFrame(self, cnx, cur)
        self.orders = OrdersFrame(self, cnx, cur)
        self.view_orders = ViewOrdersFrame(self, cnx, cur)

        self.switch_frames("inventory")

    def switch_frames(self, name):
        self.sidebar.inventoryBtn.configure(fg_color=("gray75", "gray25") if name == "inventory" else "transparent")
        self.sidebar.ordersBtn.configure(fg_color=("gray75", "gray25") if name == "orders" else "transparent")
        self.sidebar.viewOrdersBtn.configure(fg_color=("gray75", "gray25") if name == "view_orders" else "transparent")

        if name == "inventory":
            self.inventory.grid(row=0, column=1, sticky="nsew")
            self.inventory.load_inventory()
        else:
            self.inventory.grid_forget()

        if name == "orders":
            self.orders.grid(row=0, column=1, sticky="nsew")
        else:
            self.orders.grid_forget()
        
        if name == "view_orders":
            self.view_orders.grid(row=0, column=1, sticky="nsew")
        else:
            self.view_orders.grid_forget()

    def inventory_fn(self):
        self.switch_frames("inventory")

    def orders_fn(self):
        self.switch_frames("orders")

    def view_orders_fn(self):
        self.switch_frames("view_orders")
