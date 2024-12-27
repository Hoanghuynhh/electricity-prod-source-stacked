import json
from typing import List, Dict


class Country_Data_Manager:

    def __init__(self, json_file) -> None:
        """
        Khởi tạo đối tượng loader dùng để truy cập vào dữ liệu trong lớp Country_Data_Manager.

        input: Đường dẫn đến file Json(str)
        output: None

        Example:
            loader = Country_Data_Manager("data/data.json")
            print(loader.data)  # In ra toàn bộ dữ liệu từ file Json.
        """
        self.json_file = json_file # Gán đường dẫn của file Json cho biến cục bộ self.json_file
        self.data = self.load_data() # Lưu dữ liệu từ file Json vào biến cục bộ self.data bằng hàm self.load_data()

    def load_data(self) -> Dict:
        """
        Đọc file Json và trả về toàn bộ dữ liệu từ file (ở đây là một Dictionary lớn gồm nhiều Dictionary nhỏ).

        input: None
        output: Dictionary

        Example:
            self.data = self.load_data() # Biến self.data sẽ chứa toàn bộ dữ liệu từ file Json (Dictionary)
        """
        with open(self.json_file, "r") as f:
            return json.load(f)
        
    def is_country(self, country_name: str) -> bool:
        """
        Kiểm tra 1 quốc gia có trong self.data hay không.

        input: country_name(str)
        output: True or False

        Example:
            boolean = self.is_country('Brazil')
            print(boolean) # In ra 'True' vì Brazil có trong self.data
        """
        return country_name in self.data
    
    def is_country_year(self, country_name: str, year: str) -> bool:
        """
        Kiểm tra 1 năm có trong 1 quốc gia của self.data hay không.

        input: country_name(str), year(str)
        output: True, False

        Example:
            boolean = self.is_country_year('Brazil', '1800')
            print(boolean) # In ra 'False' vì '1800' không có trong dữ liệu của self.data/'Brazil'
        """
        return year in self.data[country_name]
    
    def is_country_year_energy(self, country_name: str, year: str, energy_type: str) -> bool:
        """
        Kiểm tra 1 loại năng lượng có trong self.data/country/year hay không.

        input: country_name(str), year(str), energy_type(str)
        output: True, False

        Example: 
            boolean = self.is_country_year_energy('Brazil', '2011', 'Wind')
            print(boolean) # In ra 'True' vì 'Wind' có trong dữ liệu của self.data/'Brazil'/'2011'
        """
        return energy_type in self.data[country_name][year]

    
    clearly_data = {
            "Other": "0",
            "Bioenergy": "0",
            "Solar": "0",
            "Wind": "0",
            "Hydro": "0",
            "Nuclear": "0",
            "Oil": "0",
            "Gas": "0",
            "Coal": "0"
        } # Khởi tạo một Dictionary rỗng thuận tiện cho việc sửa xóa.
    
    def save_data(self) -> None:
        """
        Ghi đè dữ liệu từ self.data (dữ liệu cục bộ của lớp Country_Data_Manager) vào file Json gốc (data/data.json).

        input: None
        output: None

        Example:
            self.save_data() # Dữ liệu từ self.data sẽ được ghi đè vào file data/data.json
        """
        with open(self.json_file, "w") as file:
            json.dump(self.data, file, indent = 4)

    def listenergy_to_dict(self, new_value: list) -> dict:
        """
        Xử lí dữ liệu đầu vào từ List -> Dict

        input: List (9 values)
        output: Dict (9 items)

        Example:
            lst = ['1','2','3','4','5','6','7','8','9']   
            dct = self.listenergy_to_dict(lst)
            print(dct) # {'Other': '1', 'Bioenergy': '2', 'Solar': '3', 'Wind': '4', 'Hydro': '5', 'Nuclear': '6', 'Oil': '7', 'Gas': '8', 'Coal': '9'}
        """
        value_to_dict = self.clearly_data

        i = 0
        for key in value_to_dict.keys(): 
            value_to_dict[key] = new_value[i]
            i+=1
        return value_to_dict

    def update_data(self, country_name: str, year: str, energy_type: str, new_value: str) -> None:
        """
        Cập nhật giá trị mới cho 1 energy_type trong data/data.json/country/year
        
        input: country_name(str), year(str), energy_type(str), new_value(str)
        output: None

        Example:
            loader.update_data('Brazil', '2011', 'Wind', '10') # data/data.json/'Brazil'/'2011'/'Wind': '10'
        """
        if self.is_country_year(country_name, year):
            self.data[country_name][year][energy_type] = new_value
            self.save_data()

    def create_and_update_data(self, country_name: str, year: str, new_values: list) -> None:
        """
        Thêm dữ liệu của 1 năm vào data/data.json/country

        input: country_name(str), year(str), new_values(list)
        output: None

        Example:
            lst = ['1','2','3','4','5','6','7','8','9']
            loader.create_and_update_data('Brazil', '2011', lst) # data/data.json/'Brazil'/'2011': {
                                                                                               "Other": "1",
                                                                                               "Bioenergy": "2",
                                                                                               "Solar": "3",
                                                                                               "Wind": "4",
                                                                                               "Hydro": "5",
                                                                                               "Nuclear": "6",
                                                                                               "Oil": "7",
                                                                                               "Gas": "8",
                                                                                               "Coal": "9"
                                                                                            }
        """
        if self.is_country(country_name):
            if not self.is_country_year(country_name, year):  # Nếu năm đó chưa có thì thêm dữ liệu
                self.data[country_name][year] = self.listenergy_to_dict(new_values)
            else:  # Nếu năm đó đã tồn tại, ghi đè dữ liệu
                self.data[country_name][year].update(self.listenergy_to_dict(new_values))
        else:  # Nếu quốc gia chưa tồn tại thì thêm dữ liệu
            self.data[country_name] = {
                year: self.listenergy_to_dict(new_values)
            }
        self.save_data()

    def delete_data_energy(self, country_name: str, year: str, energy_type: str) -> None:
        """
        Xoá dữ liệu (đưa về '0') của 1 energy_type trong data/data.json/country/year 

        input: country_name(str), year(str), energy_type(str)
        output: None

        Example:
            loader.delete_data_energy('Brazil', '2011', 'Wind') # data/data.json/'Brazil'/'2011'/'Wind': "0"
        """
        if self.is_country_year_energy(country_name, year, energy_type):
            self.data[country_name][year][energy_type] = '0'
            self.save_data()
    
    def delete_data_country(self, country_name: str) -> None:
        """
        Xóa 1 quốc gia khỏi data/data.json

        input: country_name
        output: None

        Example:
            loader.delete_data_country('Brazil') # Item 'Brazil' bị xóa khỏi data/data.json
        """
        if self.is_country(country_name):
            del self.data[country_name]
            self.save_data()

    def delete_data_year(self, country_name: str, year: str) -> None:
        """
        Xoá 1 năm khỏi data/data.json/country

        input: country_name(str), year(str)
        output: None

        Example:
            loader.delete_data_year('Brazil', '2011') # Item '2011' bị xóa khỏi data/data.json/'Brazil'
        """
        if self.is_country_year(country_name, year):
            del self.data[country_name][year]
            self.save_data()

    def delete_all_data_energy_type(self, country_name: str, energy_type: str) -> None:
        """
        Xóa dữ liệu của energy_type (đưa về '0' một loại năng lượng trong tất cả năm của 1 quốc gia) của data/data.json/country

        input: country_name(str), energy_Type(str)
        output: None

        Example:
            loader.delete_all_data_energy_type('Brazil', 'Wind') # Dữ liệu của 'Wind' trong toàn bộ năm của data/data.json/'Brazil' sẽ bị đưa về '0'
        """
        for Year in self.data[country_name].keys():
            self.delete_data_energy(country_name, Year, energy_type)
        self.save_data()
