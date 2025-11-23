import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    print("Initial Data:")
    print(data.head())
    return data

def save_data(data, file_path):
    # Save the dataframe to a CSV file
    data.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    file_path = './../Data/iris.data'
    print(f"Loading data from {file_path}")
    data = load_data(file_path)
    # Now, let's create a new dataframe where the flower type is 'Iris-setosa'
    setosa_data = data[data['Class'] == 'Iris-setosa']
    # Show the number of Iris-setosa flowers
    print(f"Number of Iris-setosa flowers: {len(setosa_data)}")
    # Show what type of variable this is (hint: it's a DataFrame)
    print(f"Type of setosa_data: {type(setosa_data)}")
    # Save this to CSV for manual verification
    save_data(setosa_data, 'setosa_data.csv')
