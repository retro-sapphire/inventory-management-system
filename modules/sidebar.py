import customtkinter as ctk
from PIL import Image
import os

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, inventory_fn, orders_fn, view_orders_fn):
        super().__init__(master)

        images_path = "images/pngs"
        self.inventoryImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "boxes.png")), size=(25, 20))
        self.clockImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "clock.png")), size=(20, 20))
        self.ordersImage = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "clipboard.png")), size=(15, 20))
      
        self.inventoryBtn = ctk.CTkButton(self, text="Inventory",
                                          corner_radius=0, height=40, border_spacing=10, font=("Segoe UI", 13),
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          hover_color=("gray70", "gray30"), anchor="w",
                                          image=self.inventoryImage, command=inventory_fn)
        self.inventoryBtn.grid(row=0, column=0, sticky="ew", padx=20, pady=10)

        self.ordersBtn = ctk.CTkButton(self, text="Create Orders",
                                       corner_radius=0, height=40, border_spacing=10, font=("Segoe UI", 13),
                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                       hover_color=("gray70", "gray30"), anchor="w",
                                       image=self.ordersImage, command=orders_fn)
        self.ordersBtn.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        self.viewOrdersBtn = ctk.CTkButton(self, text="View Orders",
                                       corner_radius=0, height=40, border_spacing=10, font=("Segoe UI", 13),
                                       fg_color="transparent", text_color=("gray10", "gray90"),
                                       hover_color=("gray70", "gray30"), anchor="w",
                                       image=self.clockImage, command=view_orders_fn)
        self.viewOrdersBtn.grid(row=2, column=0, sticky="ew", padx=20, pady=10)
