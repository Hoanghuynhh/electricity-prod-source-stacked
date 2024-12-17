import os
from convert_data import *
import customtkinter
from CTkRangeSlider import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
from tkinter import messagebox
from GetCountryData import *
from CountryDataManager import *
from findmenu import *

path = 'data/data.json'
if os.path.exists(path) == False:
    Convert_data.convert()

customtkinter.set_appearance_mode("Dark") 
customtkinter.set_default_color_theme("blue")

class AdjustDataWindow(customtkinter.CTkToplevel):
    def __init__(self,country,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.loader = Country_Data_Manager("data/data.json")
        self.loaderdata = Get_Country_Data("data/data.json")
        self.geometry("300x170")
        self.country_var = country
        self.title(f"{self.country_var} Adjust Data")
        self.label_year = customtkinter.CTkLabel(self, text="Year :")
        self.label_year.grid(row=2, column=0, pady=(5, 10), padx=5)
        self.year_menu = customtkinter.CTkOptionMenu(self, 
            values=['All']+self.loaderdata.Get_Year_of_one_Country(self.country_var)
        )
        self.year_menu.grid(row=2, column=1, pady=(5, 10), padx=5)

        self.label_source = customtkinter.CTkLabel(self, text="Type of Source : ")
        self.label_source.grid(row=3, column=0, pady=(5, 10), padx=5)
        self.source_menu = customtkinter.CTkOptionMenu(self, 
            values=["All","Other", "Bioenergy", "Solar", "Wind", "Hydro", "Nuclear", "Oil", "Gas", "Coal"]
        )
        self.source_menu.grid(row=3, column=1, pady=(5, 10), padx=5)
       
        self.label_value = customtkinter.CTkLabel(self, text="Value : ")
        self.label_value.grid(row=4, column=0, pady=(5, 10), padx=5)

        self.value_entry = customtkinter.CTkEntry(self)
        self.value_entry.grid(row=4, column=1, pady=(5, 10), padx=5)
        
        self.btn_delete = customtkinter.CTkButton(self, text="Delete",command=self.delete)
        self.btn_edit = customtkinter.CTkButton(self, text="Edit",command = self.edit)
        
        self.btn_delete.grid(row=5, column=0, pady=(5, 10), padx=5)
        self.btn_edit.grid(row=5, column=1, pady=(5, 10), padx=5)

    def edit(self):
        year_edit = self.year_menu.get()
        source_edit = self.source_menu.get()
        entry_edit = self.value_entry.get()
        if year_edit == '' and source_edit == '':
            messagebox.showwarning(message="Please select a year and a type of source to edit !",title = 'WARNING')
        elif year_edit == '':
            messagebox.showwarning(message="Please select a year to edit !",title = 'WARNING')
        elif source_edit == '':
            messagebox.showwarning(message="Please select a type of source to edit !",title = 'WARNING')
        elif entry_edit == '':
            messagebox.showwarning(message="Please add a value to edit !",title = 'WARNING')
        elif year_edit == 'All':
            messagebox.showwarning(message="Please select a year except All !",title = 'WARNING')
        else:
            if source_edit == 'All':
                messagebox.showwarning(message="Please choose one type of source except All !",title = 'WARNING')
            else:
                if entry_edit.isdigit():
                    ans = messagebox.askyesno(title="Confirm",message=f"Do you want to change the value of {source_edit} source in {year_edit} is {entry_edit} ?")
                    if ans:
                        self.loader.update_data(country_name=self.country_var,year=year_edit,energy_type=source_edit,new_value=entry_edit)
                        self.destroy()
                        messagebox.showinfo("Status","Success !")
                else:
                    messagebox.showwarning(message="Value must be number",title = 'WARNING')
            
    def delete(self):
        year_edit = self.year_menu.get()
        source_edit = self.source_menu.get()
        if year_edit == '' and source_edit == '':
            messagebox.showwarning(message="Please select a year and a type of source to delete !",title = 'WARNING')
        elif year_edit == '':
            messagebox.showwarning(message="Please select a year to delete !",title = 'WARNING')
        elif source_edit == '':
            messagebox.showwarning(message="Please select a type of source to delete !",title = 'WARNING')
        elif year_edit == 'All' and source_edit != "All":
            ans = messagebox.askyesno(title="Confirm",message=f"Do you want to delete {source_edit}'s values in all years ?")
            if ans:
                self.loader.delete_all_data_energy_type(country_name=self.country_var,energy_type=source_edit)
                self.destroy()
                messagebox.showinfo("Status","Success !")
        elif year_edit == "All" and source_edit == "All":
            ans = messagebox.askyesno(title="Confirm",message=f"Do you want to delete all the values of {self.country_var} ?")
            if ans:
                self.loader.delete_data_country(self.country_var)
                self.destroy()
                messagebox.showinfo("Status","Success !")
        elif year_edit != "All" and source_edit == "All":
            ans = messagebox.askyesno(title="Confirm",message=f"Do you want to delete all the values in {year_edit} ?")
            if ans:
                self.loader.delete_data_year(country_name=self.country_var,year=year_edit)
                self.destroy()
                messagebox.showinfo("Status","Success !")
        elif year_edit != "All" and source_edit != "All":
            ans = messagebox.askyesno(title="Confirm",message=f"Do you want to delete {source_edit}'s values in {year_edit} ?")
            if ans:
                self.loader.delete_data_energy(country_name=self.country_var,year = year_edit, energy_type=source_edit)
                self.destroy()
                messagebox.showinfo("Status","Success !")

class AddDataWindow(customtkinter.CTkToplevel):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.loader = Country_Data_Manager("data/data.json")
        self.geometry("300x620")
        self.title("Add new data")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.label_country = customtkinter.CTkLabel(self, text="Country:")
        self.label_country.grid(row=0, column=0,sticky="nsew", pady=10, padx=10)
        self.country_entry = customtkinter.CTkEntry(self)
        self.country_entry.grid(row=0, column=1,sticky="nsew", pady=10, padx=10)
        self.label_year = customtkinter.CTkLabel(self,text="Year:")
        self.year = customtkinter.IntVar(value = 1985)
        self.label_year.grid(row = 1,column = 0, sticky = "nsew", pady = 10,padx = 10)
        self.year_slider = customtkinter.CTkSlider(self,from_=1985, to=2024,variable=self.year,number_of_steps= 39)
        self.year_slider.grid(row = 1,column = 1,sticky = 'nsew',pady = 10,padx =10)
        self.label_yearstatus = customtkinter.CTkLabel(self,textvariable = self.year)
        self.label_yearstatus.grid(row = 2,columnspan = 2)
        self.label_other = customtkinter.CTkLabel(self, text="Other:")
        self.label_other.grid(row=3, column=0,sticky="nsew", pady=10, padx=10)
        self.other_entry = customtkinter.CTkEntry(self)
        self.other_entry.grid(row=3, column=1,sticky="nsew", pady=10, padx=10)

        self.label_bio = customtkinter.CTkLabel(self, text="Bioenergy:")
        self.label_bio.grid(row=4, column=0,sticky="nsew", pady=10, padx=10)
        self.bio_entry = customtkinter.CTkEntry(self)
        self.bio_entry.grid(row=4, column=1,sticky="nsew", pady=10, padx=10)

        self.label_solar = customtkinter.CTkLabel(self, text="Solar:")
        self.label_solar.grid(row=5, column=0,sticky="nsew", pady=10, padx=10)
        self.solar_entry = customtkinter.CTkEntry(self)
        self.solar_entry.grid(row=5, column=1,sticky="nsew", pady=10, padx=10)

        self.label_wind = customtkinter.CTkLabel(self, text="Wind:")
        self.label_wind.grid(row=6, column=0,sticky="nsew", pady=10, padx=10)
        self.wind_entry = customtkinter.CTkEntry(self)
        self.wind_entry.grid(row=6, column=1,sticky="nsew", pady=10, padx=10)

        self.label_hydro = customtkinter.CTkLabel(self, text="Hydro:")
        self.label_hydro.grid(row=7, column=0,sticky="nsew", pady=10, padx=10)
        self.hydro_entry = customtkinter.CTkEntry(self)
        self.hydro_entry.grid(row=7, column=1,sticky="nsew", pady=10, padx=10)

        self.label_nuclear = customtkinter.CTkLabel(self, text="Nuclear:")
        self.label_nuclear.grid(row=8, column=0,sticky="nsew", pady=10, padx=10)
        self.nuclear_entry = customtkinter.CTkEntry(self)
        self.nuclear_entry.grid(row=8, column=1,sticky="nsew", pady=10, padx=10)

        self.label_oil = customtkinter.CTkLabel(self, text="Oil:")
        self.label_oil.grid(row=9, column=0,sticky="nsew", pady=10, padx=10)
        self.oil_entry = customtkinter.CTkEntry(self)
        self.oil_entry.grid(row=9, column=1,sticky="nsew", pady=10, padx=10)

        self.label_gas = customtkinter.CTkLabel(self, text="Gas:")
        self.label_gas.grid(row=10, column=0,sticky="nsew", pady=10, padx=10)
        self.gas_entry = customtkinter.CTkEntry(self)
        self.gas_entry.grid(row=10, column=1,sticky="nsew", pady=10, padx=10)

        self.label_coal = customtkinter.CTkLabel(self, text="Coal:")
        self.label_coal.grid(row=11, column=0,sticky="nsew", pady=10, padx=10)
        self.coal_entry = customtkinter.CTkEntry(self)
        self.coal_entry.grid(row=11, column=1,sticky="nsew", pady=10, padx=10)

        self.add_btn = customtkinter.CTkButton(self,text='Add',command=self.add)
        self.add_btn.grid(row = 12,columnspan=2,sticky="nsew", pady=10, padx=10)

    def add(self):
        loader = Country_Data_Manager("data/data.json")
        country = self.country_entry.get()
        year = self.year_slider.get()
        other = self.other_entry.get()
        bio = self.bio_entry.get()
        solar = self.solar_entry.get()
        wind =  self.wind_entry.get()
        hydro = self.hydro_entry.get()
        nuclear = self.nuclear_entry.get()
        oil = self.oil_entry.get()
        gas = self.gas_entry.get()
        coal = self.coal_entry.get()

        if country == '':
            messagebox.showwarning(message="Please enter a country !",title = 'WARNING')
        elif other == '' or other.isdigit() == False:
            messagebox.showwarning(message="Other's value must be number !",title = 'WARNING')
        elif bio == '' or bio.isdigit() == False:
            messagebox.showwarning(message="Bioenergy's value must be number!",title = 'WARNING')
        elif solar == '' or solar.isdigit() == False:
            messagebox.showwarning(message="Solar's value must be number !",title = 'WARNING')
        elif wind == '' or wind.isdigit() == False:
            messagebox.showwarning(message="Wind's value must be number !",title = 'WARNING')
        elif hydro == '' or hydro.isdigit() == False:
            messagebox.showwarning(message="Hydro's value must be number !",title = 'WARNING')
        elif nuclear == '' or nuclear.isdigit() == False:
            messagebox.showwarning(message="Nuclear's value must be number !",title = 'WARNING')
        elif oil == '' or oil.isdigit() == False:
            messagebox.showwarning(message="Oil's value must be number !",title = 'WARNING')
        elif gas == '' or gas.isdigit() == False:
            messagebox.showwarning(message="Gas's value must be number !",title = 'WARNING')
        elif coal == '' or coal.isdigit() == False:
            messagebox.showwarning(message="Coal's value must be number !",title = 'WARNING')
        else:
            ans = messagebox.askyesno(title="Confirm",message=f"Do you want to add new values in {int(year)} to {country} ?")
            if ans:
                loader.create_and_update_data(country_name=country,year=str(int(year)),new_values=[other,bio,solar,wind,hydro,nuclear,oil,gas,coal])
                self.destroy()
                messagebox.showinfo("Status","Success !")

class MyTabView(customtkinter.CTkTabview):
    def __init__(self,master,years,country,yearpie1,countrypie1,yearpie2,countrypie2,**kwargs):
        super().__init__(master,**kwargs)
        #=============table==============
        self.add("Table")
        self.tab("Table").grid_columnconfigure(0, weight=1)
        self.tab("Table").grid_rowconfigure(0, weight=1)

        self.years = years
        self.country = country
        self.yearpie1 = yearpie1
        self.countrypie1 = countrypie1
        self.yearpie2 = yearpie2
        self.countrypie2 = countrypie2

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
        self.loaderdata = Get_Country_Data('data/data.json')
        self.data = self.loaderdata.Get_Data_From_Year_to_Year(str(self.country),str(int(self.years[0])),str(int(self.years[1])))
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
        #=============Graph==============#
        self.add("Graph")
        self.tab("Graph").grid_columnconfigure(0, weight=1)
        self.tab("Graph").grid_rowconfigure(0, weight=1)
        
        self.yeargraph,self.other,self.Bioenergy,self.Solar,self.Wind, self.Hydro,self.Nuclear,self.Old,self.Gas,self.Coal = self.loaderdata.Get_Data_From_Year_to_Year_Graph(str(self.country),str(int(self.years[0])),str(int(self.years[1])))
        self.fig = Figure(figsize=(17, 10))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.tab("Graph"))
        self.update_graph(self.yeargraph,self.other,self.Bioenergy,self.Solar,self.Wind, self.Hydro,self.Nuclear,self.Old,self.Gas,self.Coal)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0, column=0)

        #=============Compare==============#
        self.add("Compare")
        self.tab("Compare").grid_columnconfigure(0, weight=1)
        self.tab("Compare").grid_columnconfigure(1, weight=1)
        self.tab("Compare").grid_rowconfigure(0, weight=1)

        self.pie1 = self.loaderdata.Get_EnergyData_Type_1Country_1Year(self.countrypie1,str(self.yearpie1))
        self.pie2 = self.loaderdata.Get_EnergyData_Type_1Country_1Year(self.countrypie2,str(self.yearpie2))

        self.figpie = Figure(figsize=(17, 10))
        self.axpie1 = self.figpie.add_subplot(121)
        self.axpie2 = self.figpie.add_subplot(122)
        self.canvaspie = FigureCanvasTkAgg(self.figpie, master=self.tab('Compare'))
        self.update_Compare(self.pie1,self.pie2,[self.countrypie1,self.yearpie1],[self.countrypie2,self.yearpie2])
        self.canvaspie_widget = self.canvaspie.get_tk_widget()
        self.canvaspie_widget.grid(row=0, column=0)


    def update_table(self,sort_item,sort_mode):
        self.data = Get_Country_Data('data/data.json').Get_Data_From_Year_to_Year(str(self.country),str(int(self.years[0])),str(int(self.years[1])))
        column_index = ["Entity", "Year", "Other", "Bioenergy", "Solar", "Wind", "Hydro", "Nuclear", "Oil", "Gas", "Coal"].index(sort_item)
        if sort_item == "Year":
            key_function = lambda row: int(row[column_index])
        else:
            key_function = lambda row: float(row[column_index])
    
        reverse = (sort_mode == "Descending")
        self.data.sort(key=key_function, reverse=reverse)
        
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
    def update_Compare(self, pie1, pie2,data1,data2):  
        """Cập nhật và hiển thị biểu đồ so sánh."""
        self.axpie1.clear()
        self.axpie2.clear()

        if pie1 == '#None_Data':
            self.axpie1.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=16)
        else:
            pie1 = list(map(float,pie1))
            # Cấu hình biểu đồ
            self.axpie1.set_title(f'Sản lượng nguồn điện {data1[0]} của {data1[1]}')
            mylabels1 = ['other', 'bioenergy', 'solar', 'wind', 'hydro', 'nuclear', 'oil', 'gas', 'coal']
            # Lọc dữ liệu và nhãn
            values1 = [value for value in pie1 if value > 0]
            labels1 = [label for value, label in zip(pie1, mylabels1) if value > 0]
            # Vẽ biểu đồ năng lượng
            wedges1, texts1, autotexts1 = self.axpie1.pie(x=values1, labels=labels1, autopct='%1.1f%%')
            # Hiển thị chú giải
            self.axpie1.legend(wedges1, labels1, title="Nguồn", loc="lower left", bbox_to_anchor=(-0.1, -0.1))

        if pie2 == '#None_Data':
            self.axpie2.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=16)
        else:
            pie2 = list(map(float,pie2))
            # Cấu hình biểu đồ
            self.axpie2.set_title(f'Sản lượng nguồn điện {data2[0]} của {data2[1]}')
            mylabels2 = ['other', 'bioenergy', 'solar', 'wind', 'hydro', 'nuclear', 'oil', 'gas', 'coal']
            # Lọc dữ liệu và nhãn
            values2 = [value for value in pie2 if value > 0]
            labels2 = [label for value, label in zip(pie2, mylabels2) if value > 0]
            # Vẽ biểu đồ năng lượng
            wedges2, texts2, autotexts2 = self.axpie2.pie(x=values2, labels=labels2, autopct='%1.1f%%')
            # Hiển thị chú giải
            self.axpie2.legend(wedges2, labels2, title="Nguồn", loc="lower left", bbox_to_anchor=(-0.1, -0.1))

        self.canvaspie.draw()



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title("Dashboard")
        
        #chia window làm 2 frame
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.loaderdata = Get_Country_Data('data/data.json')

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

        #menu country
        self.country_menu = customtkinter.CTkComboBox(
            master=self.left_frame,
            width=200,
            values=self.loaderdata.Get_Country_Name(),
        )
        self.country_menu.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        findbox(self.country_menu,self.loaderdata.Get_Country_Name())

        #slider
        self.varyearstart = customtkinter.IntVar(value=1985)
        self.varyearend = customtkinter.IntVar(value=2024)
        self.slider_frame = customtkinter.CTkFrame(
            master= self.left_frame,
        )
        self.slider_frame.grid(row=2, column=0, sticky="nswe",padx = 10,pady = 10)
        self.slider = CTkRangeSlider(master= self.slider_frame, from_=1985, to=2024,number_of_steps=39,variables = [self.varyearstart, self.varyearend],width=150)
        self.slider.grid(row=0, column=1, sticky="nswe",padx = 10,pady = 10)
        self.label_sliderstart = customtkinter.CTkLabel(master=self.slider_frame, textvariable = self.varyearstart,height = 20)
        self.label_sliderstart.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.label_sliderend = customtkinter.CTkLabel(master=self.slider_frame, textvariable = self.varyearend,height = 20)
        self.label_sliderend.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        #sort area
        self.sort_frame = customtkinter.CTkFrame(
            master= self.left_frame,
        )
        self.sort_frame.grid(row=3, column=0, sticky="nswe",padx = 10,pady = 10)
        self.sort_frame.grid_columnconfigure(1, weight=1)
        self.sort_frame.grid_columnconfigure(0, weight=1)
        self.label_sortitem = customtkinter.CTkLabel(master = self.sort_frame,text = "Sort Item")
        self.label_sortitem.grid(row = 0,column = 0,sticky="nsew", padx=10, pady=10)
        self.items_menu = customtkinter.CTkOptionMenu(
            master=self.sort_frame,
            values=["Year","Other", "Bioenergy", "Solar", "Wind", "Hydro", "Nuclear", "Oil", "Gas", "Coal"]
        )
        self.items_menu.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.label_sortmode = customtkinter.CTkLabel(master = self.sort_frame,text = "Sort mode")
        self.label_sortmode.grid(row = 1,column = 0,sticky="nsew", padx=10, pady=10)
        self.mod_menu = customtkinter.CTkOptionMenu(
            master=self.sort_frame,
            values=["Ascending","Descending"]
        )
        self.mod_menu.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        #compare_data_area
        self.compare_frame = customtkinter.CTkFrame(master= self.left_frame )
        self.compare_frame.grid_columnconfigure(1, weight=1)
        self.compare_frame.grid_columnconfigure(0, weight=1)
        self.compare_frame.grid(row=5, column=0, sticky="nswe",padx = 10,pady = 10)
        self.label_compare = customtkinter.CTkLabel(
            master=self.compare_frame,
            text="Compare"
        )
        self.label_compare.grid(row=0, columnspan=2, sticky="nsew", pady=(10, 5), padx=5 )
        self.country1_menu = customtkinter.CTkComboBox(master=self.compare_frame , 
            values= self.loaderdata.Get_Country_Name()
        )
        self.country1_menu.grid(row=1, column=0, pady=(5, 10), padx=5,sticky="w")
        findbox(self.country1_menu,self.loaderdata.Get_Country_Name())
        self.country2_menu = customtkinter.CTkComboBox(master=self.compare_frame , 
            values=self.loaderdata.Get_Country_Name()
        )
        self.country2_menu.grid(row=1, column=1, pady=(5, 10), padx=5)
        findbox(self.country2_menu,self.loaderdata.Get_Country_Name())
        self.year_country1_menu = customtkinter.CTkOptionMenu(master=self.compare_frame ,
             values=[str(i) for i in range(1985, 2024)]
        )
        self.year_country1_menu.grid(row=2, column=0, pady=(5, 10), padx=5,sticky="w")
        self.year_country2_menu = customtkinter.CTkOptionMenu(master=self.compare_frame ,  
            values=[str(i) for i in range(1985, 2024)]
        )
        self.year_country2_menu.grid(row=2, column=1, pady=(5, 10), padx=5)
        #update button
        self.btn_update = customtkinter.CTkButton(
            master= self.left_frame,
            text = 'Update',
            command = self.update_handle,
            fg_color= 'green'
        )
        self.btn_update.grid(row=6, column=0, pady=(5, 10), padx=5)
        #adjust data button
        self.btn_settings = customtkinter.CTkButton(
            master=self.left_frame,
            text="Adjust Data",
            command=self.open_adjustwindow
        )
        self.adjust_window = None
        self.btn_settings.grid(row=7, column=0, pady=(5, 10), padx=5)
        #add data button
        self.btn_add_data = customtkinter.CTkButton(
            master=self.left_frame,
            text="Add Data",
            command=self.open_addwindow
        )
        self.add_window = None
        self.btn_add_data.grid(row=8, column=0, pady=(5, 10), padx=5)

        #------------Right-Side (frame_right)---------------#
        self.right_frame.grid_columnconfigure(0, weight=1)
        self.right_frame.grid_rowconfigure(0, weight=1)
        
        self.tab_view = MyTabView(master=self.right_frame,height = 1080,width = 1920,country= self.country_menu.get(),years=self.slider.get(),countrypie1 = self.country1_menu.get(),yearpie1= self.year_country1_menu.get(),countrypie2 = self.country2_menu.get(),yearpie2=self.year_country2_menu.get())
        self.tab_view.grid(row=0, column=0)

    def update_handle(self):
        """Xử lý cập nhật bảng và biểu đồ khi bấm nút Update."""
        # Lấy giá trị mới từ các widget
        loader = Get_Country_Data('data/data.json')

        self.country_menu.configure(values=loader.Get_Country_Name())
        selected_country = self.country_menu.get()
        selected_years = self.slider.get()
        sort_item = self.items_menu.get()
        sort_mode = self.mod_menu.get()
        comparecountry1 = self.country1_menu.get()
        comparecountry2 = self.country2_menu.get()
        compareyear1 = self.year_country1_menu.get()
        compareyear2 = self.year_country2_menu.get()
        comparedata1 = loader.Get_EnergyData_Type_1Country_1Year(comparecountry1,str(compareyear1))
        comparedata2 = loader.Get_EnergyData_Type_1Country_1Year(comparecountry2,str(compareyear2))

        self.tab_view.update_Compare(comparedata1,comparedata2,[comparecountry1,compareyear1],[comparecountry2,compareyear2])

        # Cập nhật dữ liệu trong MyTabView
        self.tab_view.country = selected_country
        self.tab_view.years = selected_years
        self.tab_view.update_table(sort_item, sort_mode)

        # Cập nhật biểu đồ
        yeargraph,other,Bioenergy,Solar,Wind, Hydro,Nuclear,Old,Gas,Coal = loader.Get_Data_From_Year_to_Year_Graph(str(selected_country),str(int(selected_years[0])),str(int(selected_years[1])))

        self.tab_view.update_graph(yeargraph,other,Bioenergy,Solar,Wind, Hydro,Nuclear,Old,Gas,Coal)

        #update menu findbox
        findbox(self.country_menu,loader.Get_Country_Name())
        findbox(self.country1_menu,loader.Get_Country_Name())
        findbox(self.country2_menu,loader.Get_Country_Name())

    def open_adjustwindow(self):
        """Khởi tạo cửa sổ phụ"""
        if self.adjust_window is None or not self.adjust_window.winfo_exists():
            self.country = self.country_menu.get()
            self.adjust_window = AdjustDataWindow(self.country)
            self.adjust_window.grab_set()
        else:
            self.adjust_window.focus()

    def open_addwindow(self):
        """Khởi tạo cửa sổ phụ"""
        if self.add_window is None or not self.add_window.winfo_exists():
            self.add_window = AddDataWindow()
            self.add_window.grab_set()
        else:
            self.add_window.focus()

app = App()
app.mainloop()
