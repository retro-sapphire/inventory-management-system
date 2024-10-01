import customtkinter as ctk
from PIL import Image
import os

class Sidebar(ctk.CTkFrame):
    def __init__(self, master, inventoryFn, ordersFn, settingsFn):
        super().__init__(master)
        self.rowconfigure(2, weight=1)

        images_path = "images"
        self.inventoryImage = ctk.CTkImage(light_image=Image.open(os.path.join(images_path, "boxes-light.png")),
                                           dark_image=Image.open(os.path.join(images_path, "boxes-dark.png")),
                                           size=(20, 20))
        self.ordersImage = ctk.CTkImage(light_image=Image.open(os.path.join(images_path, "clipboard-light.png")),
                                        dark_image=Image.open(os.path.join(images_path, "clipboard-dark.png")),
                                        size=(20, 20))
        self.settingsImage = ctk.CTkImage(light_image=Image.open(os.path.join(images_path, "gears-light.png")),
                                          dark_image=Image.open(os.path.join(images_path, "gears-dark.png")),
                                          size=(20, 20))

        self.inventoryButton = ctk.CTkButton(self, text="Inventory", 
                                             corner_radius=0, height=40, border_spacing=10,
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             hover_color=("gray70", "gray30"), anchor="w",
                                             image=self.inventoryImage, command=inventoryFn)
        self.inventoryButton.grid(row=0, column=0, sticky="ew", padx=20, pady=10)
        
        self.ordersButton = ctk.CTkButton(self, text="Orders", 
                                          corner_radius=0, height=40, border_spacing=10,
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          hover_color=("gray70", "gray30"), anchor="w",
                                          image=self.ordersImage, command=ordersFn)
        self.ordersButton.grid(row=1, column=0, sticky="ew", padx=20, pady=10)

        self.settingsButton = ctk.CTkButton(self, text="Settings", 
                                            corner_radius=0, height=40, border_spacing=10,
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"), anchor="w",
                                            image=self.settingsImage, command=settingsFn)
        self.settingsButton.grid(row=2, column=0, sticky="s", padx=20, pady=10)

