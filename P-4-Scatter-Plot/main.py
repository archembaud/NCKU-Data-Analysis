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

    # Now let's make a 3D scatter plot of SepalLength, SepalWidth, and PetalLength
    # using the setosa_data dataframe.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(setosa_data['SepalLength'], setosa_data['SepalWidth'], setosa_data['PetalLength'], c='r', marker='o')
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')
    ax.set_zlabel('Petal Length')

    # Now, add the data for Iris-versicolor in a different color
    versicolor_data = data[data['Class'] == 'Iris-versicolor']
    ax.scatter(versicolor_data['SepalLength'], versicolor_data['SepalWidth'], versicolor_data['PetalLength'], c='b', marker='o') 

    # Show the plot
    ax.set_title('3D Scatter Plot of Iris-setosa and Iris-versicolor')
    plt.show()
