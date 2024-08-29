import customtkinter as ctk

class OrdersFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tempLabel = ctk.CTkLabel(self, text="Orders! Yay!")
        self.tempLabel.grid(row=0, column=0)