from demo_1 import * 


choose = input("hãy nhập tên quốc gia: ")

country_data = Country_Data_Manager("data.json")
print(country_data.print_country_data(choose))
