"""
Project 3: Brazil Waste Analysis
Author: Rohan Kumar
Description:
    This project analyzes waste collection data in Brazil. 
    It uses dimensional modeling data (Date, Waste, Zone) 
    and a fact table (Trips) to explore patterns in waste collection.

How to run:
    1. Ensure all CSVs are in the 'data' folder.
    2. Run this script with Python 3:
       python Project3_Brazil.py
"""

import pandas as pd
import os

# --- Setup paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# --- Load data ---
def load_csv(filename):
    """Loads a CSV file from the data folder."""
    return pd.read_csv(os.path.join(DATA_DIR, filename))

dim_date = load_csv('MyDimDate.csv')
dim_waste = load_csv('MyDimWaste.csv')
dim_zone = load_csv('MyDimZone.csv')
fact_trips = load_csv('MyFactTrips.csv')

# --- Example Analysis ---
# 1. Merge all data into a single DataFrame
merged_df = fact_trips.merge(dim_date, on='DateID', how='left') \
                      .merge(dim_waste, on='WasteID', how='left') \
                      .merge(dim_zone, on='ZoneID', how='left')

# 2. Show top 5 rows
print("Sample of merged data:")
print(merged_df.head())

# 3. Example: Total waste collected by type
waste_summary = merged_df.groupby('WasteType')['Weight'].sum().reset_index()
print("\nTotal Waste Collected by Type:")
print(waste_summary)

# 4. Example: Trips by Zone
zone_trips = merged_df.groupby('ZoneName')['TripID'].count().reset_index()
zone_trips.rename(columns={'TripID': 'TotalTrips'}, inplace=True)
print("\nTotal Trips by Zone:")
print(zone_trips)

# Save summaries to CSV (optional)
waste_summary.to_csv(os.path.join(BASE_DIR, 'WasteSummary.csv'), index=False)
zone_trips.to_csv(os.path.join(BASE_DIR, 'ZoneTripsSummary.csv'), index=False)

print("\nAnalysis complete. Summaries saved to WasteSummary.csv and ZoneTripsSummary.csv.")
