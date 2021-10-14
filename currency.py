import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk
import re


class Converter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, fcurrency, tcurrency, amount):
        initial_amount = amount
        if fcurrency != 'USD':
            amount = amount / self.currencies[fcurrency]

        amount = round(amount * self.currencies[tcurrency], 4)
        return amount

def clear_all(self) :
	self.amount_field.delete(0, END)
    
	

class App(tk.Tk):

    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Currency Converter'
        self.currency_converter = converter

        self.configure(background = 'black')
        self.geometry("500x250")

       
        self.intro_label = Label(self, text ='   Welcome to the Currency Convertor   ', fg='black', relief=tk.RAISED)
        self.intro_label.config(font=('Courier', 15, 'bold'))

        self.id_label1 = Label(self, text ='   19DIT065   ', fg='black', relief=tk.RAISED)
        self.id_label1.config(font=('Courier', 15, 'bold'))
        self.id_label1.place(x=10, y=50)

        self.id_label2 = Label(self, text ='   19DIT081   ', fg='black', relief=tk.RAISED)
        self.id_label2.config(font=('Courier', 15, 'bold'))
        self.id_label2.place(x=310, y=50)

        self.date_label = Label(self, text=f"Date : {self.currency_converter.data['date']}", relief=tk.GROOVE, borderwidth=5)

        self.intro_label.place(x=10, y=5)
        self.date_label.place(x=195, y=100)

        
    
        self.amount_field = Entry(self, bd=3, relief=tk.RIDGE, justify=tk.CENTER, validate='key')
        self.converted_amount_field_label = Label(self, text='', fg='blue', bg='white', relief=tk.RIDGE, justify=tk.CENTER, width=17, borderwidth=3)

        
        self.from_currency_variable = StringVar(self)
        self.from_currency_variable.set("INR")  
        self.to_currency_variable = StringVar(self)
        self.to_currency_variable.set("USD") 

        font = ("Courier", 12, "bold")
        self.option_add('*TCombobox*Listbox.font', font)
        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.currency_converter.currencies.keys()), font=font,
                                                   state='readonly', width=12, justify=tk.CENTER)
        self.to_currency_dropdown = ttk.Combobox(self, textvariable=self.to_currency_variable,
                                                 values=list(self.currency_converter.currencies.keys()), font=font,
                                                 state='readonly', width=12, justify=tk.CENTER)

       
        self.from_currency_dropdown.place(x=30, y=150)
        self.amount_field.place(x=36, y=200)
        self.to_currency_dropdown.place(x=325, y=150)
        self.converted_amount_field_label.place(x=335, y=200)

        
        self.convert_button = Button(self, text="Convert", bg="green", fg="black", command=self.perform)
        self.convert_button.config(font=('Courier', 10, 'bold'))
        self.convert_button.place(x=220, y=150)

        self.clear_button = Button(self, text = "Clear", bg = "grey", fg = "black", command = clear_all)
        self.clear_button.place(x=235, y=200)

    def perform(self):
        amount = float(self.amount_field.get())
        from_curr = self.from_currency_variable.get()
        to_curr = self.to_currency_variable.get()

        converted_amount = self.currency_converter.convert(from_curr, to_curr, amount)
        converted_amount = round(converted_amount, 2)

        self.converted_amount_field_label.config(text=str(converted_amount))



if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = Converter(url)

    App(converter)
    mainloop()