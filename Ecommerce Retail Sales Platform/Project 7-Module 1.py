import pandas as pd
import sqlite3
import os

# --- Setup relative paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'oltpdata.csv')
DB_PATH = os.path.join(BASE_DIR, 'Database.db')

# --- Load CSV without headers and assign column names ---
Car_df = pd.read_csv(CSV_PATH, header=None)
Car_df.columns = ['product_id', 'customer_id', 'price', 'quantity', 'timestamp']

# --- Connect to SQLite database ---
con = sqlite3.connect(DB_PATH)
cursor = con.cursor()

# --- Create the sales_data table ---
create_table_query = '''
CREATE TABLE IF NOT EXISTS sales_data (
    product_id INTEGER,
    customer_id INTEGER,
    price INTEGER,
    quantity INTEGER,
    timestamp TEXT
)
'''
cursor.execute(create_table_query)

# --- Insert data into sales_data table ---
Car_df.to_sql("sales_data", con, if_exists='replace', index=False)

# --- Query 1: List all tables ---
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables in the database:")
for table in cursor.fetchall():
    print(table[0])

# --- Query 2: Count records in sales_data ---
cursor.execute("SELECT COUNT(*) FROM sales_data")
print("Number of records in sales_data:", cursor.fetchone()[0])

# --- Query 3: Create an index on customer_id ---
cursor.execute("CREATE INDEX IF NOT EXISTS customer_index ON sales_data(customer_id)")
con.commit()

# --- Query 4: List indexes on sales_data ---
cursor.execute("PRAGMA index_list('sales_data')")
print("Indexes on sales_data table:")
for index in cursor.fetchall():
    print(index)

# --- Close the connection ---
con.close()
