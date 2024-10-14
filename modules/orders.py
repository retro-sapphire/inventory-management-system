import customtkinter as ctk
from PIL import Image
import os
from modules.items_frame import ItemsFrame


class OrdersFrame(ctk.CTkFrame):
    def __init__(self, master, cnx, cur):
        super().__init__(master)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)

        self.cnx = cnx
        self.cur = cur

        self.address = ctk.StringVar()
        self.addressLabel = ctk.CTkLabel(self, textvariable=self.address,
                                         height=50, width=200,
                                         font=('Segoe UI', 20))
        self.addressLabel.grid(row=1, column=1, sticky="ne", padx=10, pady=10, columnspan=3)

        self.users = self.get_users()
        self.users_dropdown_label = ctk.CTkLabel(self, text="Select User", font=('Segoe UI', 20))
        self.users_dropdown_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.users_dropdown = ctk.CTkComboBox(self, values=[i[0] for i in self.users],
                                              variable=ctk.StringVar(),
                                              corner_radius=0, height=50, width=150,
                                              justify="center", command=self.load_address,
                                              font=('Segoe UI', 20))
        self.users_dropdown.grid(row=1, column=0, sticky="nw", padx=10, pady=10)

        self.net_price = ctk.StringVar()
        self.itemsFrame = ItemsFrame(self, cnx, cur, self.set_net_price)
        self.itemsFrame.grid(row=2, column=0, sticky="nsew", padx=10, pady=10, columnspan=4)

        self.priceLabel = ctk.CTkLabel(self, text="Total Price: ", height=50, font=('Segoe UI', 20))
        self.priceLabel.grid(row=3, column=1, sticky="sw", padx=10, pady=10)

        self.priceDisplay = ctk.CTkLabel(self, textvariable=self.net_price, height=50, font=('Segoe UI', 20))
        self.priceDisplay.grid(row=3, column=2, sticky="se", padx=10, pady=10)

        images_path = "images/pngs"
        self.submitImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "submit.png")), size=(15, 20))
        self.submitBtn = ctk.CTkButton(self, text="Submit",
                                       corner_radius=0, height=50, width=150, border_spacing=10,
                                       anchor="w", image=self.submitImage, command=self.submit,
                                       font=("Segoe UI", 15))
        self.submitBtn.grid(row=3, column=3, sticky='se', padx=10, pady=10)

    def get_users(self):
        self.cur.execute("SELECT name, shipping_address FROM USERS;")
        return self.cur.fetchall()

    def load_address(self, choice):
        for i in self.users:
            if choice == i[0]:
                self.address.set("Address: " + i[1])
                break

    def set_net_price(self):
        net_price = 0
        for i in self.itemsFrame.items:
            if i.price.get() != "N/A":
                net_price += int(i.price.get()[:-2])
        self.net_price.set(net_price)

    def insert_order(self, user_id):
        self.cur.execute(f"INSERT INTO ORDERS(userId) VALUES({user_id})")
        self.cnx.commit()

    def insert_order_products(self, order_id):
        for i in self.itemsFrame.items.copy():
            self.cur.execute(f"INSERT INTO ORDER_PRODUCTS(orderId, itemId, quantity) VALUES({order_id}, {i.itemId}, {i.spinbox.get()});")
            self.cur.execute(f"UPDATE INVENTORY SET quantity = quantity - {i.spinbox.get()} WHERE itemId = {i.itemId};")

            i.del_btn.destroy()
            self.itemsFrame.del_item(i.i)
            self.cnx.commit()

    def submit(self):
        self.cur.execute(f"SELECT userId FROM USERS WHERE name = '{self.users_dropdown.get()}';")
        user_id = self.cur.fetchone()[0]

        self.insert_order(user_id)

        self.cur.execute(f"SELECT orderId FROM ORDERS WHERE userId = {user_id}")
        order_id = self.cur.fetchall()[-1][0]

        self.insert_order_products(order_id)
