import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    return data

def generate_report(subject_name, dataframe):
    # Create a simple Markdown file containing statistics from the chosen subject
    with open("Report.md", "w") as file:
        file.write(f"# Subject Report for {subject_name}\n")
        file.write("\n")
        file.write("## Mean score\n")
        file.write(f"The mean score for {subject_name} is {dataframe['score'].mean()}")
        file.write("\n")

        # Now write the details of the top 5 students
        file.write("## Top 5 Student Report \n")
        # Create a markdown table
        file.write('| Student ID | Score |\n ')
        file.write('|-|-|\n ')
        for student_index in range(5):
            student_number =  dataframe.iloc[student_index]['student_id']
            '''
            Note: we cannot use
                student_number = dataframe.loc[student_index, 'student_id']

            because loc uses the real index - the original index - in the unsorted, original dataframe.

            In the case above, student_index starts with 0.

            Using loc will attempt to fetch row 0s student ID, which is E14104357.
            However, trying to fetch 0 here using loc will cause an error. Why?

            Because row 0's subject was Art - not geography. So that original row 0 data is not present
            in this dataframe. Pandas will throw an error.

            No, we want to first 5 rows in this sorted frame - rows 0 to 4 - based on their sorted row
            position. So we use iloc.

            '''
            student_score = dataframe.iloc[student_index]['score']
            file.write(f"|{student_number}|{student_score}| \n")




if __name__ == "__main__":
    file_path = './../Data/broken_exams_data.csv'
    print(f"Loading data from {file_path}")
    df = load_data(file_path)
    
    target_subject = 'Geography'

    # Find all the results for geography
    target_rows = df['subject'] == target_subject
    target_df = df[target_rows]

    # Sort based on score - this will sort from low to high
    sorted_df = target_df.sort_values(by='score')
    print(sorted_df)

    # Sort again - this time, from high to low
    sorted_df = target_df.sort_values(by='score', ascending=False)
    print(sorted_df)

    # Generate the report
    generate_report(target_subject, sorted_df)