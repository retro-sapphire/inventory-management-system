import customtkinter as ctk
from PIL import Image
import os
from modules.table import Table
from tkinter import ttk

class ViewOrdersFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, cnx, cur):
        super().__init__(master)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.cnx = cnx
        self.cur = cur

        users = [i[0] for i in self.get_users()]
        self.users_dropdown_label = ctk.CTkLabel(self, text="Select User", font=('Segoe UI', 20))
        self.users_dropdown_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.users_dropdown = ctk.CTkComboBox(self, values=users,
                                              variable=ctk.StringVar(),
                                              corner_radius=0, height=50, width=150,
                                              justify="center", command=self.load_orders,
                                              font=('Segoe UI', 20))
        self.users_dropdown.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

        
        self.columns = ("Order ID", "Product", "Quantity", "Price", "Order Date")
        self.order_table = Table(self, columns=self.columns)

    def get_users(self):
        self.cur.execute("SELECT name FROM USERS;")
        return self.cur.fetchall()

    def load_orders(self, user_name):
        self.order_table.grid_forget()
        for i in self.order_table.get_children():
            self.order_table.delete(i)

        # Query to fetch all order details along with user info
        query = f'''
        SELECT ORDERS.orderId, INVENTORY.name, ORDER_PRODUCTS.quantity, 
               INVENTORY.price, ORDERS.createdAt
        FROM ORDERS
        JOIN USERS ON ORDERS.userId = USERS.userId
        JOIN ORDER_PRODUCTS ON ORDERS.orderId = ORDER_PRODUCTS.orderId
        JOIN INVENTORY ON ORDER_PRODUCTS.itemId = INVENTORY.itemId
        WHERE USERS.name = "{user_name}"
        ORDER BY ORDERS.orderId;
        ''' 
        
        # Execute the query
        self.cur.execute(query)
        order_data = self.cur.fetchall()

        # Group data by order ID
        for row in order_data:
            for col in self.columns:
                self.order_table.column(col, anchor="c", minwidth=30, width=120)
                self.order_table.heading(col, text=col)
                self.order_table.column(col, width=150)

            # Insert the row data into the corresponding order's table
            self.order_table.insert("", "end", values=row)
        self.order_table.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)
