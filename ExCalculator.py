import tkinter as tk
from math import sqrt

def calculate_input(input_value):
    if input_value == "C":
        display_var.set("")
    elif input_value == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except:
            display_var.set("Error")
    elif input_value == "√":
        try:
            result = sqrt(float(display_var.get()))
            display_var.set(result)
        except:
            display_var.set("Error")
    else:
        display_var.set(display_var.get() + input_value)

main_window = tk.Tk()
main_window.title("Simple Calculator")
main_window.configure(bg="#1e1e1e")
main_window.geometry("300x400")

menu_bar = tk.Menu(main_window)
main_window.config(menu=menu_bar)

display_var = tk.StringVar()
display = tk.Entry(main_window,textvariable=display_var,font=("Arial", 20),justify="right")
display.grid(row=0,column=0,columnspan=4,sticky="nsew")
display.configure(bg="#2d2d2d",fg="#ffffff",insertbackground="#ffffff")

buttons = [
    "√", ".", "**", "C",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "=", "+"
]

for index, button_text in enumerate(buttons):
    if button_text == "0":
        button = tk.Button(main_window,text=button_text,font=("Arial", 16),command=lambda x=button_text: calculate_input(x))
        button.grid(row=5,column=0,columnspan=2,sticky="nsew")
    elif button_text == "=":
        button = tk.Button(main_window,text=button_text,font=("Arial", 16),command=lambda x=button_text: calculate_input(x))
        button.grid(row=5,column=2,sticky="nsew")
    elif button_text == "+":
        button = tk.Button(main_window,text=button_text,font=("Arial", 16),command=lambda x=button_text: calculate_input(x))
        button.grid(row=5,column=3,sticky="nsew")
    else:
        row = (index // 4) + 1
        col = index % 4
        button = tk.Button(main_window,text=button_text,font=("Arial", 16),command=lambda x=button_text: calculate_input(x))
        button.grid(row=row,column=col,sticky="nsew")
    button.configure(bg="#3e3e3e",fg="#ffffff",activebackground="#565656",activeforeground="#ffffff")

for i in range(6):
    main_window.grid_rowconfigure(i,weight=1)
for j in range(4):
    main_window.grid_columnconfigure(j,weight=1)

def open_currency_converter():
    currency_window = tk.Toplevel(main_window)
    currency_window.title("Currency Converter")
    currency_window.geometry("300x200")
    currency_window.configure(bg="#1e1e1e")

    tk.Label(currency_window,text="Enter amount:",font=("Arial", 12),bg="#1e1e1e",fg="#ffffff").grid(row=0,column=0,padx=10,pady=10,sticky="w")
    amount_entry = tk.DoubleVar()
    tk.Entry(currency_window,textvariable=amount_entry,font=("Arial", 12),bg="#2d2d2d",fg="#ffffff",insertbackground="#ffffff").grid(row=0,column=1,padx=10)
    
    currency_choices = ["USD to THB", "EUR to JPY", "GBP to USD", "THB to USD"]
    selected_currency = tk.StringVar(value=currency_choices[0])
    tk.OptionMenu(currency_window, selected_currency, *currency_choices).config(bg="#3e3e3e",fg="#ffffff")
    tk.OptionMenu(currency_window, selected_currency, *currency_choices).grid(row=1,column=0,columnspan=2,pady=10)
    
    result_label = tk.StringVar()
    
    def convert_currency():
        amount = amount_entry.get()
        selected_conversion = selected_currency.get()
        
        rates = {
            "USD to THB": 35,
            "EUR to JPY": 130,
            "GBP to USD": 1.3,
            "THB to USD": 0.03
        }
        
        result = amount * rates[selected_conversion]
        result_label.set(f"{result:.2f} {selected_conversion.split()[-1]}")
    
    tk.Button(currency_window,text="Convert",command=convert_currency,bg="#3e3e3e",fg="#ffffff",activebackground="#565656").grid(row=2,column=0,columnspan=2,pady=10)
    tk.Label(currency_window,textvariable=result_label,font=("Arial", 12),bg="#1e1e1e",fg="#ffffff").grid(row=3,column=0,columnspan=2)

def open_time_converter():
    time_window = tk.Toplevel(main_window)
    time_window.title("Time Converter")
    time_window.geometry("300x200")
    time_window.configure(bg="#1e1e1e")
    
    tk.Label(time_window,text="Enter time:",font=("Arial", 12),bg="#1e1e1e",fg="#ffffff").grid(row=0,column=0,padx=10,pady=10,sticky="w")
    time_entry = tk.DoubleVar()
    tk.Entry(time_window,textvariable=time_entry,font=("Arial", 12),bg="#2d2d2d",fg="#ffffff",insertbackground="#ffffff").grid(row=0,column=1,padx=10)
    
    time_choices = ["Hours to Minutes", "Hours to Seconds", "Days to Hours"]
    selected_time = tk.StringVar(value=time_choices[0])
    tk.OptionMenu(time_window, selected_time, *time_choices).config(bg="#3e3e3e", fg="#ffffff")
    tk.OptionMenu(time_window, selected_time, *time_choices).grid(row=1,column=0,columnspan=2,pady=10)
    
    result_time = tk.StringVar()
    
    def convert_time():
        time_amount = time_entry.get()
        time_conversion = selected_time.get()
        
        if time_conversion == "Hours to Minutes":
            result = time_amount * 60
            unit = "minutes"
        elif time_conversion == "Hours to Seconds":
            result = time_amount * 3600
            unit = "seconds"
        elif time_conversion == "Days to Hours":
            result = time_amount * 24
            unit = "hours"
        
        result_time.set(f"{result} {unit}")
    
    tk.Button(time_window,text="Convert",command=convert_time,bg="#3e3e3e",fg="#ffffff",activebackground="#565656").grid(row=2,column=0,columnspan=2,pady=10)
    tk.Label(time_window,textvariable=result_time,font=("Arial", 12),bg="#1e1e1e",fg="#ffffff").grid(row=3,column=0,columnspan=2)

def open_temperature_converter():
    temperature_window = tk.Toplevel(main_window)
    temperature_window.title("Temperature Converter")
    temperature_window.geometry("300x200")
    temperature_window.configure(bg="#1e1e1e")
    
    tk.Label(temperature_window,text="Enter temperature:",font=("Arial", 12),bg="#1e1e1e",fg="#ffffff").grid(row=0,column=0,padx=10,pady=10,sticky="w")
    temperature_entry = tk.DoubleVar()
    tk.Entry(temperature_window,textvariable=temperature_entry,font=("Arial", 12),bg="#2d2d2d",fg="#ffffff",insertbackground="#ffffff").grid(row=0,column=1,padx=10)
    
    temperature_choices = ["Celsius to Fahrenheit", "Celsius to Kelvin", "Fahrenheit to Celsius"]
    selected_temperature = tk.StringVar(value=temperature_choices[0])
    tk.OptionMenu(temperature_window, selected_temperature, *temperature_choices).config(bg="#3e3e3e", fg="#ffffff")
    tk.OptionMenu(temperature_window, selected_temperature, *temperature_choices).grid(row=1,column=0,columnspan=2,pady=10)
    
    result_temperature = tk.StringVar()
    
    def convert_temperature():
        temperature = temperature_entry.get()
        temp_conversion = selected_temperature.get()
        
        if temp_conversion == "Celsius to Fahrenheit":
            result = (temperature * 9/5) + 32
            unit = "°F"
        elif temp_conversion == "Celsius to Kelvin":
            result = temperature + 273.15
            unit = "K"
        elif temp_conversion == "Fahrenheit to Celsius":
            result = (temperature - 32) * 5/9
            unit = "°C"
        
        result_temperature.set(f"{result:.2f} {unit}")
    
    tk.Button(temperature_window,text="Convert",command=convert_temperature,bg="#3e3e3e",fg="#ffffff",activebackground="#565656").grid(row=2,column=0,columnspan=2,pady=10)
    tk.Label(temperature_window,textvariable=result_temperature,font=("Arial", 12),bg="#1e1e1e",fg="#ffffff").grid(row=3,column=0,columnspan=2)

menu_bar.add_command(label="Currency",command=open_currency_converter)
menu_bar.add_command(label="Time",command=open_time_converter)
menu_bar.add_command(label="Temperature",command=open_temperature_converter)

main_window.mainloop()
