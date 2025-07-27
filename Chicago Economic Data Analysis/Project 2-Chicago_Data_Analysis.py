import pandas as pd
import sqlite3
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths (relative to project directory)
db_path = os.path.join(BASE_DIR, 'Database.db')
crime_path = os.path.join(BASE_DIR, 'data', 'ChicagoCrimeData.csv')
census_path = os.path.join(BASE_DIR, 'data', 'ChicagoCensusData.csv')
school_path = os.path.join(BASE_DIR, 'data', 'ChicagoPublicSchools.csv')

# Connect to SQLite database
con = sqlite3.connect(db_path)

# Read CSV files into DataFrames
Crime_df = pd.read_csv(crime_path)
Census_df = pd.read_csv(census_path)
School_df = pd.read_csv(school_path)

# Convert DataFrames to SQL tables
Crime_df.to_sql("ChicagoCrimeData", con, if_exists='replace', index=False)
Census_df.to_sql("ChicagoCensusData", con, if_exists='replace', index=False)
School_df.to_sql("ChicagoPublicSchool", con, if_exists='replace', index=False)

# Create a cursor
cursor = con.cursor()

# Problem 1: Total number of crimes
cursor.execute('SELECT COUNT(DISTINCT Case_Number) FROM ChicagoCrimeData')
print(f"Total number of crimes recorded: {cursor.fetchone()[0]}")

# Problem 2: Community areas with per capita income < 11000
cursor.execute('SELECT "COMMUNITY AREA NAME", "COMMUNITY AREA NUMBER" FROM ChicagoCensusData WHERE "PER CAPITA INCOME " < 11000')
print("Community areas with per capita income less than 11000:")
for area in cursor.fetchall():
    print(area)

# Problem 3: Case numbers for crimes involving minors
cursor.execute("SELECT Case_Number FROM ChicagoCrimeData WHERE Description LIKE '%MINOR%'")
print("Case numbers for crimes involving minors:")
for case in cursor.fetchall():
    print(case[0])

# Problem 4: Kidnapping crimes involving a child
cursor.execute("SELECT Case_Number FROM ChicagoCrimeData WHERE Primary_Type = 'KIDNAPPING' AND Description LIKE '%CHILD%'")
print("Case numbers for kidnapping crimes involving a child:")
for case in cursor.fetchall():
    print(case[0])

# Problem 5: Distinct crime types at schools
cursor.execute("SELECT DISTINCT Primary_Type FROM ChicagoCrimeData WHERE Location_Description LIKE '%SCHOOL%'")
print("Kinds of crimes recorded at schools:")
for crime in cursor.fetchall():
    print(crime[0])

# Problem 6: Average safety score by school type
cursor.execute('SELECT "Elementary, Middle, or High School", AVG("SAFETY SCORE") FROM ChicagoPublicSchool GROUP BY "Elementary, Middle, or High School"')
print("Average safety score for each type of school:")
for school in cursor.fetchall():
    print(school)

# Problem 7: Top 5 areas by poverty percentage
cursor.execute('SELECT "COMMUNITY AREA NAME", "PERCENT HOUSEHOLDS BELOW POVERTY" FROM ChicagoCensusData ORDER BY "PERCENT HOUSEHOLDS BELOW POVERTY" DESC LIMIT 5')
print("5 community areas with highest % of households below poverty line:")
for area in cursor.fetchall():
    print(area)

# Problem 8: Community area with highest hardship index
cursor.execute('SELECT "COMMUNITY AREA NAME" FROM ChicagoCensusData ORDER BY "HARDSHIP INDEX" DESC LIMIT 1')
print(f"Community area with highest hardship index: {cursor.fetchone()[0]}")

# Problem 9: School with highest hardship index
cursor.execute('SELECT "NAME OF SCHOOL" FROM ChicagoPublicSchool ORDER BY "HARDSHIP INDEX" DESC LIMIT 1')
print(f"School with highest hardship index: {cursor.fetchone()[0]}")

# Close the connection
con.close()
