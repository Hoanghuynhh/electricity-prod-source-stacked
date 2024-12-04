import json

# 1. Đưa về những giá trị để in ra
class Get_Country_Data:

    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()

    # dùng để khởi chạy file dữ liệu
    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)
    

    # 1.1: Đưa ra tên các quốc gia:
    def Get_Country_Name(self):
        return self.data.keys()
    
    # 1.2: Đưa ra các năm của 1 quốc gia:
    def Get_Year_of_one_Country(self, country_name):
        if self.data.get(country_name):
            return list(self.data[country_name].keys())
        else:
            return "#None_Data"
    
    # 1.3: Đưa ra các loại dữ liệu của một quốc gia trong một năm:
    def Get_EnergyTypes_1Country_1Year(self, country_name, year):
        if country_name in self.data and year in self.data[country_name]:
            return list(self.data[country_name][year].keys())
        else:
            return "#None_Data"
    
    # 1.4: Đưa ra dữ liệu của tất cả các nước trong một năm:
    def Get_Data_aCountry_1Year(self, year):
        all_data = {}
        for country, data in self.data.items():
            if year in data:
                all_data[country] = data[year]
            else:
                all_data[country] = "#None_Data"

        return all_data
    
    # 1.5: Đưa về tất cả dữ liệu của file dữ liệu
    def Get_all_data(self):
        return dict(self.data)
    

# 2. Update dữ liệu (thay đổi, ghi đè)
class Update_Country_Data:

    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()

    # dùng để khởi chạy file dữ liệu
    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)
    
    # dùng để save file dữ liệu lại sau khi ghi đè
    def save_data(self):
        with open(self.json_file, "w") as file:
            json.dump(self.data, file, indent = 4)

    # 2.1: thay đổi 1 loại dữ liệu của một quốc gia trong một năm:
    def Update_1DataType_1Country_1Year(self, country_name, year, data_type, new_value):
        if country_name in self.data and year in self.data[country_name]:
            if data_type in self.data[country_name][year]:
                self.data[country_name][year][data_type] = new_value
                self.save_data()
            else:
                return "#None_Data_To_Change"
        else:
            return "#None_Data_To_Change"
    
    # 2.2: thay đổi tất cả dữ liệu trong 1 năm của một quốc gia:
    def Update_aDataType_1Country_1Year(self, country_name, year, data_other, data_bio, data_sol, data_wind, data_hydro, data_nuc, data_oil, data_gas, data_coal):
        if country_name in self.data and year in self.data[country_name]:
            self.data[country_name][year] = {
                "Other": data_other,
                "Bioenergy": data_bio,
                "Solar": data_sol,
                "Wind": data_wind,
                "Hydro": data_hydro,
                "Nuclear": data_nuc,
                "Oil": data_oil,
                "Gas": data_gas,
                "Coal": data_coal   
            }
            self.save_data()
        else:
            return "#None_Data_To_Change"
    

# 3. xóa đi dữ liệu
class Delete_Country_Data:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()

    # dùng để khởi chạy file dữ liệu
    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)
    
    # dùng để save file dữ liệu lại sau khi ghi đè
    def save_data(self):
        with open(self.json_file, "w") as file:
            json.dump(self.data, file, indent = 4)

    
    # 3.1: xóa 1 dữ liệu của 1 nước của 1 năm:
    def Del_1Data_1Country_1Year(self, country_name, year, data_type):
        if country_name in self.data and year in self.data[country_name]:
            if data_type in self.data[country_name][year]:
                self.data[country_name][year][data_type] = "0"
                self.save_data()
            else:
                return "#None_Data_to_Delete"
        else:
            return "#None_Data_to_Delete"
        
    # 3.2: xóa đi tất cả dữ liệu của 1 nước trong 1 năm
    def Del_aData_1Country_1Year(self, country_name, year):
        if country_name in self.data and year in self.data[country_name]:
            self.data[country_name][year] = "0"
            self.save_data()
        else:
            return "#None_Data_to_Delete"
    
    # 3.3 xóa đi dữ liệu của một nước:
    def Del_Country_Data(self, country_name):
        if self.data.get(country_name):
            self.data[country_name] = 0
            self.save_data()
        else:
            return "#None_Data_to_Delete"
        