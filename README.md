# NCKU-Data-Analysis
Codes and documentation for my course on Data Analysis, using Pandas and Julia.

This material is covered as part of the semester 2 subject "Python資料分析入門" (Introduction to Data Analysis in Python), although (be warned!) there is some Julia covered as part of this course.

## Julia Examples and README file

You can find out more about the Julia examples covered as part of this course [here](./JULIA.md).

## Pandas Examples

The examples using Pandas for data loading, manipulation and analysis are shown below.

### P-1 Hello World

This python script:

* Loads the Iris dataset in the /Data directory into a Pandas dataframe,
* Shows the first few rows of the dataframe.

To run this - navigate to the folder first, and then run the python script. From the root of this directory:

```
cd P-1-Hello-World
python main.py
```

If working, this should be the output:

```
Loading data from ./../Data/iris.data
Initial Data:
   SepalLength  SepalWidth  PetalLength  PetalWidth        Class
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa
```

### P-2 Extract Data

This python script:

* Loads the Iris dataset in the /Data directory into a Pandas dataframe,
* From the Iris dataframe, creates a new dataframe containing a subset of the Iris dataframe,
* Saves the subset to file (CSV)

To run this:

```
P-2-Extract-Data
python main.py
```

If this worked, you'll see this output:

```
Loading data from ./../Data/iris.data
Initial Data:
   SepalLength  SepalWidth  PetalLength  PetalWidth        Class
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa
Number of Iris-setosa flowers: 50
Type of setosa_data: <class 'pandas.core.frame.DataFrame'>
Data saved to setosa_data.csv
```