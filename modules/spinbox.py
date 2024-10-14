import customtkinter as ctk


class Spinbox(ctk.CTkFrame):
    def __init__(self, master, max_val, width, height, callback):
        super().__init__(master, width=width, height=height)

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.max_val = max_val
        self.callback = callback

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = ctk.CTkButton(self, text="-", width=height - 6, height=height - 6,
                                             command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = ctk.CTkEntry(self, width=width - (2 * height), height=height - 6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")
        self.entry.bind("<Return>", self.callback)

        self.add_button = ctk.CTkButton(self, text="+", width=height - 6, height=height - 6,
                                        command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "1")

    def add_button_callback(self):
        try:
            value = int(self.entry.get())

            if value < self.max_val:
                self.entry.delete(0, "end")
                self.entry.insert(0, value+1)
            else:
                self.entry.delete(0, "end")
                self.entry.insert(0, self.max_val)
            self.callback()
        except ValueError:
            return

    def subtract_button_callback(self):
        try:
            value = int(self.entry.get())

            if value > 1:
                self.entry.delete(0, "end")
                self.entry.insert(0, value-1)
            self.callback()
        except ValueError:
            return

    def get(self):
        try:
            return float(self.entry.get())
        except ValueError:
            return

    def set(self, value):
        self.entry.delete(0, "end")
        self.entry.insert(0, int(value))
