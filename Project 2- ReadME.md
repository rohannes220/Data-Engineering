# Chicago Data Analysis with SQLite

This project involves analyzing crime, census, and public school data for Chicago. It reads data from CSV files, loads it into an SQLite database, and performs various SQL queries to extract meaningful insights.

## Data Files

The project uses the following CSV files:
- `ChicagoCrimeData.csv`: Contains data about crimes in Chicago.
- `ChicagoCensusData.csv`: Contains census data for Chicago community areas.
- `ChicagoPublicSchools.csv`: Contains information about public schools in Chicago.

## Prerequisites

- Python 3.x
- pandas library
- sqlite3 library

To install the required libraries, you can use pip:
```sh
pip install pandas
```

## Project Structure

- **main.py**: The main script to read data from CSV files, load it into an SQLite database, and perform various queries.
- **ChicagoCrimeData.csv**: Crime data in Chicago.
- **ChicagoCensusData.csv**: Census data for Chicago community areas.
- **ChicagoPublicSchools.csv**: Public schools information in Chicago.

## Usage

1. **Set the File Paths**

   Ensure the file paths for the CSV files are correctly set in the script:
   ```python
   Crime_File_Path = "/path/to/ChicagoCrimeData.csv"
   Census_File_Path = "/path/to/ChicagoCensusData.csv"
   School_File_Path = "/path/to/ChicagoPublicSchools.csv"
   ```

2. **Execute the Script**

   Run the script using Python:
   ```sh
   python main.py
   ```

3. **View the Output**

   The script will print the results of the queries to the console.

## Queries Performed

1. **Total Number of Crimes**
   - Finds the total number of crimes recorded in the `ChicagoCrimeData` table.

2. **Community Areas with Low Income**
   - Lists community area names and numbers with per capita income less than 11000.

3. **Crimes Involving Minors**
   - Lists all case numbers for crimes involving minors.

4. **Kidnapping Crimes Involving a Child**
   - Lists all kidnapping crimes involving a child.

5. **Crimes Recorded at Schools**
   - Lists the kinds of crimes that were recorded at schools (no repetitions).

6. **Average Safety Score by School Type**
   - Lists the type of schools along with the average safety score for each type.

7. **Community Areas with Highest Poverty**
   - Lists 5 community areas with the highest percentage of households below the poverty line.

8. **Community Area with Highest Hardship Index**
   - Finds the name of the community area with the highest hardship index.

9. **School with Highest Hardship Index**
   - Finds the school with the highest hardship index.

## Example Output

```sh
Total number of crimes recorded: 533
Community areas with per capita income less than 11000:
('Area 1', 1)
('Area 2', 2)
...
Case numbers for crimes involving minors:
HZ123456
HZ123457
...
Case numbers for kidnapping crimes involving a child:
HZ123456
HZ123457
...
Kinds of crimes recorded at schools:
BATTERY
CRIMINAL DAMAGE
...
Average safety score for each type of school:
('ES', 48.5)
('HS', 42.3)
...
5 community areas with highest % of households below poverty line:
('Area 1', 56.0)
('Area 2', 52.0)
...
Community area with highest hardship index: 'Area X'
School with highest hardship index: 'School Y'
```

## Closing the Connection

The script closes the SQLite database connection at the end of the execution.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- The data used in this project is publicly available from the City of Chicago's data portal.
