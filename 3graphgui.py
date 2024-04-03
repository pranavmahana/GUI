import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.signal import find_peaks
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

        self.load_data_button = ttk.Button(self.master, text="Load Data", command=self.load_data)
        self.load_data_button.pack()

        self.select_button = ttk.Button(self.master, text="Select Part", command=self.select_part)
        self.select_button.pack()

        self.load_csv_button = ttk.Button(self.master, text="Load CSV", command=self.load_csv)
        self.load_csv_button.pack()

    def load_data(self):
        # Example data loading function
        time = np.linspace(0, 10, 1000)
        data1 = np.sin(2 * np.pi * 5 * time)
        data2 = np.sin(2 * np.pi * 2 * time)
        data3 = np.sin(2 * np.pi * 1 * time)

        self.ax[0].plot(time, data1)
        self.ax[1].plot(time, data2)
        self.ax[2].plot(time, data3)

        self.canvas.draw()

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            try:
                df = pd.read_csv(file_path)
                # Assume the first column is time and the rest are data columns
                time = df.iloc[:, 0]
                data_cols = df.iloc[:, 1:]

                for i, data_col in enumerate(data_cols.columns):
                    self.ax[i].plot(time, data_cols[data_col])

                self.canvas.draw()
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def select_part(self):
        try:
            xmin, xmax = self.ax[0].get_xlim()
            ymin, ymax = self.ax[0].get_ylim()
            rect = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, facecolor='yellow', alpha=0.5)
            self.ax[0].add_patch(rect)

            self.canvas.draw()

            messagebox.showinfo("Select Part", "Select the part by clicking and dragging on the graph.")

            def onselect(eclick, erelease):
                x0, y0 = eclick.xdata, eclick.ydata
                x1, y1 = erelease.xdata, erelease.ydata

                new_data = self.ax[0].get_lines()[0].get_ydata()
                mask = (new_data >= min(y0, y1)) & (new_data <= max(y0, y1))
                new_data = new_data[mask]

                time = np.linspace(0, len(new_data), len(new_data))
                self.ax[0].cla()
                self.ax[0].plot(time, new_data)

                self.canvas.draw()

                # Calculate RMS data
                rms = np.sqrt(np.mean(new_data ** 2))
                messagebox.showinfo("RMS Data", f"RMS: {rms}")

            self.fig.canvas.mpl_connect('button_press_event', onselect)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = VibrationAnalyzerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
