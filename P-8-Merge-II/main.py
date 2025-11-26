import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    file_path = './../Data/broken_students_data.csv'
    print(f"Loading data from {file_path}")
    students_df = load_data(file_path)
    file_path = './../Data/broken_exams_data.csv'
    print(f"Loading data from {file_path}")
    exams_df = load_data(file_path)
    # We know that some of these exams are missing student records
    # Let's count
    print(f"Number of exam records: {len(exams_df)}")
    # Perform an inner merge this time to keep only matching records
    # This will drop any exam records without a matching student
    merged_df = pd.merge(exams_df, students_df[['student_id', 'surname', 'firstname']], on='student_id', how='inner')
    # Count the numebr of records after the merge
    print(f"Number of exam records after inner merge: {len(merged_df)}")
    # Create a dataframe holding the dropped exam records
    dropped_exams_df = exams_df[~exams_df['student_id'].isin(merged_df['student_id'])]
    print(f"Number of dropped exam records: {len(dropped_exams_df)}")
    # Save these to file
    dropped_exams_df.to_csv('dropped_exams_data.csv', index=False)