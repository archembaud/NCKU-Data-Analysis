import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load data from a CSV file
    # The wine quality dataset uses a ; delimeter!
    data = pd.read_csv(file_path, sep=';')
    print("Initial Data:")
    print(data.head())
    return data


if __name__ == "__main__":
    file_path = './../../Data/winequality-red.csv'
    print(f"Loading data from {file_path}")
    df = load_data(file_path)

    # Cleam the quality, alcohol and pH
    list_to_clean = ['alcohol', 'pH', 'quality']
    for item in list_to_clean:
        is_bad_data = pd.to_numeric(df[item], errors='coerce').isnull()
        rows_to_drop = df[is_bad_data].index
        df.drop(rows_to_drop, inplace=True)
        print(f'Dropped {len(rows_to_drop)} rows while cleaning {item}')
        # Since this table contained stringy data, Pandas has opened the whole dataframe
        # as string type objects.
        # Now that we have removed these, we can directly convert the columns we
        # are interested in to proper numbers.
        df[item] = pd.to_numeric(df[item], errors="coerce")

    # Set up a scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # The code below could be collected into a for loop.
    # However, since you are all learning python, this is clearer.

    # Find quality 6
    mid_df = df[df['quality'] == 6]
    print(f'Found {len(mid_df)} wines with quality 6')
    ax.scatter(mid_df['alcohol'], mid_df['pH'], c='r', marker='.')

    # Quality 7
    mid_df = df[df['quality'] == 7]
    print(f'Found {len(mid_df)} wines with quality 7')
    ax.scatter(mid_df['alcohol'], mid_df['pH'], c='b', marker='.')

    # Quality 8
    mid_df = df[df['quality'] == 8]
    print(f'Found {len(mid_df)} wines with quality 8')
    ax.scatter(mid_df['alcohol'], mid_df['pH'], c='g', marker='o')

    # Quality 9
    mid_df = df[df['quality'] == 9]
    print(f'Found {len(mid_df)} wines with quality 9')
    ax.scatter(mid_df['alcohol'], mid_df['pH'], c='k', marker='o')

    # Add details and show
    plt.title('Scatter plot showing alcohol content and pH vs quality')
    plt.legend(['Quality = 6', 'Quality = 7', 'Quality = 8', 'Quality = 9'])
    plt.xlabel('Alcohol Content')
    plt.ylabel('pH level')
    plt.show()
