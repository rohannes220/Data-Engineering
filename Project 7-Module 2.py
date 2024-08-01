import pandas as pd
import sqlite3

# Connect to the database
con = sqlite3.connect('/Users/god/Desktop/Data Engineering/Database.db')
cursor = con.cursor()

# Task 1: Load data into the DimDate table
dimdate_path = "/Users/god/Downloads/DimDate.csv"
DimDate_df = pd.read_csv(dimdate_path)

# Create the DimDate table if it doesn't exist
create_dimdate_query = '''
CREATE TABLE IF NOT EXISTS DimDate (
    DateKey INTEGER PRIMARY KEY,
    Date TEXT,
    Day INTEGER,
    Month INTEGER,
    Year INTEGER,
    Quarter INTEGER
)
'''
cursor.execute(create_dimdate_query)

# Insert data into DimDate table
DimDate_df.to_sql("DimDate", con, if_exists='replace', index=False)

# Query: Retrieve first 5 rows from DimDate
query = "SELECT * FROM DimDate LIMIT 5"
cursor.execute(query)
dimdate_rows = cursor.fetchall()
print("First 5 rows in DimDate:")
for row in dimdate_rows:
    print(row)

# Task 2: Load data into the DimCategory table
dimcategory_path = "/Users/god/Downloads/DimCategory.csv"
DimCategory_df = pd.read_csv(dimcategory_path)

# Create the DimCategory table if it doesn't exist
create_dimcategory_query = '''
CREATE TABLE IF NOT EXISTS DimCategory (
    CategoryKey INTEGER PRIMARY KEY,
    CategoryName TEXT
)
'''
cursor.execute(create_dimcategory_query)

# Insert data into DimCategory table
DimCategory_df.to_sql("DimCategory", con, if_exists='replace', index=False)

# Query: Retrieve first 5 rows from DimCategory
query = "SELECT * FROM DimCategory LIMIT 5"
cursor.execute(query)
dimcategory_rows = cursor.fetchall()
print("First 5 rows in DimCategory:")
for row in dimcategory_rows:
    print(row)

# Task 3: Load data into the DimCountry table
dimcountry_path = "/Users/god/Downloads/DimCountry.csv"
DimCountry_df = pd.read_csv(dimcountry_path)

# Create the DimCountry table if it doesn't exist
create_dimcountry_query = '''
CREATE TABLE IF NOT EXISTS DimCountry (
    CountryKey INTEGER PRIMARY KEY,
    CountryName TEXT
)
'''
cursor.execute(create_dimcountry_query)

# Insert data into DimCountry table
DimCountry_df.to_sql("DimCountry", con, if_exists='replace', index=False)

# Query: Retrieve first 5 rows from DimCountry
query = "SELECT * FROM DimCountry LIMIT 5"
cursor.execute(query)
dimcountry_rows = cursor.fetchall()
print("First 5 rows in DimCountry:")
for row in dimcountry_rows:
    print(row)

# Task 4: Load data into the FactSales table
factsales_path = "/Users/god/Downloads/FactSales.csv"
FactSales_df = pd.read_csv(factsales_path)

# Create the FactSales table if it doesn't exist
create_factsales_query = '''
CREATE TABLE IF NOT EXISTS FactSales (
    SalesKey INTEGER PRIMARY KEY,
    DateKey INTEGER,
    ProductKey INTEGER,
    CustomerKey INTEGER,
    StoreKey INTEGER,
    PromotionKey INTEGER,
    CurrencyKey INTEGER,
    SalesTerritoryKey INTEGER,
    SalesOrderNumber TEXT,
    SalesOrderLineNumber INTEGER,
    Quantity INTEGER,
    UnitPrice REAL,
    ExtendedAmount REAL,
    UnitCost REAL,
    GrossProfit REAL,
    SalesAmount REAL,
    TaxAmt REAL,
    Freight REAL,
    TotalDue REAL,
    OrderDate TEXT,
    DueDate TEXT,
    ShipDate TEXT,
    FOREIGN KEY (DateKey) REFERENCES DimDate(DateKey),
    FOREIGN KEY (CustomerKey) REFERENCES DimCountry(CountryKey)
)
'''
cursor.execute(create_factsales_query)

# Insert data into FactSales table
FactSales_df.to_sql("FactSales", con, if_exists='replace', index=False)

# Query: Retrieve first 5 rows from FactSales
query = "SELECT * FROM FactSales LIMIT 5"
cursor.execute(query)
factsales_rows = cursor.fetchall()
print("First 5 rows in FactSales:")
for row in factsales_rows:
    print(row)

# Task 5: Create a grouping sets query
grouping_sets_query = '''
SELECT CountryName, CategoryName, SUM(SalesAmount) AS TotalSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
JOIN DimCategory ON FactSales.ProductKey = DimCategory.CategoryKey
GROUP BY GROUPING SETS ((CountryName), (CategoryName), (CountryName, CategoryName))
'''
cursor.execute(grouping_sets_query)
groupingsets_rows = cursor.fetchall()
print("Grouping Sets Query Result:")
for row in groupingsets_rows:
    print(row)

# Task 6: Create a rollup query
rollup_query = '''
SELECT Year, CountryName, SUM(SalesAmount) AS TotalSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
JOIN DimDate ON FactSales.DateKey = DimDate.DateKey
GROUP BY ROLLUP (Year, CountryName)
'''
cursor.execute(rollup_query)
rollup_rows = cursor.fetchall()
print("Rollup Query Result:")
for row in rollup_rows:
    print(row)

# Task 7: Create a cube query
cube_query = '''
SELECT Year, CountryName, AVG(SalesAmount) AS AverageSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
JOIN DimDate ON FactSales.DateKey = DimDate.DateKey
GROUP BY CUBE (Year, CountryName)
'''
cursor.execute(cube_query)
cube_rows = cursor.fetchall()
print("Cube Query Result:")
for row in cube_rows:
    print(row)

# Task 8: Create an MQT
create_mqt_query = '''
CREATE TABLE IF NOT EXISTS total_sales_per_country AS
SELECT CountryName, SUM(SalesAmount) AS TotalSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
GROUP BY CountryName
'''
cursor.execute(create_mqt_query)
con.commit()

# Query: Retrieve data from total_sales_per_country
query = "SELECT * FROM total_sales_per_country"
cursor.execute(query)
mqt_rows = cursor.fetchall()
print("Total Sales Per Country MQT:")
for row in mqt_rows:
    print(row)

# Close the connection
con.close()
