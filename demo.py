import customtkinter
from CTkRangeSlider import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
from data_manager import *

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("blue")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title("Dashboard")
        
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

        #------------Left-Side (frame_left)---------------#

        self.label_title = customtkinter.CTkLabel(master=self.left_frame, text="Electricity Production By Source")
        self.label_title.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.country = customtkinter.StringVar
        self.country_menu = customtkinter.CTkOptionMenu(
            master=self.left_frame,
            width=200,
            values=Get_Country_Data('data.json').Get_Country_Name(),
        )
        self.country_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.varyearstart = customtkinter.IntVar(value=2000)
        self.varyearend = customtkinter.IntVar(value=2023)

        self.left_textbox = customtkinter.CTkFrame(
            master= self.left_frame,
        )
        self.left_textbox.grid(row=2, column=0, sticky="nswe",padx = 10,pady = 10)
        

        self.slider = CTkRangeSlider(master= self.left_textbox, from_=2000, to=2023,number_of_steps=38,variables = [self.varyearstart, self.varyearend],width=150)
        self.slider.grid(row=2, column=2, sticky="nswe",padx = 10,pady = 10)
        self.label_sliderstart = customtkinter.CTkLabel(master=self.left_textbox, textvariable = self.varyearstart,height = 20)
        self.label_sliderstart.grid(row=2, column=1, sticky="nsew", padx=10, pady=10)
        self.label_sliderend = customtkinter.CTkLabel(master=self.left_textbox, textvariable = self.varyearend,height = 20)
        self.label_sliderend.grid(row=2, column=3, sticky="nsew", padx=10, pady=10)

        self.btn_update = customtkinter.CTkButton(
            master= self.left_frame,
            text = 'Update',
            command = self.update_handle
        )
        self.btn_update.grid(row=4, column=0, pady=(5, 10), padx=5)

        self.btn_settings = customtkinter.CTkButton(
            master=self.left_frame,
            text="Adjust Data",
            command=self.open_toplevel
        )

        self.btn_settings.grid(row=6, column=0, pady=(5, 10), padx=5)
        #------------Right-Side (frame_right)---------------#
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)
        
        self.tab_view = MyTabView(master=self.right_frame,height = 1080,width = 1920,country= self.country_menu.get(),years=self.slider.get())
        self.tab_view.grid(row=0, column=0)

    def update_handle(self):
        """Xử lý cập nhật bảng khi bấm nút Update Table."""
        # Lấy giá trị mới từ các widget
        selected_country = self.country_menu.get()
        selected_years = self.slider.get()

        # Cập nhật dữ liệu trong MyTabView
        self.tab_view.country = selected_country
        self.tab_view.years = selected_years
        self.tab_view.update_table()

        # Cập nhật biểu đồ
        yeargraph,other,Bioenergy,Solar,Wind, Hydro,Nuclear,Old,Gas,Coal = Get_Country_Data('data.json').Get_Data_From_Year_to_Year_Graph(str(selected_country),str(int(selected_years[0])),str(int(selected_years[1])))

        self.tab_view.update_graph(yeargraph,other,Bioenergy,Solar,Wind, Hydro,Nuclear,Old,Gas,Coal)


    def open_toplevel(self):
        """Khởi tạo cửa sổ phụ"""
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)
            self.toplevel_window.title("Adjust Data")
        else:
            self.toplevel_window.focus()


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.geometry("300x220")
        self.create_widgets()
    def create_widgets(self):
        self.label_country = customtkinter.CTkLabel(self, text="Country :")
        self.label_country.grid(row=1, column=0, pady=(5, 10), padx=5)

        self.country_var = customtkinter.StringVar()
        self.country_menu = customtkinter.CTkOptionMenu(self, 
            variable=self.country_var, 
            values=Get_Country_Data('data.json').Get_Country_Name()
        )
        self.country_menu.grid(row=1, column=1, pady=(5, 10), padx=5)

        self.label_year = customtkinter.CTkLabel(self, text="Year :")
        self.label_year.grid(row=2, column=0, pady=(5, 10), padx=5)

        self.year_var = customtkinter.StringVar()
        self.year_menu = customtkinter.CTkOptionMenu(self, 
            variable=self.year_var, 
            values=[str(year) for year in range(2000, 2024)]  
        )
        self.year_menu.grid(row=2, column=1, pady=(5, 10), padx=5)

        self.label_source = customtkinter.CTkLabel(self, text="Type of Source : ")
        self.label_source.grid(row=3, column=0, pady=(5, 10), padx=5)

        self.source_var = customtkinter.StringVar()
        self.source_menu = customtkinter.CTkOptionMenu(self, 
            variable=self.source_var, 
            values=["Other", "Bioenergy", "Solar", "Wind", "Hydro", "Nuclear", "Oil", "Gas", "Coal"]
        )
        self.source_menu.grid(row=3, column=1, pady=(5, 10), padx=5)
       
        self.label_value = customtkinter.CTkLabel(self, text="Value : ")
        self.label_value.grid(row=4, column=0, pady=(5, 10), padx=5)

        self.value_entry = customtkinter.CTkEntry(self)
        self.value_entry.grid(row=4, column=1, pady=(5, 10), padx=5)
        
        self.btn_delete = customtkinter.CTkButton(self, text="Delete" )
        self.btn_edit = customtkinter.CTkButton(self, text="Edit")
        
        self.btn_delete.grid(row=5, column=0, pady=(5, 10), padx=5)
        self.btn_edit.grid(row=5, column=1, pady=(5, 10), padx=5)

