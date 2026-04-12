import pandas as pd
import statistics

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

    # Export the whole column for petals width to a list
    # This allows us to use other packages to perform analysis
    petal_width = list(data['PetalWidth'])

    # Find the mean petal width using statistics
    print(f"Average petal width for all classes = {statistics.mean(petal_width)}")

    # Find the mean petal width using panda's built in mean() function
    print(f"The PetalWidth column of the dataframe is type = {type(data['PetalWidth'])}")
    print(f"Average petal width for all classes = {data['PetalWidth'].mean()}")


