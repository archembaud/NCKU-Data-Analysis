import numpy as np
import pandas as pd


def generate_email_addresses(student_number):
    email = f"{student_number.lower()}@ncku.edu.tw"
    return email


def generate_random_surname():
    surnames = ['Lee', 'Chang', 'Chen', 'Wang', 'Zhang', 'Liu', 'Huang', 'Lin', 'Wu', 'Zhao', 'Yang', 'Xu', 'Sun', 'He', 'Gao', 'Deng', 'Cao', 'Feng', 'Jiang', 'Tang', 'Shi', 'Qian', 'Yuan', 'Xie', 'Zhou', 'Guo', 'Ma', 'Liang', 'Pan', 'Ding', 'Ren']
    selected_surname = np.random.choice(surnames)
    return selected_surname


def generate_random_firstname():
    firstnames = ['Wei', 'Fang', 'Hua', 'Jie', 'Li', 'Ming', 'Qiang', 'Ting', 'Xia', 'Ying', 'Zhi', 'Bo', 'Chao', 'Dan', 'Feng', 'Guo', 'Hao', 'Jian', 'Kun', 'Lei', 'Ning', 'Ping', 'Qiu', 'Rong', 'Shan', 'Tao', 'Wen', 'Xiang', 'Yan', 'Zhen', 'Zhong']
    selected_firstname_A = np.random.choice(firstnames)
    selected_firstname_B = np.random.choice(firstnames)
    return f"{selected_firstname_A}-{selected_firstname_B}"


def generate_students(number_of_students=10):
    clients = []
    for i in range(number_of_students):
        firstname = generate_random_firstname()
        surname = generate_random_surname()
        student_number = f"E{np.random.randint(14100000, 14110000)}"
        client_data = {
            'student_id': student_number,
            'surname': surname,
            'firstname': firstname,
            'emailaddress': generate_email_addresses(student_number)
        }
        clients.append(client_data)
    return clients


def generate_exams(students_df, number_of_exams=10):
    exams = []
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Geography', 'English', 'Computer Science', 'Art', 'Physical Education']
    for i in range(number_of_exams):
        subject = np.random.choice(subjects)
        student_id = np.random.choice(students_df['student_id'])
        exam_data = {
            'student_id': student_id,
            'subject': subject,
            'score': np.random.randint(0, 101)
        }
        exams.append(exam_data)
    return exams


if __name__ == "__main__":
    students = generate_students(100)
    students_df = pd.DataFrame(students)
    students_df.to_csv("students_data.csv", index=False)
    exams = generate_exams(students_df, 200)
    exams_df = pd.DataFrame(exams)
    exams_df.to_csv("exams_data.csv", index=False)

    '''
    Good problems to solve with this data
    1. Analyzing the distribution of scores across different subjects.
    2. Finding students who got the 100 in any subject.
    3. Finding the average score of each student.
    4. Find students who got the same score in the same subject.

    And more!
    
    '''