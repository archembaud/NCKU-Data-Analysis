import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    # The wine quality dataset uses a ; delimeter!
    data = pd.read_csv(file_path, sep=';')
    print("Initial Data:")
    print(data.head())
    return data


if __name__ == "__main__":
    file_path = './../Data/winequality-white.csv'
    print(f"Loading data from {file_path}")
    df = load_data(file_path)
    # Show the number of rows
    print(f"Number of rows before dropping bad volatile acidity values: {len(df)}")

    # Try computing the mean volalite_acidity
    # This fails - I'll put it in a try - except to test
    try:
        mean_acidity = pd.to_numeric(df['volatile_acidity']).mean()
    except:
        print("There was an error when attempting to compute the mean of volatile acidity")

    # Find rows which hold bad values for volatile acidity 
    # This is data which is not holding a number, but holds some other text.
    # We can check the data in volatile_acidity is a number using the to_numeric
    # function included with Pandas
    is_bad_data = pd.to_numeric(df['volatile_acidity'], errors='coerce').isnull()
    print(f"Checking which data is bad: {is_bad_data}")
    # Create a new data frame with just the bad data
    bad_df = df[is_bad_data]
    bad_df.to_csv('bad_data.csv')

    # Now we can drop the bad rows
    rows_to_drop = df[is_bad_data].index
    print(f"Dropping {len(rows_to_drop)} rows with acidity levels which are not numbers")
    print(f"Rows we are dropping = {rows_to_drop}")
    # Use the index to drop the rows
    df.drop(rows_to_drop, inplace=True)
    # Show the number of rows after dropping missing values 
    print(f"Number of rows after dropping invalid acidity values: {len(df)}")
    # Save these to file so we can inspect them
    df.to_csv('good_data.csv')

    # Now I can find the mean volatile acidity
    # I can run the map(type) command to see what type the data is.
    print(df['volatile_acidity'].map(type))
    mean_acidity = pd.to_numeric(df['volatile_acidity']).mean()
    print(f"The mean volatile acidity is {mean_acidity}")