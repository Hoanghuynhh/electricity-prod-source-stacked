import customtkinter as ctk
import unicodedata

class findbox():
    def __init__(self, master, values,command,command2=None,command3=None) -> None:
        self.options = values
        self.command = command
        self.command2 = command2
        self.command3 = command3
        self.combobox = ctk.CTkComboBox(
            master=master,
            width=40,
            values=values,
            command=self.value_combobox
        )
        self.suggest_list =values
        self.combobox.bind("<KeyRelease>", self.suggest)

    @staticmethod
    def normalize_text(text):
        # Loại bỏ dấu và chuyển văn bản thành chữ thường
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8').lower()

    def value_combobox(self, event):
        value_choose = self.combobox.get()
        self.combobox.set(value_choose)
        self.combobox.configure(values=self.options)  # Đặt lại danh sách gốc
        self.suggest_list = [value_choose]
        self.command()
        if self.command2 is not None:
            self.command2()

    def suggest(self,event):
        input_value = self.normalize_text(self.combobox.get())
        if input_value == "":
            self.combobox.configure(values=self.options)  # Hiển thị tất cả nếu không nhập gì
            self.suggest_list = self.options
            self.command3()
        else:
            # Lọc danh sách dựa trên kí tự đầu của input_value
            values = [x for x in self.options if self.normalize_text(x).startswith(input_value)]
            self.combobox.configure(values=values)  # Cập nhật danh sách gợi ý
            self.suggest_list = values
        if self.command3 is not None:
            self.command3()

    def getsuggestlist(self):
        return self.suggest_list

    def grid(self,row,column):
        self.combobox.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)

    def get(self):
        return self.combobox.get()
    
    def configure(self,values):
        self.combobox.configure(values=values)
