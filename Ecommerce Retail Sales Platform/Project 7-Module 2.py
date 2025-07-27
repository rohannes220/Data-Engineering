import pandas as pd
import sqlite3
import os

# --- Setup relative paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
DB_PATH = os.path.join(BASE_DIR, 'Database.db')

# --- Connect to SQLite database ---
con = sqlite3.connect(DB_PATH)
cursor = con.cursor()

# --- Task 1: Load DimDate ---
dimdate_path = os.path.join(DATA_DIR, "DimDate.csv")
DimDate_df = pd.read_csv(dimdate_path)
cursor.execute('''
CREATE TABLE IF NOT EXISTS DimDate (
    DateKey INTEGER PRIMARY KEY,
    Date TEXT,
    Day INTEGER,
    Month INTEGER,
    Year INTEGER,
    Quarter INTEGER
)
''')
DimDate_df.to_sql("DimDate", con, if_exists='replace', index=False)
cursor.execute("SELECT * FROM DimDate LIMIT 5")
print("First 5 rows in DimDate:", cursor.fetchall())

# --- Task 2: Load DimCategory ---
dimcategory_path = os.path.join(DATA_DIR, "DimCategory.csv")
DimCategory_df = pd.read_csv(dimcategory_path)
cursor.execute('''
CREATE TABLE IF NOT EXISTS DimCategory (
    CategoryKey INTEGER PRIMARY KEY,
    CategoryName TEXT
)
''')
DimCategory_df.to_sql("DimCategory", con, if_exists='replace', index=False)
cursor.execute("SELECT * FROM DimCategory LIMIT 5")
print("First 5 rows in DimCategory:", cursor.fetchall())

# --- Task 3: Load DimCountry ---
dimcountry_path = os.path.join(DATA_DIR, "DimCountry.csv")
DimCountry_df = pd.read_csv(dimcountry_path)
cursor.execute('''
CREATE TABLE IF NOT EXISTS DimCountry (
    CountryKey INTEGER PRIMARY KEY,
    CountryName TEXT
)
''')
DimCountry_df.to_sql("DimCountry", con, if_exists='replace', index=False)
cursor.execute("SELECT * FROM DimCountry LIMIT 5")
print("First 5 rows in DimCountry:", cursor.fetchall())

# --- Task 4: Load FactSales ---
factsales_path = os.path.join(DATA_DIR, "FactSales.csv")
FactSales_df = pd.read_csv(factsales_path)
cursor.execute('''
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
''')
FactSales_df.to_sql("FactSales", con, if_exists='replace', index=False)
cursor.execute("SELECT * FROM FactSales LIMIT 5")
print("First 5 rows in FactSales:", cursor.fetchall())

# --- Task 5: Grouping Sets ---
cursor.execute('''
SELECT CountryName, CategoryName, SUM(SalesAmount) AS TotalSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
JOIN DimCategory ON FactSales.ProductKey = DimCategory.CategoryKey
GROUP BY GROUPING SETS ((CountryName), (CategoryName), (CountryName, CategoryName))
''')
print("Grouping Sets Query Result:", cursor.fetchall())

# --- Task 6: Rollup ---
cursor.execute('''
SELECT Year, CountryName, SUM(SalesAmount) AS TotalSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
JOIN DimDate ON FactSales.DateKey = DimDate.DateKey
GROUP BY ROLLUP (Year, CountryName)
''')
print("Rollup Query Result:", cursor.fetchall())

# --- Task 7: Cube ---
cursor.execute('''
SELECT Year, CountryName, AVG(SalesAmount) AS AverageSales
FROM FactSales
JOIN DimCountry ON FactSales.CustomerKey = DimCountry.CountryKey
JOIN DimDate ON FactSales.Date

