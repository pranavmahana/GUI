import pandas as pd
import numpy as np

# Global variable to keep track of file counter
file_counter = 1

def generate_velocity_profile(num_samples, sampling_frequency, min_velocity, max_velocity):
    # Generate time values
    time_values = np.arange(num_samples) / sampling_frequency

    # Linearly interpolate velocity values between min and max velocity
    velocity_data = np.linspace(min_velocity, max_velocity, num_samples)

    # Create a DataFrame with time values and velocity data
    df = pd.DataFrame({'Time': time_values, 'Velocity': velocity_data})

    return df

def save_velocity_profile_to_csv(data):
    global file_counter
    filename = f"velocity_profile_{file_counter}.csv"
    data.to_csv(filename, index=False)
    print(f"CSV velocity profile saved: {filename}")
    file_counter += 1

def save_velocity_profile_to_excel(data):
    global file_counter
    filename = f"velocity_profile_{file_counter}.xlsx"
    data.to_excel(filename, index=False)
    print(f"Excel velocity profile saved: {filename}")
    file_counter += 1

if __name__ == "__main__":
    # Parameters for generating velocity profile
    num_samples = 1000  # Number of samples
    sampling_frequency = 25000  # Sampling frequency in Hz

    # Ask user for maximum and minimum velocity range
    min_velocity = float(input("Enter the minimum velocity: "))
    max_velocity = float(input("Enter the maximum velocity: "))

    # Generate velocity profile
    velocity_df = generate_velocity_profile(num_samples, sampling_frequency, min_velocity, max_velocity)

    # Save velocity profile to CSV
    save_velocity_profile_to_csv(velocity_df)

    # Save velocity profile to Excel
    save_velocity_profile_to_excel(velocity_df)
