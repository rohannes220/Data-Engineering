
## Project Overview
This project involves designing and implementing a data warehouse for a solid waste management company in Brazil. The data warehouse will enable the company to generate various reports, such as total waste collected per year and average weight collected per city.

## Files
- **MyDimDate.csv**: Contains date-related information.
- **MyDimWaste.csv**: Contains waste type information.
- **MyDimZone.csv**: Contains information about the collection zones.
- **MyFactTrips.csv**: Contains information about the waste collection trips.

## Script: Brazil.py
The script performs the following tasks:
1. Reads data from the CSV files.
2. Creates and populates the dimension and fact tables.
3. Executes queries to generate reports.

## Queries
### Total Weight Collected per Year
Calculates the total weight of waste collected per year.

```sql
SELECT Year, SUM(Weight) AS TotalWeight
FROM MyFactTrips
JOIN MyDimDate ON MyFactTrips.DateKey = MyDimDate.DateKey
GROUP BY Year;
```

### Total Weight Collected per Year and Month
Calculates the total weight of waste collected per year and month.

```sql
SELECT Year, Month, SUM(Weight) AS TotalWeight
FROM MyFactTrips
JOIN MyDimDate ON MyFactTrips.DateKey = MyDimDate.DateKey
GROUP BY Year, Month;
```

### Average Weight Collected per City
Calculates the average weight of waste collected per city.

```sql
SELECT City, AVG(Weight) AS AvgWeight
FROM MyFactTrips
JOIN MyDimZone ON MyFactTrips.ZoneKey = MyDimZone.ZoneKey
GROUP BY City;
```

### Materialized View for Max Weight per Station
Creates a view that stores the maximum weight collected per station for each city and truck type.

```sql
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
    City, Station, TruckType;
```

## How to Run the Script
1. Ensure that the CSV files (`MyDimDate.csv`, `MyDimWaste.csv`, `MyDimZone.csv`, `MyFactTrips.csv`) are available in the specified directory (`/Users/god/Downloads/`).
2. Run the Python script `Brazil.py` to create the tables, load the data, and execute the queries.

```bash
python Brazil.py
```

## Example Output
### Total Weight Collected per Year
| Year | TotalWeight |
|------|-------------|
| 2024 | 4501.25     |

### Total Weight Collected per Year and Month
| Year | Month | TotalWeight |
|------|-------|-------------|
| 2024 | 1     | 1000.50     |
| 2024 | 2     | 2000.75     |
| 2024 | 3     | 1500.00     |

### Average Weight Collected per City
| City           | AvgWeight |
|----------------|-----------|
| Brasilia       | 1500.00   |
| Rio de Janeiro | 2000.75   |
| Sao Paulo      | 1000.50   |

### Materialized View Result
| City           | Station   | TruckType | MaxWeight |
|----------------|-----------|-----------|-----------|
| Brasilia       | Station C | Truck C   | 1500.00   |
| Rio de Janeiro | Station B | Truck B   | 2000.75   |
| Sao Paulo      | Station A | Truck A   | 1000.50   |

## Conclusion
This project demonstrates the fundamental steps in designing and implementing a data warehouse, including schema design, data loading, and query formulation. The provided SQL scripts and instructions should help in setting up and completing the final assignment.
```
