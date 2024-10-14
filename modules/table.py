from tkinter import ttk

class Table(ttk.Treeview):
    def __init__(self, master, columns):
        super().__init__(master, columns=columns,
                         height=17,
                         selectmode='browse',
                         show='headings')
        style = ttk.Style()
        style.theme_use('default')
        style.configure('Treeview',
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=("Segoe UI", 11))
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=("Segoe UI", 16))
        style.map("Treeview.Heading",
                  background=[('active', '#3484F0')])
        self.bind('<Motion>', 'break')
