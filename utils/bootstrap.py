import tkinter as tk
from utils.lsm import LSM


def run(lsm: LSM):
    window = tk.Tk()
    window.title("Метод найменших квадратів")

    x = "5, 6, 7, 8, 9, 30"
    y = "101, 106, 118, 124, 130, 145"

    independent_values_entry = tk.Entry(window, width=30)
    independent_values_entry.insert(0, x)
    independent_value_name = tk.Entry(window, width=15)
    independent_value_name.insert(0, "x")

    dependent_values_entry = tk.Entry(window, width=30)
    dependent_values_entry.insert(0, y)
    dependent_value_name = tk.Entry(window, width=15)
    dependent_value_name.insert(0, "y")

    independent_values_entry.grid(column=1, row=1, padx=30, pady=15)
    independent_value_name.grid(column=2, row=1, padx=30, pady=15)

    dependent_values_entry.grid(column=1, row=2, padx=30, pady=15)
    dependent_value_name.grid(column=2, row=2, padx=30, pady=15)

    dependent_label = tk.Label(window, text="Введіть вік піддослідних (через кому)")
    independent_label = tk.Label(window, text="Введіть зріст піддослідних (через кому)")

    dependent_label.grid(column=0, row=1)
    independent_label.grid(column=0, row=2)

    btn = tk.Button(window, text="Показати графік",
                    command=lambda: lsm.show_plot(window,
                                                  independent_values_entry, dependent_values_entry,
                                                  independent_value_name, dependent_value_name))
    btn.grid(column=0, columnspan=3, row=0, padx=10, pady=5)

    window.mainloop()
