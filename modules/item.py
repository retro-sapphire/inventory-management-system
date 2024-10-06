import customtkinter as ctk

from modules.spinbox import Spinbox


class Item(ctk.CTkFrame):
    def __init__(self, master, i, cnx, cur, callback):
        super().__init__(master)
        self.configure(fg_color="transparent")

        self.i = i
        self.cnx = cnx
        self.cur = cur
        self.callback = callback
        self.itemId = 0

        values = self.get_inventory()
        self.dropdown = ctk.CTkComboBox(self, values=[i[0] for i in values],
                                        variable=ctk.StringVar(),
                                        corner_radius=0, height=50, width=150,
                                        justify="center", command=self.on_dropdown_select,
                                        font=('Segoe UI', 20))
        self.dropdown.grid(row=0, column=0, sticky="nw", padx=10, pady=10)

        self.spinbox = Spinbox(self, max_val=1, width=150, height=50, callback=self.on_change)
        self.spinbox.grid(row=0, column=1, sticky="nw", padx=10, pady=10)

        self.priceLabel = ctk.CTkLabel(self, text="Price: ", font=('Segoe UI', 20))
        self.priceLabel.grid(row=0, column=2, sticky="e", padx=10, pady=10)

        self.price = ctk.StringVar()
        self.price.set("N/A")
        self.priceDisplay = ctk.CTkLabel(self, textvariable=self.price, font=('Segoe UI', 20))
        self.priceDisplay.grid(row=0, column=3, sticky="e", padx=10, pady=10)

    def get_inventory(self):
        self.cur.execute("SELECT name FROM INVENTORY;")
        return self.cur.fetchall()

    def on_dropdown_select(self, choice):
        self.cur.execute(f"SELECT quantity, itemId FROM INVENTORY WHERE name = '{choice}';")
        (self.spinbox.max_val, self.itemId) = self.cur.fetchone()

        self.on_change()

        if self.spinbox.get() > self.spinbox.max_val:
            self.spinbox.set(self.spinbox.max_val)

    def on_change(self, _ = None):
        name = self.dropdown.get()

        if self.spinbox.get() > self.spinbox.max_val:
            self.spinbox.set(self.spinbox.max_val)

        if name:
            self.cur.execute(f"SELECT price from INVENTORY where name = '{name}'")
            price_one = self.cur.fetchone()[0]
            self.price.set(price_one * self.spinbox.get())
            self.callback()
