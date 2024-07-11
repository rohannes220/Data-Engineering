import pandas as pd
import sqlite3

# Create file paths and connect to SQLite database
con = sqlite3.connect('/Users/god/Desktop/Data Engineering/Database.db')

# File paths
Crime_File_Path = "/Users/god/Downloads/ChicagoCrimeData.csv"
Census_File_Path = "/Users/god/Downloads/ChicagoCensusData.csv"
School_File_Path = "/Users/god/Downloads/ChicagoPublicSchools.csv"

# Read CSV files into DataFrames
Crime_df = pd.read_csv(Crime_File_Path)
Census_df = pd.read_csv(Census_File_Path)
School_df = pd.read_csv(School_File_Path)

# Convert DataFrames to SQL tables
Crime_df.to_sql("ChicagoCrimeData", con, if_exists='replace', index=False)
Census_df.to_sql("ChicagoCensusData", con, if_exists='replace', index=False)
School_df.to_sql("ChicagoPublicSchool", con, if_exists='replace', index=False)

# Create a cursor object
cursor = con.cursor()

# Verify column names in each table
cursor.execute("PRAGMA table_info(ChicagoCensusData)")
census_columns = cursor.fetchall()
print("Census Table Columns:", [col[1] for col in census_columns])

cursor.execute("PRAGMA table_info(ChicagoCrimeData)")
crime_columns = cursor.fetchall()
print("Crime Table Columns:", [col[1] for col in crime_columns])

cursor.execute("PRAGMA table_info(ChicagoPublicSchool)")
school_columns = cursor.fetchall()
print("School Table Columns:", [col[1] for col in school_columns])

# Problem 1
# Find the total number of crimes recorded in the CRIME table.
query1 = 'SELECT COUNT(DISTINCT Case_Number) FROM ChicagoCrimeData'
cursor.execute(query1)
total_crimes = cursor.fetchone()[0]
print(f"Total number of crimes recorded: {total_crimes}")

# Problem 2
# List community area names and numbers with per capita income less than 11000.
query2 = 'SELECT "COMMUNITY AREA NAME", "COMMUNITY AREA NUMBER" FROM ChicagoCensusData WHERE "PER CAPITA INCOME " < 11000'
cursor.execute(query2)
low_income_areas = cursor.fetchall()
print("Community areas with per capita income less than 11000:")
for area in low_income_areas:
    print(area)

# Problem 3
# List all case numbers for crimes involving minors?
query3 = "SELECT Case_Number FROM ChicagoCrimeData WHERE Description LIKE '%MINOR%'"
cursor.execute(query3)
crimes_involving_minors = cursor.fetchall()
print("Case numbers for crimes involving minors:")
for case in crimes_involving_minors:
    print(case[0])

# Problem 4
# List all kidnapping crimes involving a child?
query4 = "SELECT Case_Number FROM ChicagoCrimeData WHERE Primary_Type = 'KIDNAPPING' AND Description LIKE '%CHILD%'"
cursor.execute(query4)
kidnapping_crimes = cursor.fetchall()
print("Case numbers for kidnapping crimes involving a child:")
for case in kidnapping_crimes:
    print(case[0])

# Problem 5
# List the kind of crimes that were recorded at schools. (No repetitions)
query5 = "SELECT DISTINCT Primary_Type FROM ChicagoCrimeData WHERE Location_Description LIKE '%SCHOOL%'"
cursor.execute(query5)
school_crimes = cursor.fetchall()
print("Kinds of crimes recorded at schools:")
for crime in school_crimes:
    print(crime[0])

# Problem 6
# List the type of schools along with the average safety score for each type.
query6 = 'SELECT "Elementary, Middle, or High School", AVG("SAFETY SCORE") FROM ChicagoPublicSchool GROUP BY "Elementary, Middle, or High School"'
cursor.execute(query6)
school_safety_scores = cursor.fetchall()
print("Average safety score for each type of school:")
for school in school_safety_scores:
    print(school)

# Problem 7
# List 5 community areas with highest % of households below poverty line.
query7 = 'SELECT "COMMUNITY AREA NAME", "PERCENT HOUSEHOLDS BELOW POVERTY" FROM ChicagoCensusData ORDER BY "PERCENT HOUSEHOLDS BELOW POVERTY" DESC LIMIT 5'
cursor.execute(query7)
poverty_areas = cursor.fetchall()
print("5 community areas with highest % of households below poverty line:")
for area in poverty_areas:
    print(area)

# Problem 8
# Find the name of the community area with highest hardship index.
query8 = 'SELECT "COMMUNITY AREA NAME" FROM ChicagoCensusData ORDER BY "HARDSHIP INDEX" DESC LIMIT 1'
cursor.execute(query8)
highest_hardship_area = cursor.fetchone()[0]
print(f"Community area with highest hardship index: {highest_hardship_area}")

# Problem 9
# Find the school with highest hardship index.
query9 = 'SELECT "NAME OF SCHOOL" FROM ChicagoPublicSchool ORDER BY "HARDSHIP INDEX" DESC LIMIT 1'
cursor.execute(query9)
highest_hardship_school = cursor.fetchone()[0]
print(f"School with highest hardship index: {highest_hardship_school}")

# Close the connection
con.close()
