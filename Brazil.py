import sqlite3
import pandas as pd

# Read data from CSV files
mydimdate_df = pd.read_csv('/Users/god/Downloads/MyDimDate.csv')
mydimwaste_df = pd.read_csv('/Users/god/Downloads/MyDimWaste.csv')
mydimzone_df = pd.read_csv('/Users/god/Downloads/MyDimZone.csv')
myfacttrips_df = pd.read_csv('/Users/god/Downloads/MyFactTrips.csv')

# Connect to SQLite database
conn = sqlite3.connect('data_warehouse.db')
cursor = conn.cursor()

# Drop tables if they exist to avoid conflicts with existing data
cursor.execute('DROP TABLE IF EXISTS MyDimDate')
cursor.execute('DROP TABLE IF EXISTS MyDimWaste')
cursor.execute('DROP TABLE IF EXISTS MyDimZone')
cursor.execute('DROP TABLE IF EXISTS MyFactTrips')

# Task 1: Design the dimension table MyDimDate
cursor.execute('''
CREATE TABLE MyDimDate (
    DateKey INT PRIMARY KEY,
    Date TEXT NOT NULL,
    Year INT,
    Month INT,
    Quarter INT
)
''')

# Task 2: Design the dimension table MyDimWaste
cursor.execute('''
CREATE TABLE MyDimWaste (
    WasteTypeKey INT PRIMARY KEY,
    WasteType TEXT NOT NULL
)
''')

# Task 3: Design the dimension table MyDimZone
cursor.execute('''
CREATE TABLE MyDimZone (
    ZoneKey INT PRIMARY KEY,
    City TEXT,
    Station TEXT
)
''')

# Task 4: Design the fact table MyFactTrips
cursor.execute('''
CREATE TABLE MyFactTrips (
    TripID INT PRIMARY KEY,
    DateKey INT,
    WasteTypeKey INT,
    ZoneKey INT,
    TruckType TEXT,
    Weight REAL,
    FOREIGN KEY (DateKey) REFERENCES MyDimDate(DateKey),
    FOREIGN KEY (WasteTypeKey) REFERENCES MyDimWaste(WasteTypeKey),
    FOREIGN KEY (ZoneKey) REFERENCES MyDimZone(ZoneKey)
)
''')

# Insert data into MyDimDate
mydimdate_df.to_sql('MyDimDate', conn, if_exists='append', index=False)

# Insert data into MyDimWaste
mydimwaste_df.to_sql('MyDimWaste', conn, if_exists='append', index=False)

# Insert data into MyDimZone
mydimzone_df.to_sql('MyDimZone', conn, if_exists='append', index=False)

# Insert data into MyFactTrips
myfacttrips_df.to_sql('MyFactTrips', conn, if_exists='append', index=False)

# Task 13: Query to get total weight collected per year
query_13 = '''
SELECT Year, SUM(Weight) AS TotalWeight
FROM MyFactTrips
JOIN MyDimDate ON MyFactTrips.DateKey = MyDimDate.DateKey
GROUP BY Year;
'''
result_13 = pd.read_sql_query(query_13, conn)
print("Total Weight Collected per Year:")
print(result_13)

# Task 14: Simple query to get total weight collected per year and month
query_14 = '''
SELECT Year, Month, SUM(Weight) AS TotalWeight
FROM MyFactTrips
JOIN MyDimDate ON MyFactTrips.DateKey = MyDimDate.DateKey
GROUP BY Year, Month;
'''
result_14 = pd.read_sql_query(query_14, conn)
print("Total Weight Collected per Year and Month:")
print(result_14)

# Task 15: Simple query to get average weight collected per city
query_15 = '''
SELECT City, AVG(Weight) AS AvgWeight
FROM MyFactTrips
JOIN MyDimZone ON MyFactTrips.ZoneKey = MyDimZone.ZoneKey
GROUP BY City;
'''
result_15 = pd.read_sql_query(query_15, conn)
print("Average Weight Collected per City:")
print(result_15)

# Task 16: Create a materialized view using CREATE VIEW
cursor.execute('''
CREATE VIEW max_waste_per_station AS
SELECT 
    City, 
    Station, 
    TruckType, 
    MAX(Weight) AS MaxWeight
FROM 
    MyFactTrips
    JOIN MyDimZone ON MyFactTrips.ZoneKey = MyDimZone.ZoneKey
GROUP BY 
    City, Station, TruckType
''')
materialized_view_result = pd.read_sql_query('SELECT * FROM max_waste_per_station', conn)
print("Materialized View Result:")
print(materialized_view_result)

# Commit changes and close connection
conn.commit()
conn.close()
