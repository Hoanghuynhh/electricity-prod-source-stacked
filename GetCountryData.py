import json

class Get_Country_Data:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.load_data()
    
    def load_data(self):
        with open(self.json_file, "r") as file:
            return json.load(file)
    
    
    # 1.1: Đưa ra tên các quốc gia:
    def Get_Country_Name(self):
        """
        Hàm dùng để lấy dữ liệu tên của tất cả các quốc gia:
        input: 
            <#None>: Không yêu cầu nhập đầu vào dữ liệu
        
        output:
            <tên_các_nước> (list): trả về một list chứa tên các nước có trong dữ DataBase
        """
        return sorted(list(self.data.keys()))
    
    # 1.2: Đưa ra các năm của 1 quốc gia:
    def Get_Year_of_one_Country(self, country_name):

        """
        Hàm dùng để lấy dữ liệu tất cả các năm của một quốc gia:
        input:
            <tên_quốc_gia> (string): dữ liệu đầu vào cần có một tên quốc gia
            Get_Year_of_one_Country(<country_name>)
        output:
            <các_năm_có_tồn_tại> (list): trả về một list chứa các năm đã tồn tại có trong một nước có tồn tại
            nằm trong DataBase
        """

        if self.data.get(country_name):
            return list(self.data[country_name].keys())
        else:
            return "#None_Data"
    
    # 1.3: Đưa ra tên các loại dữ liệu của một quốc gia trong một năm:
    def Get_EnergyTypes_1Country_1Year(self, country_name, year):

        """
        Hàm dùng để lấy tất cả tên các loại dữ liệu của 1 năm của một quốc gia:
        input:
            <tên_nước>, <năm> (string) (string): dữ liệu đầu vào cần có tên một quốc gia và một năm cố định có tồn tại hoặc không
            Get_EnergyTypes_1Country_1Year(country_name, year)
        output:
            if <input> == True:
                <tên_các_loại_dữ_liệu> (list): trả về một list tên các loại năng lượng có tồn tại trong DataBase của một nước trong năm đó
            else:
                <"#None_Data"> (string): trả về string None_Data vì nước hoặc năm không đúng hoặc nước và năm không tồn tại
        """

        if country_name in self.data and year in self.data[country_name]:
            return list(self.data[country_name][year].keys())
        else:
            return "#None_Data"
    
    # 1.4: Đưa ra dữ liệu của tất cả các nước trong một năm:
    
    
    # 1.5: lấy dữ liệu về các loại năng lượng trong một năm của một quốc gia
    def Get_EnergyData_Type_1Country_1Year(self, country_name, year):

        """
        Hàm dùng để lấy dữ liệu về các loại năng lượng của một quốc gia trong một năm
        input:
            <tên_nước>, <năm> (string) (string): dữ liệu đầu vào cần có tên một quốc gia và một năm cố định có tồn tại hoặc không
            Get_Energy_Data_1Country_1Year(country_name, year)
        output:
            if <tên_nước>, <năm> == True:   
                <tất_cả_dữ_liệu_năng_lượng> (dict): trả về một dictionary chứa các keys là tên loại năng lượng và value là giá trị loại năng lượng
            else:
                <"#None_Data"> (string): trả về string None_Data vì nước hoặc năm không đúng hoặc nước và năm không tồn tại
        """

        if country_name in self.data and year in self.data[country_name]:
            energy_data = []
            for i in list(self.data[country_name][year]):
                energy_data.append(self.data[country_name][year].get(i))
            return energy_data
        else:
            return "#None_Data"
    
    # 1.6: lấy một loại dữ liệu nào đó của một quốc gia trong một năm:
    def Get_1EnergyData_1Country_1Year(self, country_name, year, energy_name):

        """
        Hàm trả về một loại năng lượng của một quốc gia trong một năm:
        input:
            <tên_nước> <năm> <tên_loại_năng_lượng> (string) (string) (string): dữ liệu đầu vào cần có tên nước, năm, loại năng lượng đã
            tồn tại hoặc không tồn tại trong DataBase
            Get_1EnergyData_1Country_1Year(country_name, year, energy_name):
        output:
            if <tên_nước> <năm> <tên_loại_năng_lượng> == True:
                <tên_năng_lượng> : <giá_trị> (dict): trả về một string chứa loại năng lượng và giá trị của nó
            else:
                <"#None_Data"> (string): trả về string None_Data vì nước hoặc năm hoặc loại năng lượng không đúng hoặc
                nước hoặc năm hoặc loại năng lượng không tồn tại
        """

        if country_name in self.data and year in self.data[country_name] and energy_name in self.data[country_name][year]:
            energy_data = list(self.data[country_name][year][energy_name])
            return energy_data
        
    
    # 1.7: lấy tất cả dữ liệu của một năm của một nước:
    def Get_aData_1Country_1Year(self, country_name, year):
        """
        Hàm dùng để lấy tất cả các dữ liệu của một năm của một quốc gia
        input:
            <tên_nước> <năm> (string) (string): dữ liệu đầu vào cần có tên một quốc gia và một năm cố định có tồn tại hoặc không
        output:
            if <tên_nước> <năm> == True
                <dữ_liệu> (list): trả về một list chứa dữ liệu về các loại năng lượng với keys là tên loại năng lượng
                và value là các giá trị của chúng
            else:
                <"#None_Data"> (string): trả về string None_Data vì nước hoặc năm không đúng hoặc nước và năm không tồn tại
        """
        # if country_name in list(self.data.keys()) and year in list(self.data[country_name].keys()):
        if country_name in self.data and year in self.data[country_name]:
            Type_Val = self.data[country_name][year]  
            if isinstance(Type_Val, dict):  
                energy_data_list = [
                    country_name,  
                    year,
                    float(Type_Val.get("Other", 0)),
                    float(Type_Val.get("Bioenergy", 0)),
                    float(Type_Val.get("Solar", 0)),
                    float(Type_Val.get("Wind", 0)),
                    float(Type_Val.get("Hydro", 0)),
                    float(Type_Val.get("Nuclear", 0)),
                    float(Type_Val.get("Oil", 0)),
                    float(Type_Val.get("Gas", 0)),
                    float(Type_Val.get("Coal", 0))
                ]
                return energy_data_list 
        return []  


    # 1.8: đưa về các giá trị trong một khoảng năm cố định
    def Get_Data_From_Year_to_Year(self, country_name, year_start, year_end):
        # Kiểm tra xem year_start và year_end có phải là số nguyên không
        if not (year_start.isdigit() and year_end.isdigit()):
            return "#None_Data"

        year_start = int(year_start)
        year_end = int(year_end)
        
        if year_start >= year_end:
            return "#None_Data"

        list_year_available = [year for year in range(year_start, year_end + 1)]
        
        if country_name in self.data:
            energy_data_final = []
            for year in list_year_available:
                energy_data_available = self.Get_aData_1Country_1Year(country_name, str(year))
                if energy_data_available != []:
                    energy_data_final.append(energy_data_available)

            return energy_data_final
        return "#None_Data"
    
    def Get_Data_From_Year_to_Year_Graph(self, country_name, year_start, year_end):
        # Kiểm tra xem year_start và year_end có phải là số nguyên không
        if not (year_start.isdigit() and year_end.isdigit()):
            return "#None_Data"

        year_start = int(year_start)
        year_end = int(year_end)
        years = []
        Other = []
        Bioenergy = []
        Solar = []
        Wind = []
        Hydro = []
        Nuclear = []
        Oil= []
        Gas = []
        Coal = []
        if year_start >= year_end:
            return "#None_Data"

        list_year_available = [year for year in range(year_start, year_end + 1)]
        
        if country_name in self.data:
            energy_data_final = []
            for year in list_year_available:
                energy_data_available = self.Get_aData_1Country_1Year(country_name, str(year))
                if energy_data_available != []:
                    years.append(int(energy_data_available[1]))
                    Other.append(energy_data_available[2])
                    Bioenergy.append(energy_data_available[3])
                    Solar.append(energy_data_available[4])
                    Wind.append(energy_data_available[5])
                    Hydro.append(energy_data_available[6])
                    Nuclear.append(energy_data_available[7])
                    Oil.append(energy_data_available[8])
                    Gas.append(energy_data_available[9])
                    Coal.append(energy_data_available[10])
            return years,Other,Bioenergy,Solar,Wind,Hydro,Nuclear,Oil,Gas,Coal
        return "#None_Data"


    def Get_All_Data(self):
        all_data = []
        for country in self.data:
            for year in self.data[country]:
                record = [country, year] + list(self.data[country][year].values())
                all_data.append(record)

        return all_data
    def Get_Multiple_Country_Data_From_Year_to_Year(self, countries, year_start, year_end):
        """
        Lấy dữ liệu của các quốc gia trong một khoảng năm.

        Args:
          countries: Danh sách các quốc gia cần lấy dữ liệu.
          year_start: Năm bắt đầu.
          year_end: Năm kết thúc.

        Returns:
          Danh sách các dòng dữ liệu.
        """
        if isinstance(countries,list) == False:
            countries = [countries]
        data_list = []
        for country in countries:
            for year in range(year_start, year_end + 1):
                year = str(year)
                if country in self.data and year in self.data[country]:
                    energy_data = self.Get_aData_1Country_1Year(country, year)
                    if energy_data:
                        data_list.append(energy_data)
        return data_list
