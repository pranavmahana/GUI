import pandas as pd
import numpy as np

# Global variable to keep track of file counter
file_counter = 1

def generate_data(num_samples, num_channels, sampling_frequency):
    # Generate time values
    time_values = np.arange(num_samples) / sampling_frequency

    # Generate random vibration data for each channel
    data = np.random.rand(num_samples, num_channels)

    # Create a DataFrame with time values as the first column
    df = pd.DataFrame(data, columns=[f"Channel_{i+1}" for i in range(num_channels)])
    df.insert(0, "Time", time_values)

    return df

def save_to_csv(data):
    global file_counter
    filename = f"vibration_data_{file_counter}.csv"
    data.to_csv(filename, index=False)
    print(f"CSV file saved: {filename}")
    file_counter += 1

def save_to_excel(data):
    global file_counter
    filename = f"vibration_data_{file_counter}.xlsx"
    data.to_excel(filename, index=False)
    print(f"Excel file saved: {filename}")
    file_counter += 1

if __name__ == "__main__":
    # Parameters for generating data
    num_samples = 1000  # Number of samples
    num_channels = 6    # Number of channels
    sampling_frequency = 25000  # Sampling frequency in Hz

    # Generate data
    df = generate_data(num_samples, num_channels, sampling_frequency)

    # Save data to CSV
    save_to_csv(df)

    # Save data to Excel
    save_to_excel(df)
