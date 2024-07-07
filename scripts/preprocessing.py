import pandas as pd
import numpy as np
import os

def preprocess_data(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}. Please provide the correct file path.")
    
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Check if 'Date' and 'Price' columns exist
    if 'Date' not in data.columns or 'Price' not in data.columns:
        raise ValueError("The input file must contain 'Date' and 'Price' columns.")
    
    # Convert the date column to datetime format
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    
    # Drop rows with invalid dates
    data = data.dropna(subset=['Date'])
    
    # Handle missing values in the 'Price' column - Here, we fill with the previous value
    data['Price'] = data['Price'].fillna(method='ffill')
    
    # Handle outliers - Here, we use IQR method to cap outliers
    Q1 = data['Price'].quantile(0.25)
    Q3 = data['Price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data['Price'] = np.where(data['Price'] < lower_bound, lower_bound, data['Price'])
    data['Price'] = np.where(data['Price'] > upper_bound, upper_bound, data['Price'])
    
    # Normalize the data for machine learning models
    data['Price'] = (data['Price'] - data['Price'].min()) / (data['Price'].max() - data['Price'].min())
    
    return data

if __name__ == "__main__":
    # File path to the dataset - Update this path as needed
    file_path = 'C:/Users/Lenovo/Desktop/Dev/brent-oil-analysis/data/raw/BrentOilPrices.csv'
    
    try:
        # Preprocess the data
        processed_data = preprocess_data(file_path)
        
        # Ensure the processed data directory exists
        output_dir = 'C:/Users/Lenovo/Desktop/Dev/brent-oil-analysis/data/processed'
        os.makedirs(output_dir, exist_ok=True)
        
        # Save the processed data
        output_file_path = os.path.join(output_dir, 'BrentOilPrices_preprocessed.csv')
        processed_data.to_csv(output_file_path, index=False)
        
        print(f"Data preprocessing complete. Processed data saved to '{output_file_path}'.")
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
