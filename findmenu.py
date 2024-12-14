import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import unicodedata

class findbox():
    def __init__(self, combobox,values) -> None:
        self.options = values
        self.combobox = combobox
        self.combobox.bind("<KeyRelease>", self.suggest)
        self.combobox.bind("<<ComboboxSelected>>", self.value_combobox)

    @staticmethod
    def normalize_text(text):
        # Loại bỏ dấu và chuyển văn bản thành chữ thường
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8').lower()

    def value_combobox(self, event):
        value_choose = self.combobox.get()
        self.combobox.set(value_choose)
        self.combobox.configure(values=self.options)  # Đặt lại danh sách gốc

    def suggest(self, event):
        input_value = self.normalize_text(self.combobox.get())
        if input_value == "":
            self.combobox.configure(values=self.options)  # Hiển thị tất cả nếu không nhập gì
        else:
            # Lọc danh sách dựa trên giá trị nhập
            values = [x for x in self.options if input_value in self.normalize_text(x)]
            self.combobox.configure(values=values)  # Cập nhật danh sách gợi ý
