import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    file_path = './../Data/iris.data'
    print(f"Loading data from {file_path}")
    data = load_data(file_path)
    
    # Now, let's create a new dataframe where the flower type is 'Iris-setosa'
    setosa_data = data[data['Class'] == 'Iris-setosa']

    # Compute the mean sepal length for Iris-setosa
    mean_sepal_length = setosa_data['SepalLength'].mean()
    print(f"Mean Sepal Length of Iris-setosa: {mean_sepal_length}")
    std_dev_sepal_length = setosa_data['SepalLength'].std()
    print(f"Standard Deviation of Sepal Length of Iris-setosa: {std_dev_sepal_length}")

    # Create a histogram of the sepal lengths of Iris-setosa flowers
    # Plot a histogram of the 'Value' column
    setosa_data['SepalLength'].hist(bins=30, edgecolor='black')
    plt.title('Distribution of Sepal Lengths of Iris-setosa')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
