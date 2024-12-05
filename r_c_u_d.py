import json
from typing import List, Dict


class Country_Data_Manager:

    def __init__(self, json_file) -> None:
        """
        Khởi tạo đối tượng loader để nạp dữ liệu từ tệp Json

        input: Json_File (str)
        output: Dữ liệu được nạp từ tệp Json, ở đây là 1 Dict

        Example:
            loader = Country_Data_Manager("data.json")
            print(loader.data)  # In ra Dict đã nạp từ tệp JSON.
        """
        self.json_file = json_file
        self.data = self.load_data()

    def load_data(self) -> Dict:
        """
        Đọc file Json và trả về dữ liệu từ file

        input: None
        output: Dictionary
        """
        with open(self.json_file, "r") as f:
            return json.load(f)
        
    def is_country(self, country_name: str) -> bool:
        """
        Kiểm tra quốc gia có trong self.Data

        input: Country_Name(str)
        output: True, False
        """
        return country_name in self.data
    
    def is_country_year(self, country_name: str, year: str) -> bool:
        """
        Kiểm tra Year có trong Country/self.Data

        input: Country_Name(str), Year(str)
        output: True, False
        """
        return year in self.data[country_name]
    
    def is_country_year_energy(self, country_name: str, year: str, energy_type: str) -> bool:
        """
        Kiểm tra Energy_Type có trong Year/Country/self.Data

        input: Country_Name(str), Year(str), Energy_Type(str)
        output: True, False
        """
        return energy_type in self.data[country_name][year]
    
    '''Khởi tạo giá trị rỗng thuận tiện việc xóa dữ liệu'''
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
        }
    

    def save_data(self) -> None:
        """
        Lưu mới dữ liệu từ self.Data vào file Json gốc

        input: None
        output: None
        """
        with open(self.json_file, "w") as file:
            json.dump(self.data, file, indent = 4)
    
    def update_data(self, country_name: str, year: str, energy_type: str, new_value: str) -> None:
        """
        Cập nhật giá trị mới cho một Energy_Type trong Year/Country/Json_File

        input: Country_Name(str), Year(Str), Energy_Type(str), New_Value(str)
        output: None
        """
        if self.is_country_year(country_name, year):
            self.data[country_name][year][energy_type] = new_value
            self.save_data()
    
    def create_data(self, country_name: str, year: str, new_value: dict) -> None:
        """
        Thêm dữ liệu của một năm mới vào Country/Json_File

        input: Country_Name(str), Year(str), New_Value(dict)
        output: None
        """
        if int(year) >= 0:
            self.data[country_name][year] = new_value
            self.save_data()
    
    def delete_data_energy(self, country_name: str, year: str, energy_type: str) -> None:
        """
        Đưa dữ liệu của Energy_Type trong Year/Countr/Json_File về '0'

        input: Country_Name(str), Year(str), Energy_Type(str)
        output: None
        """
        if self.is_country_year_energy(country_name, year, energy_type):
            self.data[country_name][year][energy_type] = '0'
            self.save_data()
    
    def delete_data_country(self, country_name: str) -> None:
        """
        Xóa một quốc gia khỏi File Json

        input: Country_Name
        output: None
        """
        if self.is_country(country_name):
            del self.data[country_name]
            self.save_data()

    def delete_data_year(self, country_name: str, year: str) -> None:
        """
        Đưa dữ liệu của một Year trong Country/Json_File về '0'

        input: Country_Name(str), Year(str)
        output: None
        """
        if self.is_country_year(country_name, year):
            self.data[country_name][year] = self.clearly_data
            self.save_data()


if __name__ == '__main__':
    loader = Country_Data_Manager('simplified_data.json')
    print(loader)
    