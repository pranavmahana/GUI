import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.widgets import RectangleSelector
import pandas as pd

class VibrationAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Vibration Analyzer")
        self.master.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.graph_frame = ttk.Frame(self.master)
        self.graph_frame.pack(fill=tk.BOTH, expand=True)

        self.fig, self.ax = plt.subplots(3, 1, figsize=(6, 6))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.load_csv1_button = ttk.Button(self.master, text="Load CSV for Graph 1", command=lambda: self.load_csv(0))
        self.load_csv1_button.pack()

        self.load_csv2_button = ttk.Button(self.master, text="Load CSV for Graph 2", command=lambda: self.load_csv(1))
        self.load_csv2_button.pack()

        self.load_csv3_button = ttk.Button(self.master, text="Load CSV for Graph 3", command=lambda: self.load_csv(2))
        self.load_csv3_button.pack()

        self.select_button = ttk.Button(self.master, text="Select Part", command=self.select_part)
        self.select_button.pack()

        self.rectSelectors = []

    def load_csv(self, idx):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                # Assume the first column is time and the rest are data columns
                time = df.iloc[:, 0]
                data_col = df.iloc[:, 1]

                self.ax[idx].plot(time, data_col)

                self.canvas.draw()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def select_part(self):
        try:
            for rs in self.rectSelectors:
                rs.set_active(False)

            messagebox.showinfo("Select Part", "Select the part by clicking and dragging on the graph.")

            for ax in self.ax:
                rs = RectangleSelector(ax, self.onselect, drawtype='box', useblit=True, button=[1], 
                                       minspanx=5, minspany=5, spancoords='pixels', interactive=True)
                self.rectSelectors.append(rs)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def onselect(self, eclick, erelease):
        xmin, xmax = eclick.xdata, erelease.xdata
        ymin, ymax = eclick.ydata, erelease.ydata

        for ax in self.ax:
            ax.set_xlim(xmin, xmax)
            ax.set_ylim(ymin, ymax)

        self.canvas.draw()

def main():
    root = tk.Tk()
    app = VibrationAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
