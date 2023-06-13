import customtkinter as ctk
from utils import *

class Dashboard:
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.geometry('1300x800')
        self.root.title("Admin Dashboard")
        ctk.set_appearance_mode('dark')

        self.Title = ctk.CTkLabel(self.root, text="Admin Dashboard",font=('Arial',30))
        self.Title.pack(pady=30)

        self.center_frame = ctk.CTkFrame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')

        label = ctk.CTkLabel(
            self.center_frame,
            text='Loading...',
            font=('Arial',20)
            )
        label.pack()

        self.ProgressBar = ctk.CTkProgressBar(
            self.center_frame,
            orientation='horizontal',
            mode='determinate',
            progress_color='green',
            height=15,
            width=300,
        )
        self.ProgressBar.pack()
        self.ProgressBar.start()
        
        self.root.after(1000, self.initial_load_data) 
        self.root.mainloop()

    def initial_load_data(self):
        db_config = readDBConfig()
        if 'message' in list(db_config.keys()):
            log_error(db_config.get("message"))
        
        if mongo_check_db() is Exception:
            log_error(Exception)

        self.ProgressBar.set(1)
        self.ProgressBar.stop()
        self.clearPage()
        self.login()

    def clearPage(self):    
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.place_forget()

    def login(self)->None:
        label = ctk.CTkLabel(self.root,text='Login')
        label.pack()
        

Dashboard() 