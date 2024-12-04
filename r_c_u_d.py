import json
from typing import List, Dict


class Country_Data_Manager:

    def __init__(self, json_file) -> None:
        """
        Khởi tạo đối tượng loader để nạp dữ liệu từ tệp JSON.

        Phương thức này nhận đường dẫn tới một tệp JSON và sử dụng nó
        để nạp dữ liệu vào thuộc tính `data` của đối tượng.

        Args:
            json_file (str): Đường dẫn tới tệp JSON chứa dữ liệu.

        Attributes:
            json_file (str): Đường dẫn tới tệp JSON được cung cấp khi khởi tạo.
            data (dict hoặc list): Dữ liệu đã được nạp từ tệp JSON, thường là
                                    một từ điển (dictionary) hoặc danh sách (list).

        Example:
            loader = Country_Data_Manager("data.json")
            print(loader.data)  # In ra nội dung dữ liệu đã nạp từ tệp JSON.
        """
        self.json_file = json_file
        self.data = self.load_data()
    
    def is_country(self, country_name: str) -> bool:
        return country_name in self.data
    
    def is_country_year(self, country_name: str, year: str) -> bool:
        return year in self.data[country_name]
    
    def is_country_year_energy(self, country_name: str, year: str, energy_type: str) -> bool:
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
        }
    def load_data(self) -> Dict:
        with open(self.json_file, "r") as f:
            return json.load(f)

    def save_data(self) -> None:
        with open(self.json_file, "w") as file:
            json.dump(self.data, file, indent = 4)
    
    def update_data(self, country_name: str, year: str, energy_type: str, new_value) -> None:
        """
        Cập nhật giá trị của một loại năng lượng/quốc gia/năm
        """
        if self.is_country_year(country_name, year):
            self.data[country_name][year][energy_type] = new_value
            self.save_data()
    
    def create_data(self, country_name: str, year: str, new_value: dict) -> None:
        """
        Thêm giá trị các loại năng lượng/quốc gia/năm
        """
        if year >= 0:
            if self.is_country_year(country_name, year):
                self.data[country_name][year] = new_value
                self.save_data()
    
    def delete_data_energy(self, country_name: str, year: str, energy_type: str) -> None:
        if self.is_country_year_energy(country_name, year, energy_type):
            self.data[country_name][year][energy_type] = '0'
            self.save_data()
    
    def delete_data_country(self, country_name: str) -> None:
        if self.is_country(country_name):
            del self.data[country_name]
            self.save_data()

    def delete_data_year(self, country_name: str, year: str) -> None:
        if self.is_country_year(country_name, year):
            self.data[country_name][year] = self.clearly_data
            self.save_data()


if __name__ == '__main__':
    loader = Country_Data_Manager('simplified_data.json')
    loader.delete_data_country('ASEAN (Ember)')
    