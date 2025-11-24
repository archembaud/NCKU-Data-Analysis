import pandas as pd

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    return data


if __name__ == "__main__":
    file_path = './../Data/SmallStudentSet/students_data.csv'
    print(f"Loading data from {file_path}")
    students_df = load_data(file_path)
    file_path = './../Data/SmallStudentSet/exams_data.csv'
    print(f"Loading data from {file_path}")
    exams_df = load_data(file_path)
    # Let's match the student ID to move the name into the exams dataframe
    merged_df = pd.merge(exams_df, students_df[['student_id', 'surname', 'firstname']], on='student_id', how='left')
    # Show the first few rows of the merged dataframe
    print(merged_df.head())
    # Save the merged dataframe to a new CSV file
    merged_df.to_csv("exams_with_names.csv", index=False)
