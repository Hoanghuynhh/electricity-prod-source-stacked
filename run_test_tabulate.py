from test_tabulate_1 import *

choose_country = input("nhập quốc gia: ")
choose_year = input("nhập năm: ")


country_data = Country_Data_manager("data.json")
print(country_data.Print_Table_1y_1c(choose_country, choose_year))