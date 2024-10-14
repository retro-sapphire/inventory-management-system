import os

import customtkinter as ctk
from PIL import Image

from modules.item import Item


class ItemsFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, cnx, cur, callback):
        super().__init__(master)
        self.items = []
        self.columnconfigure(0, weight=1)
        self.cnx = cnx
        self.cur = cur
        self.callback = callback

        images_path = "images/pngs"
        self.addImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "add-item.png")), size=(18, 20))
        self.delImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "del-item.png")), size=(18, 20))

        self.addProductBtn = ctk.CTkButton(self, text="Add Product",
                                           corner_radius=0, height=50, width=150, border_spacing=10,
                                           anchor="w", image=self.addImage, command=self.add_item,
                                           font=("Segoe UI", 15))
        self.addProductBtn.grid(row=0, column=0, sticky='nw', padx=10, pady=10)

    def add_item(self):
        item = Item(self, len(self.items), self.cnx, self.cur, self.callback)
        self.items.append(item)
        item.grid(row=item.i + 1, column=0, sticky='nw', padx=10, pady=10)

        def destroy():
            item.del_btn.destroy()
            self.del_item(item.i)

        item.del_btn = ctk.CTkButton(self, text="", corner_radius=0, height=50, width=50, fg_color="#a8324a",
                                     border_spacing=10, image=self.delImage, command=destroy)
        item.del_btn.grid(row=item.i + 1, column=1, sticky='nw', padx=10, pady=10)

    def del_item(self, i):
        for item in self.items.copy():
            if item.i == i:
                item.destroy()
                self.items.remove(item)
            elif item.i > i:
                item.i -= 1

                item.grid_forget()
                item.del_btn.grid_forget()

                item.grid(row=item.i + 1, column=0, sticky='nw', padx=10, pady=10)
                item.del_btn.grid(row=item.i + 1, column=1, sticky='nw', padx=10, pady=10)
        self.callback()
