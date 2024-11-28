

import json

class Country_Data_Manager:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()
    
    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)

    def print_country_data(self, country_name):
        if self.data.get(country_name):
            return self.data[country_name]