# Python Libraries
import customtkinter as ctk
import mysql.connector as con
from dotenv import load_dotenv
import os
from PIL import Image, ImageTk

# App modules
from app import App

class Index(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Grocery Management System")
        self.geometry("1200x800")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        images_path = "images/pngs"
        self.logoImg = ctk.CTkImage(dark_image=Image.open(os.path.join(images_path, "logo.png")), size=(512,512))
        self.logoLbl = ctk.CTkLabel(self, image=self.logoImg, text=None)
        self.logoLbl.grid(row=0, column=0, sticky="n", pady=(150, 0))
        self.nameLbl = ctk.CTkLabel(self, text="Rishab Arora XII B", font=('Segoe UI', 20))
        self.nameLbl.grid(row=1, column=0, sticky="nsew", pady=(50, 0))
        self.loginBtn = ctk.CTkButton(self, text="Login",
                                       corner_radius=0, height=50, width=150, border_spacing=10,
                                       anchor="c", command=self.login,
                                       font=("Segoe UI", 15)
                                        )
        self.loginBtn.grid(row=2, column=0, sticky='n', padx=10, pady=10)
        
        self.app = App(self)  

    def login(self):
        self.logoLbl.grid_forget()
        self.loginBtn.grid_forget()
        self.app.grid(row=0, column=0, sticky="nsew")

def main():
    # Styles
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')
    root = Index()
    root.mainloop()


if __name__ == "__main__":
    main()
