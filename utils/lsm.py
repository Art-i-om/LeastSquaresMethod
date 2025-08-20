import tkinter
from tkinter import messagebox
from tkinter.messagebox import showerror

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re


class LSM:
    def __init__(self):
        self.canvas = None
        self.a = None
        self.b = None

    def calculate_coefficients(self, x, y):
        n = len(x)

        sum_x = sum(x)
        sum_y = sum(y)
        sum_xy = sum(x[i] * y[i] for i in range(n))
        sum_x2 = sum(xi ** 2 for xi in x)

        self.a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
        self.b = (sum_y - self.a * sum_x) / n

        return self.a, self.b

    def calculate_sigma(self, x, y):
        n = len(x)
        ssr = sum((y[i] - (self.a * x[i] + self.b))**2 for i in range(n))
        return ssr, (ssr / (n - 2)) ** 0.5

    def show_plot(self, window,
                  independent_values_entry, dependent_values_entry,
                  independent_values_name, dependent_values_name):
        if self.canvas is not None:
            self.canvas.get_tk_widget().destroy()

        try:
            x = list(map(int, re.sub(r"\s+", "", independent_values_entry.get()).split(',')))
            y = list(map(int, re.sub(r"\s+", "", dependent_values_entry.get()).split(',')))

            if len(x) != len(y):
                raise ValueError(f"Length mismatch: x has {len(x)}, y has {len(y)}.")
            if len(x) < 2:
                raise ValueError("Need at least 2 points.")

            a, b = self.calculate_coefficients(x, y)
            sigma_raw, sigma_rate = self.calculate_sigma(x, y)
        except ValueError as exc:
            messagebox.showerror("Input error", str(exc))
            return
        except Exception as exc:
            messagebox.showerror("Unexpected error occurred", str(exc))

        fig, ax = plt.subplots(figsize=(7, 5))
        ax.scatter(x, y, color='blue', label='Дані')

        for xi, yi in zip(x, y):
            ax.text(xi, yi, f'({xi}, {yi})', fontsize=9, ha='right', va='bottom')

        y_pred = [a * xi + b for xi in x]
        ax.plot(x, y_pred, color='red', label=f'y = {a:.2f}x + {b:.2f}')

        ax.set_xlabel(independent_values_name.get())
        ax.set_ylabel(dependent_values_name.get())
        ax.legend()
        ax.grid(True, linestyle="--", alpha=0.7)

        a_label = tkinter.Label(window, text=f"параметр а = {self.a:.2f}")
        b_label = tkinter.Label(window, text=f"параметр b = {self.b:.2f}")
        sigma_label = tkinter.Label(window, text=f"параметр σ = {sigma_raw:.2f} або {sigma_rate:.2f}%")

        a_label.grid(column=0, row=3, columnspan=3, pady=10)
        b_label.grid(column=0, row=4, columnspan=3, pady=10)
        sigma_label.grid(column=0, row=5, columnspan=3, pady=10)

        self.canvas = FigureCanvasTkAgg(fig, master=window)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(columnspan=3, row=6, column=0)

    def including(self, *args):
        return self
