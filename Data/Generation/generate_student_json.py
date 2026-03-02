import numpy as np
import json

def generate_random_surname():
    surnames = ['Lee', 'Chang', 'Chen', 'Wang', 'Zhang', 'Liu', 'Huang', 'Lin', 'Wu', 'Zhao', 'Yang', 'Xu', 'Sun', 'He', 'Gao', 'Deng', 'Cao', 'Feng', 'Jiang', 'Tang', 'Shi', 'Qian', 'Yuan', 'Xie', 'Zhou', 'Guo', 'Ma', 'Liang', 'Pan', 'Ding', 'Ren']
    selected_surname = np.random.choice(surnames)
    return selected_surname

def generate_random_subject():
    subjects = ['Mathematics', 'Social Studies','Kinematics','Solidworks','Art','English']
    selected_subject = np.random.choice(subjects)
    return selected_subject


def generate_random_firstname():
    firstnames = ['Wei', 'Fang', 'Hua', 'Jie', 'Li', 'Ming', 'Qiang', 'Ting', 'Xia', 'Ying', 'Zhi', 'Bo', 'Chao', 'Dan', 'Feng', 'Guo', 'Hao', 'Jian', 'Kun', 'Lei', 'Ning', 'Ping', 'Qiu', 'Rong', 'Shan', 'Tao', 'Wen', 'Xiang', 'Yan', 'Zhen', 'Zhong']
    selected_firstname_A = np.random.choice(firstnames)
    selected_firstname_B = np.random.choice(firstnames)
    return f"{selected_firstname_A}-{selected_firstname_B}"


def generate_students(number_of_students=10):
    clients = []
    for i in range(number_of_students):
        id = i
        firstname = generate_random_firstname()
        surname = generate_random_surname()
        name = f"{firstname} {surname}"
        age = np.random.randint(19, 25)
        major = "Meow Meow"
        scores = []
        #Ｅach student has 3 subjects
        for j in range(3):
                subject = generate_random_subject()
                scores.append(f"{subject}: {np.random.randint(60, 100)}")

        client_data = {
	    'id': id,
            'name': name,
            'age': age,
            'major': major,
            'scores': scores
        }
        clients.append(client_data)
    return clients


if __name__ == "__main__":
    students = generate_students(5000)
    for student in students:
        print(student)

    #Dump to file
    with open('large_students.json','w') as json_file:
        json.dump(students,json_file,indent=4)

