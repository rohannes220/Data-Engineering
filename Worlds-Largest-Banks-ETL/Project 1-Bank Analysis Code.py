import requests
import pandas as pd
from bs4 import BeautifulSoup
import sqlite3
import logging

# Task 1: Logging function
def log_progress(message):
    logging.basicConfig(filename='code_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info(message)

# Task 2: Extraction of data
def extract():
    log_progress('Starting data extraction')
    url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'wikitable'})

    rows = table.find_all('tr')[1:]  # Skip the header row
    data = []
    for row in rows:
        cols = row.find_all('td')
        name = cols[1].text.strip()
        mc_usd = float(cols[2].text.strip().replace(',', ''))
        data.append([name, mc_usd])
    
    df = pd.DataFrame(data, columns=['Name', 'MC_USD_Billion'])
    log_progress('Data extraction completed')
    return df

# Task 3: Transformation of data
def transform(df, exchange_rates):
    log_progress('Starting data transformation')
    rates = pd.read_csv(exchange_rates)
    usd_to_gbp = rates.loc[rates['Currency'] == 'GBP', 'Rate'].values[0]
    usd_to_eur = rates.loc[rates['Currency'] == 'EUR', 'Rate'].values[0]
    usd_to_inr = rates.loc[rates['Currency'] == 'INR', 'Rate'].values[0]

    df['MC_GBP_Billion'] = (df['MC_USD_Billion'] * usd_to_gbp).round(2)
    df['MC_EUR_Billion'] = (df['MC_USD_Billion'] * usd_to_eur).round(2)
    df['MC_INR_Billion'] = (df['MC_USD_Billion'] * usd_to_inr).round(2)
    log_progress('Data transformation completed')
    return df

# Task 4: Loading to CSV
def load_to_csv(df, path):
    log_progress('Starting CSV load')
    df.to_csv(path, index=False)
    log_progress('CSV load completed')

# Task 5: Loading to Database
def load_to_db(df, db_name, table_name):
    log_progress('Starting database load')
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    log_progress('Database load completed')

# Task 6: Function to Run queries on Database
def run_query(db_name, query):
    log_progress('Starting database query')
    conn = sqlite3.connect(db_name)
    result = pd.read_sql_query(query, conn)
    conn.close()
    log_progress('Database query completed')
    return result

# Task 7: Verify log entries
def verify_log():
    with open('code_log.txt', 'r') as f:
        log_entries = f.readlines()
    return log_entries

if __name__ == "__main__":
    log_progress('Project started')
    
    # Extract data
    banks_df = extract()
    
    # Transform data
    exchange_rate_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
    transformed_df = transform(banks_df, exchange_rate_path)
    
    # Load to CSV
    output_csv_path = './Largest_banks_data.csv'
    load_to_csv(transformed_df, output_csv_path)
    
    # Load to Database
    db_name = 'Banks.db'
    table_name = 'Largest_banks'
    load_to_db(transformed_df, db_name, table_name)
    
    # Run a sample query
    query = 'SELECT * FROM Largest_banks'
    query_result = run_query(db_name, query)
    print(query_result)
    
    # Verify log entries
    log_entries = verify_log()
    for entry in log_entries:
        print(entry.strip())
    
    log_progress('Project completed')
