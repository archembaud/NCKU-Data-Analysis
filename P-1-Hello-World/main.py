import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    
    # Display the first few rows of the dataframe
    print("Initial Data:")
    print(data.head())    
    return data

if __name__ == "__main__":
    file_path = './../Data/iris.data'
    print(f"Loading data from {file_path}")
    data = load_data(file_path)