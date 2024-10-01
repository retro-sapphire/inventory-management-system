import customtkinter as ctk

class SettingsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.tempLabel = ctk.CTkLabel(self, text="Settings! Yay!")
        self.tempLabel.grid(row=0, column=0)