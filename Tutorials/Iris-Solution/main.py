import pandas as pd
import matplotlib.pyplot as plt
import math

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    file_path = './../../Data/iris.data'
    print(f"Loading data from {file_path}")
    data = load_data(file_path)


    # Data I care about - what is this flower?
    # SepalLength: 7.18, SepalWidth: 3.59, PetalLidth: 6.09, PetalWidth: 2.49
    my_flower = [7.18, 3.59, 6.09, 2.49] 



    # Now, let's create a new dataframe where the flower type is 'Iris-setosa'
    setosa_data = data[data['Class'] == 'Iris-setosa']
    # Do the same for virginica and versicolor
    virginica_data = data[data['Class'] == 'Iris-virginica']
    versicolor_data = data[data['Class'] == 'Iris-versicolor']

    # Create a histogram of the sepal lengths of all flowers
    # We can use different colours to capture the different flows
    setosa_data['SepalLength'].hist(bins=30, edgecolor='black', color='blue')
    virginica_data['SepalLength'].hist(bins=30, edgecolor='black', color='red', alpha=0.8)
    versicolor_data['SepalLength'].hist(bins=30, edgecolor='black', color='green',alpha=0.7)
    plt.legend(["Setosa", "Virginica", "Versicolor"])
    # Now add my plot to the data - Sepal Length for my flower
    plt.plot([my_flower[0], my_flower[0]], [-0.5, 5], color='black')

    plt.title('Distribution of Sepal Lengths of all Iris types')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('SepalLength.png')
    plt.close()

    # Create a new histogram of the sepal width of all flowers
    setosa_data['SepalWidth'].hist(bins=30, edgecolor='black', color='blue')
    virginica_data['SepalWidth'].hist(bins=30, edgecolor='black', color='red', alpha=0.8)
    versicolor_data['SepalWidth'].hist(bins=30, edgecolor='black', color='green',alpha=0.7)
    plt.legend(["Setosa", "Virginica", "Versicolor"])
    # Now add my plot to the data - Sepal Width for my flower
    plt.plot([my_flower[1], my_flower[1]], [-0.5, 5], color='black')

    plt.title('Distribution of Sepal Widths of all Iris types')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('SepalWidth.png')
    plt.close()

    # Now make histograms of all the petal lengths
    setosa_data['PetalLength'].hist(bins=30, edgecolor='black', color='blue')
    virginica_data['PetalLength'].hist(bins=30, edgecolor='black', color='red', alpha=0.8)
    versicolor_data['PetalLength'].hist(bins=30, edgecolor='black', color='green',alpha=0.7)
    plt.legend(["Setosa", "Virginica", "Versicolor"])
    # Now add my plot to the data - Petal length for my flower
    plt.plot([my_flower[2], my_flower[2]], [-0.5, 5], color='black')

    plt.title('Distribution of Petal Lengths of all Iris types')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('PetalLength.png')
    plt.close()

    # Now make histograms of all the petal widths
    setosa_data['PetalWidth'].hist(bins=30, edgecolor='black', color='blue')
    virginica_data['PetalWidth'].hist(bins=30, edgecolor='black', color='red', alpha=0.8)
    versicolor_data['PetalWidth'].hist(bins=30, edgecolor='black', color='green',alpha=0.7)
    plt.legend(["Setosa", "Virginica", "Versicolor"])
    # Now add my plot to the data - Petal Width for my flower
    plt.plot([my_flower[3], my_flower[3]], [-0.5, 5], color='black')

    plt.title('Distribution of Petal Widths of all Iris types')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('PetalWidth.png')
    plt.close()

    # These graphs show quite clearly what the flower type is. But we need to use our eyes; and that's no good.
    # We can use the z-scores - assuming a normal distribution - to show us which flower it is.
    # We need to compute 4 scores for each flower. The flower type that has the lowest z-scores
    # over each of the properties - that's our flower.
    setosa_zscores = []
    virginica_zscores = []
    versicolor_zscores = []

    # Compute the mean and dev for sepal length for Iris-setosa, and compute the z-score
    mean_value = setosa_data['SepalLength'].mean()
    stddev_value = setosa_data['SepalLength'].std()
    print(f"Setosa: mean and std deviation of sepal length = {mean_value}, {stddev_value}")
    data_point = my_flower[0]
    setosa_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Repeat for Sepal Width
    mean_value = setosa_data['SepalWidth'].mean()
    stddev_value = setosa_data['SepalWidth'].std()
    print(f"Setosa: mean and std deviation of sepal width = {mean_value}, {stddev_value}")
    data_point = my_flower[1]
    setosa_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Petal Length
    mean_value = setosa_data['PetalLength'].mean()
    stddev_value = setosa_data['PetalLength'].std()
    print(f"Setosa: mean and std deviation of petal length = {mean_value}, {stddev_value}")
    data_point = my_flower[2]
    setosa_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Petal Width
    mean_value = setosa_data['PetalWidth'].mean()
    stddev_value = setosa_data['PetalWidth'].std()
    print(f"Setosa: mean and std deviation of petal width = {mean_value}, {stddev_value}")
    data_point = my_flower[3]
    setosa_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now

    # Repeat the above steps, using virginica instead of setosa
    mean_value = virginica_data['SepalLength'].mean()
    stddev_value = virginica_data['SepalLength'].std()
    print(f"Virginica: mean and std deviation of sepal length = {mean_value}, {stddev_value}")
    data_point = my_flower[0]
    virginica_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Repeat for Sepal Width
    mean_value = virginica_data['SepalWidth'].mean()
    stddev_value = virginica_data['SepalWidth'].std()
    print(f"Virginica: mean and std deviation of sepal width = {mean_value}, {stddev_value}")
    data_point = my_flower[1]
    virginica_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Petal Length
    mean_value = virginica_data['PetalLength'].mean()
    stddev_value = virginica_data['PetalLength'].std()
    print(f"Virginica: mean and std deviation of petal length = {mean_value}, {stddev_value}")
    data_point = my_flower[2]
    virginica_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Petal Width
    mean_value = virginica_data['PetalWidth'].mean()
    stddev_value = virginica_data['PetalWidth'].std()
    print(f"Virginica: mean and std deviation of petal widths = {mean_value}, {stddev_value}")
    data_point = my_flower[3]
    virginica_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now

    # Repeat the above steps, using versicolor now
    mean_value = versicolor_data['SepalLength'].mean()
    stddev_value = versicolor_data['SepalLength'].std()
    print(f"Versicolor: mean and std deviation of sepal length = {mean_value}, {stddev_value}")
    data_point = my_flower[0]
    versicolor_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Repeat for Sepal Width
    mean_value = versicolor_data['SepalWidth'].mean()
    stddev_value = versicolor_data['SepalWidth'].std()
    print(f"Versicolor: mean and std deviation of sepal width = {mean_value}, {stddev_value}")
    data_point = my_flower[1]
    versicolor_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Petal Length
    mean_value = versicolor_data['PetalLength'].mean()
    stddev_value = versicolor_data['PetalLength'].std()
    print(f"Versicolor: mean and std deviation of petal length = {mean_value}, {stddev_value}")
    data_point = my_flower[2]
    versicolor_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now
    # Petal Width
    mean_value = versicolor_data['PetalWidth'].mean()
    stddev_value = versicolor_data['PetalWidth'].std()
    print(f"Versicolor: mean and std deviation of petal width = {mean_value}, {stddev_value}")
    data_point = my_flower[3]
    versicolor_zscores.append(abs((data_point - mean_value)/stddev_value))  # Use the absolute value for now

    # Now print the scores
    print(f"Z Scores using Iris-setosa statistics: {setosa_zscores}")
    print(f"Z Scores using Iris-virginica statistics: {virginica_zscores}")
    print(f"Z Scores using Iris-versicolor statistics: {versicolor_zscores}")

    # Compute the overall Z-score
    print(f"Overall Z-score for Iris-Setosa: {math.sqrt(sum(x**2 for x in setosa_zscores))}")
    print(f"Overall Z-score for Iris-Virginica: {math.sqrt(sum(x**2 for x in virginica_zscores))}")
    print(f"Overall Z-score for Iris-Versicolor: {math.sqrt(sum(x**2 for x in versicolor_zscores))}")    