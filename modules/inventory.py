import customtkinter as ctk
from PIL import Image
import os
from modules.table import Table


class InventoryFrame(ctk.CTkFrame):
    def __init__(self, master, cnx, cur):
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.cnx = cnx
        self.cur = cur

        self.table = Table(self, columns=("id", "name", "price", "quantity", "createdAt", "modifiedAt"))

        self.table.column("id", anchor="c", minwidth=30, width=30)
        self.table.column("name", anchor="c", minwidth=220, width=220)
        self.table.column("price", anchor="c", minwidth=120, width=120)
        self.table.column("quantity", anchor="c", minwidth=120, width=120)
        self.table.column("createdAt", anchor="c", minwidth=120, width=120)
        self.table.column("modifiedAt", anchor="c", minwidth=120, width=120)

        self.table.heading('id', text='ID')
        self.table.heading('name', text='Item Name')
        self.table.heading('price', text='Price')
        self.table.heading('quantity', text='Quantity')
        self.table.heading('createdAt', text='Created At')
        self.table.heading('modifiedAt', text='Modified At')

        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        images_path = "images/pngs"
        self.addImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "add-item.png")), size=(18, 20))
        self.addBtn = ctk.CTkButton(self, text="Add Product",
                                    corner_radius=0, height=40, border_spacing=10,
                                    anchor="w", image=self.addImage, command=self.show_popup,
                                    font=("Segoe UI", 15))
        self.addBtn.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        self.load_inventory()

    def load_inventory(self):
        for i in self.table.get_children():
            self.table.delete(i)

        self.cur.execute(f"SELECT * FROM INVENTORY;")
        for i in self.cur.fetchall():
            self.table.insert("", "end", values=i)

    def add_item(self, name, price, quantity):
        self.cur.execute(f"INSERT INTO INVENTORY (name, price, quantity) VALUES ('{name}', {price}, {quantity})")
        self.cnx.commit()

    def show_popup(self):
        dialog = ctk.CTkToplevel(self.master)
        dialog.geometry("350x400")
        dialog.title("Add Item")

        item_name_label = ctk.CTkLabel(dialog, text="Item Name:")
        item_name_label.pack(pady=(20, 5))

        item_name_entry = ctk.CTkEntry(dialog)
        item_name_entry.pack(pady=5)

        price_label = ctk.CTkLabel(dialog, text="Price of Item:")
        price_label.pack(pady=(10, 5))

        price_entry = ctk.CTkEntry(dialog)
        price_entry.pack(pady=5)

        quantity_label = ctk.CTkLabel(dialog, text="Quantity of Item:")
        quantity_label.pack(pady=(10, 5))

        quantity_entry = ctk.CTkEntry(dialog)
        quantity_entry.pack(pady=5)

        def handle_submit():
            self.add_item(item_name_entry.get(), price_entry.get(), quantity_entry.get())
            self.load_inventory()
            dialog.destroy()

        submit_btn = ctk.CTkButton(dialog, text="Submit", command=handle_submit)
        submit_btn.pack(pady=20)