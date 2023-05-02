import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)


def convert():
    mile = mile_input.get()
    result = str(round(float(mile) * 1.609, 2))
    result_label.config(text=result)


mile_input = tk.Entry(width=6)
mile_input.grid(column=1, row=0, padx=10, pady=10)

mile_label = tk.Label(text="Miles")
mile_label.grid(column=2, row=0, padx=10, pady=10)

equal_label = tk.Label(text="is equal to")
equal_label.grid(column=0, row=1, padx=10, pady=10)

result_label = tk.Label(text="0")
result_label.grid(column=1, row=1, padx=10, pady=10)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1, padx=10, pady=10)

calc_button = tk.Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2, padx=10, pady=10)

window.mainloop()