class MyTabView(customtkinter.CTkTabview):
    def __init__(self,master,years,country,**kwargs):
        super().__init__(master,**kwargs)
        #=============table==============
        self.add("Table")
        self.tab("Table").grid_columnconfigure(0, weight=1)
        self.tab("Table").grid_rowconfigure(0, weight=1)

        self.years = years
        self.country = country

        self.current_page = 1
        self.numberrowofpage=20
        #style bảng
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview.Heading", font=("Arial", 16, "bold"),background="#565b5e",foreground="white",relief="flat")  # Kích thước chữ của tiêu đề cột
        style.configure("Treeview",background="#2a2d2e",foreground="white",rowheight=40,fieldbackground="#343638",bordercolor="#343638",borderwidth=0,font=("Arial", 14))
        style.map('Treeview', background=[('selected', '#22559b')])
        style.configure("Treeview.Heading",background="#565b5e",foreground="white",relief="flat")
        style.map("Treeview.Heading",background=[('active', '#3484F0')])
        #tạo bảng
        self.tree = ttk.Treeview(self.tab("Table"), columns=("Column1", "Column2", "Column3","Column4","Column5","Column6","Column7","Column8","Column9","Column10","Column11"), show="headings",height =  self.numberrowofpage)
        self.tree.heading("Column1", text="Entity")
        self.tree.heading("Column2", text="Year")
        self.tree.heading("Column3", text="Other")
        self.tree.heading("Column4", text="Bioenergy")
        self.tree.heading("Column5", text="Solar")
        self.tree.heading("Column6", text="Wind")
        self.tree.heading("Column7", text="Hydro")
        self.tree.heading("Column8", text="Nuclear")
        self.tree.heading("Column9", text="Oil")
        self.tree.heading("Column10", text="Gas")
        self.tree.heading("Column11", text="Coal")
        # Đặt kích thước cột
        self.tree.column("Column1", width=200,stretch=False)
        self.tree.column("Column2", width=120,stretch=False)
        self.tree.column("Column3", width=120,stretch=False)
        self.tree.column("Column4", width=120,stretch=False)
        self.tree.column("Column5", width=120,stretch=False)
        self.tree.column("Column6", width=120,stretch=False)
        self.tree.column("Column7", width=120,stretch=False)
        self.tree.column("Column8", width=120,stretch=False)
        self.tree.column("Column9", width=120,stretch=False)
        self.tree.column("Column10", width=120,stretch=False)
        self.tree.column("Column11", width=120,stretch=False)
        # Thêm dữ liệu vào bảng

        self.data = Get_Country_Data('data.json').Get_Data_From_Year_to_Year(str(self.country),str(int(self.years[0])),str(int(self.years[1])))
        for row in self.data:
            self.tree.insert("", "end", values=row)

        # Hiển thị Treeview trong Frame
        self.tree.grid(row = 0, column = 0)
        self.control_frame = customtkinter.CTkFrame(self.tab("Table"))
        self.control_frame.grid(row=1, column=0)

        self.prev_button = customtkinter.CTkButton(self.control_frame, text="Previous",command=self.prev_page)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = customtkinter.CTkButton(self.control_frame, text="Next",command=self.next_page)
        self.next_button.grid(row=0, column=2, padx=5)

        self.page_label = customtkinter.CTkLabel(self.control_frame, text="Page 1")
        self.page_label.grid(row=0, column=1, padx=5)
        #=============Graph==============
        self.add("Graph")
        self.tab("Graph").grid_columnconfigure(0, weight=1)
        self.tab("Graph").grid_rowconfigure(0, weight=1)
        
        self.yeargraph,self.other,self.Bioenergy,self.Solar,self.Wind, self.Hydro,self.Nuclear,self.Old,self.Gas,self.Coal = Get_Country_Data('data.json').Get_Data_From_Year_to_Year_Graph(str(self.country),str(int(self.years[0])),str(int(self.years[1])))
        self.fig = Figure(figsize=(17, 10))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab("Graph"))
        self.update_graph(self.yeargraph,self.other,self.Bioenergy,self.Solar,self.Wind, self.Hydro,self.Nuclear,self.Old,self.Gas,self.Coal)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0)
 

    def update_table(self):
        self.data = Get_Country_Data('data.json').Get_Data_From_Year_to_Year(str(self.country),str(int(self.years[0])),str(int(self.years[1])))
        self.current_page = 1  # Reset về trang đầu tiên
        self.show_page(self.current_page)

    def show_page(self, page):
        """Hiển thị dữ liệu của trang hiện tại."""
        # Xóa dữ liệu cũ trong bảng
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Lấy dữ liệu cho trang hiện tại
        start_index = (page - 1) * self.numberrowofpage
        end_index = start_index + self.numberrowofpage
        page_data = self.data[start_index:end_index]

        # Thêm dữ liệu vào bảng
        for row in page_data:
            self.tree.insert("", "end", values=row)

        # Cập nhật nhãn số trang
        self.page_label.configure(text=f"Page {page}")

    def prev_page(self):
        """Chuyển sang trang trước."""
        if self.current_page > 1:
            self.current_page -= 1
            self.show_page(self.current_page)

    def next_page(self):
        """Chuyển sang trang tiếp theo."""
        if self.current_page < (len(self.data) - 1) // self.numberrowofpage + 1:
            self.current_page += 1
            self.show_page(self.current_page)

    def update_graph(self, years, other, bioenergy, solar, wind, hydro, nuclear, oil, gas, coal):
        """Cập nhật và hiển thị biểu đồ."""
        self.ax.clear()
        if not years:
            self.ax.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=16)
        else:
            # Cấu hình biểu đồ
            self.ax.set_title(f'SẢN LƯỢNG ĐIỆN THEO NGUỒN SẢN XUẤT TỪ NĂM {years[0]} ĐẾN NĂM {years[-1]} của {self.country}', fontsize=14)
            self.ax.set_xlabel('Năm')
            self.ax.set_ylabel('Sản lượng điện sản xuất được (TWh)')
            self.ax.set_xticks(years)
            self.ax.grid(True, linestyle='--', alpha=0.7)

            # Vẽ từng loại năng lượng
            self.ax.plot(years, other, marker='o', markerfacecolor='black', color='black', label='Other')
            self.ax.plot(years, bioenergy, marker='o', markerfacecolor='red', color='red', label='Bioenergy')
            self.ax.plot(years, solar, marker='o', markerfacecolor='blue', color='blue', label='Solar')
            self.ax.plot(years, wind, marker='o', markerfacecolor='yellow', color='yellow', label='Wind')
            self.ax.plot(years, hydro, marker='o', markerfacecolor='grey', color='grey', label='Hydro')
            self.ax.plot(years, nuclear, marker='o', markerfacecolor='magenta', color='magenta', label='Nuclear')
            self.ax.plot(years, oil, marker='o', markerfacecolor='green', color='green', label='Oil')
            self.ax.plot(years, gas, marker='o', markerfacecolor='cyan', color='cyan', label='Gas')
            self.ax.plot(years, coal, marker='o', markerfacecolor='orange', color='orange', label='Coal')

            self.ax.legend(loc='upper left', fontsize=10)

        self.canvas.draw()

app = App()
app.mainloop()
