import json
from tabulate import *

class Country_Data_manager:

    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()

    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)
        
    def Print_Table_1y_1c(self, country_name, year):
        if country_name in self.data and year in self.data[country_name]:
            year_data = self.data[country_name][year]
            table_data = [[keys, value] for keys, value in year_data.items()]

            return tabulate(table_data, headers=["loai", "sang luong"], tablefmt="grid")
    
    