import numpy as np
import pandas as pd
import uuid
from num2words import num2words


def generate_email_addresses(firstname, surname, chance_of_email=0.95):
    providers = ['example.com', 'mail.com', 'test.org', 'demo.net', 'sample.co', 'myemail.com', 'webmail.org', 'inbox.net', 'emailservice.com', 'fastmail.co']
    selected_provider = np.random.choice(providers)
    email = f"{firstname.lower()}.{surname.lower()}@{selected_provider}"
    if np.random.rand() > chance_of_email:
        email = None
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


# Generate random company name
def generate_random_company_name():
    company_prefixes = ['Tech', 'Info', 'Data', 'Net', 'Global', 'Prime', 'Next', 'Future', 'Vision', 'Dynamic', 'Quantum', 'Pioneer', 'Vertex', 'Nexus', 'Summit', 'Apex', 'Zenith', 'Echelon', 'Vanguard', 'Innovate', 'Synergy', 'Fusion', 'Core', 'Matrix', 'Pulse', 'Strive']
    company_suffixes = ['Solutions', 'Systems', 'Services', 'Technologies', 'Concepts', 'Innovations', 'Enterprises', 'Holdings', 'Ventures', 'Labs', 'Works', 'Dynamics', 'Networks', 'Partners', 'Group', 'Consulting', 'Development', 'Designs', 'Studios', 'Creations', 'Productions', 'Strategies', 'Insights', 'Analytics', 'Resources', 'Management',    'Logistics']
    prefix = np.random.choice(company_prefixes)
    suffix = np.random.choice(company_suffixes)
    return f"{prefix} {suffix}"


def generate_random_filenames(invoices_df, number_of_files=10):
    files = []
    for invoice in range(len(invoices_df)):
        invoice_id = invoices_df.iloc[invoice]['invoice_id']

        for i in range(number_of_files):
            filename_data = {
                'file_id': uuid.uuid4(),
                'invoice_id': invoice_id,
                'filename': f"invoice_{str(uuid.uuid4())[:8]}.pdf"
            }
            files.append(filename_data)
    return files


def generate_clients(number_of_clients=10, chance_of_age_in_words=0.95, chance_of_missing_phone=0.1):
    clients = []
    for i in range(number_of_clients):
        firstname = generate_random_firstname()
        surname = generate_random_surname()
        if np.random.rand() < chance_of_age_in_words:
            age = np.random.randint(18, 70)
        else:
            age = num2words(np.random.randint(18, 70))

        if np.random.rand() < chance_of_missing_phone:
            phonenumber = None
        else:
            phonenumber = f"+886-{910}-{np.random.randint(100,999)}-{np.random.randint(100,999)}"

        client_data = {
            'client_id': uuid.uuid4(),
            'surname': surname,  # 100 samples, 10 features,
            'firstname': firstname,  # 100 samples, 5 features
            'age': age,
            'emailaddress': generate_email_addresses(firstname, surname),
            'phonenumber': phonenumber
        }
        clients.append(client_data)
    return clients


def generate_companies(number_of_companies=10, chance_of_missing_employees=0.1):
    companies = []
    for i in range(number_of_companies):
        company_name = generate_random_company_name()
        if np.random.rand() < chance_of_missing_employees:
            num_employees = None
        else:
            num_employees = np.random.randint(10, 10000)
    
        company_data = {
            'company_id': uuid.uuid4(),
            'company_name': company_name,
            'founded_year': np.random.randint(1950, 2023),
            'num_employees': num_employees
        }
        companies.append(company_data)
    return companies


def generate_invoices(df, company_df, client_ID, chance_of_found_company=0.95):
    invoices = []
    number_of_invoices = np.random.randint(1, 50)
    for i in range(number_of_invoices):
        if np.random.rand() < chance_of_found_company:
            company_id = np.random.choice(company_df['company_id'])
        else:
            company_id = uuid.uuid4()
        invoice_data = {
            'invoice_id': uuid.uuid4(),
            'company_id': company_id,  # 100 samples, 1 feature,
            'amount': np.round(np.random.uniform(50.0, 5000.0), 2),  # 100 samples, 1 feature,
            'due_date': str(pd.Timestamp('2023-01-01') + pd.to_timedelta(np.random.randint(1, 365), unit='d')),
            'is_paid': np.random.choice([True, False]),  # 100 samples, 1 feature,
            'client_id': client_ID
        }
        invoices.append(invoice_data)
    # Append new invoices to the DataFrame
    df_new_rows = pd.DataFrame(invoices)
    # Update dataframe
    if (len(df) == 0):
        df = df_new_rows
    else:
        df = pd.concat([df, df_new_rows], ignore_index=True, copy=True)
    
    return df


if __name__ == "__main__":
    clients = generate_clients(100)
    companies = generate_companies(50)
    clients_df = pd.DataFrame(clients)
    print(f'Number of clients generated: {len(clients_df)}')
    companies_df = pd.DataFrame(companies)
    print(f'Number of clients generated: {len(companies_df)}')

    print(clients_df.head())
    print(companies_df.head())
    
    # Now to generate invoices for each client
    invoices_df = pd.DataFrame()
    for client in clients:
        invoices_df = generate_invoices(invoices_df, companies_df, client['client_id'], 0.95)

    # Now to generate some invoices which are not linked to any client
    # Generate a random client ID 
    for _ in range(int(0.2*len(clients))):
        invoices_df = generate_invoices(invoices_df, companies_df, uuid.uuid4())

    # Shuffle the invoices to make it harder to find the unlinked ones
    invoices_df = invoices_df.sample(frac=1).reset_index(drop=True)
    print(f"Number of invoices generated: {len(invoices_df)}")
    print(invoices_df.head())

    # Generate files for each invoice
    files = generate_random_filenames(invoices_df,  np.random.randint(0, 10))
    files_df = pd.DataFrame(files)
    print(f"Number of files generated: {len(files_df)}")
    print(files_df.head())

    # Save data to CSV files
    clients_df.to_csv('clients.csv', index=False)
    companies_df.to_csv('companies.csv', index=False)
    invoices_df.to_csv('invoices.csv', index=False)
    files_df.to_csv('files.csv', index=False)

    '''
    Good problems to tackle with this dataset
    1. Identifying all clients with the surname "Wang".
    2. Identifying all the clients that use the inbox.net email provider.
    3. Find all clients with a missing phone number AND a missing email address.
    4. Find all the companies that have a client with a missing phone number and email address.
    3. Create a CSV that lists all of the invoices for a chosen company.
    4. Create a CSV that lists of clients with unpaid invoices, and shows the total amount due for each client.
    5. Find the company with the highest number of unpaid invoices.
    6. Find the average invoice amount for each company. Create a CSV that shows this.
    7. Find the top 5 clients with the highest total invoice amounts for a given company.
    8. Compute the average amount made per invoice per employee in the company - find the most efficient company.
    9. Find all the invoices that don't have an associated file.

    '''
    # Good problems to tackle with this dataset
