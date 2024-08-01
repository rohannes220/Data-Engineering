import pandas as pd
import sqlite3

# Load CSV data and connect to the database
path = "/Users/god/Downloads/oltpdata.csv"

# Load the CSV without headers and then manually add column names
Car_df = pd.read_csv(path, header=None)
Car_df.columns = ['product_id', 'customer_id', 'price', 'quantity', 'timestamp']

# Connect to the SQLite database
con = sqlite3.connect('/Users/god/Desktop/Data Engineering/Database.db')
cursor = con.cursor()

# Create the sales_data table if it doesn't exist
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

# Insert data into sales_data table
Car_df.to_sql("sales_data", con, if_exists='replace', index=False)

# Query 1: List all tables in the database
query1 = "SELECT name FROM sqlite_master WHERE type='table';"
cursor.execute(query1)
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table)

# Query 2: Count the records in the sales_data table
query2 = "SELECT COUNT(*) FROM sales_data"
cursor.execute(query2)
count = cursor.fetchone()
print("Number of records in sales_data:", count[0])

# Query 3: Create an index named 'customer_index' on the 'customer_id' field
query3 = "CREATE INDEX IF NOT EXISTS customer_index ON sales_data(customer_id)"
cursor.execute(query3)
con.commit()

# Query 4: List indexes on the table sales_data
query4 = "PRAGMA index_list('sales_data')"
cursor.execute(query4)
indexes = cursor.fetchall()
print("Indexes on sales_data table:")
for index in indexes:
    print(index)

# Close the connection
con.close()
