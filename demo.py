import customtkinter

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("960x540")
        self.title("CTk example")
        self.minsize(960, 540)
        #self.maxsize(960, 540) //nên để free
        
        #chia window làm 2 frame
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = customtkinter.CTkFrame(
            master = self,
            width=500
        )
        self.left_frame.grid(row=0, column=0, sticky="nswe",padx = 10,pady = 10)

        self.right_frame = customtkinter.CTkFrame(
            master = self
        )
        self.right_frame.grid(row=0, column=1, sticky="nswe",padx = 10,pady = 10)

        #------------Left-Side Menu (frame_left)---------------#

        self.label_title = customtkinter.CTkLabel(master=self.left_frame, text="Electricity Production By Source")
        self.label_title.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.country_menu = customtkinter.CTkOptionMenu(
            master=self.left_frame,
            width=200,
            values=['Vietnam','Indonesia'] #chỉnh lại bằng 1 list bên ngoài, import bằng json
        )
        self.country_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        self.varyear1 = customtkinter.IntVar
        self.varyear2 = customtkinter.IntVar

        self.left_textbox = customtkinter.CTkFrame(
            master= self.left_frame,
        )
        self.left_textbox.grid(row=2, column=0, sticky="nswe",padx = 10,pady = 10)
        
        self.label_title = customtkinter.CTkLabel(master=self.left_textbox, text="year start")
        self.label_title.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        self.label_entry = customtkinter.CTkEntry(master= self.left_textbox )
        self.label_entry.grid(row=2, column=2, sticky="nswe",padx = 10,pady = 10)

        
        self.left_textbox = customtkinter.CTkFrame(
            master= self.left_frame,
        )
        self.left_textbox.grid(row=3, column=0, sticky="nswe",padx = 10,pady = 10)
        
        self.label_title = customtkinter.CTkLabel(master=self.left_textbox, text="year end")
        self.label_title.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        self.label_entry = customtkinter.CTkEntry(master= self.left_textbox )
        self.label_entry.grid(row=2, column=2, sticky="nswe",padx = 10,pady = 10)

        

        self.btn_settings = customtkinter.CTkButton(
            master=self.left_frame,
            text="Adjust Data",
        )
        self.btn_settings.grid(row=4, column=0, pady=(5, 10), padx=5)

        #------------Right-Side Menu (frame_left)---------------#






app = App()
app.mainloop()