import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    print("Initial Data:")
    print(data.head())
    return data


if __name__ == "__main__":
    file_path = './../Data/adult.data'
    print(f"Loading data from {file_path}")
    df = load_data(file_path)
    # Show the column names
    print("Column names:")
    print(df.columns)
    # Show the number of rows
    print(f"Number of rows before dropping missing values: {len(df)}")
    # Drop rows with missing values
    # In this data, missing values are represented by '?'
    # It's possible these are either in the occupation column, or the country column
    # But there are spaces around the '?' so we need to strip those first
    rows_to_drop = df[df['Occupation'].str.strip() == "?"].index
    print(f"Dropping {len(rows_to_drop)} rows with missing Occupation values")
    # Use the index to drop the rows
    df.drop(rows_to_drop, inplace=True)
    # Show the number of rows after dropping missing values 
    print(f"Number of rows after dropping missing values: {len(df)}")