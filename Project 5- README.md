
# Employee Data Analysis with PySpark

This project involves analyzing employee data using PySpark. It reads data from a CSV file, processes it into a DataFrame, and performs various data manipulations and analyses using Spark SQL.

## Data Files

The project uses the following CSV file:
- `employees.csv`: Contains employee data including EmployeeID, Name, Department, Salary, JoiningDate, and Age.

## Prerequisites

Ensure you have Python 3.x installed along with Apache Spark and the necessary libraries:
- `pyspark` for Spark session and DataFrame operations

Install PySpark using pip:
```sh
pip install pyspark
```

## Project Structure

- **employee_data_analysis.py**: The main script to read data from `employees.csv`, process it using PySpark, and perform various SQL queries and transformations.
- **employees.csv**: CSV file containing employee data.

## Usage

1. **Set the File Path**

   Ensure the file path for `employees.csv` is correctly set in the script:
   ```python
   csv_file_path = "/path/to/employees.csv"
   ```

2. **Run the Script**

   Execute the Python script `employee_data_analysis.py` to perform data analysis tasks:
   ```sh
   python employee_data_analysis.py
   ```

3. **View the Output**

   The script will print the results of the queries and transformations to the console.

## Tasks Performed

1. **Read Data from CSV**

   Reads employee data from `employees.csv` into a PySpark DataFrame (`employees_df`).

2. **Display Schema**

   Displays the schema of the `employees_df` DataFrame to understand its structure.

3. **Create Temporary View**

   Creates a temporary SQL view (`employees`) for running SQL queries against the DataFrame.

4. **Execute SQL Queries**

   Executes SQL queries to analyze the employee data:
   - Calculate Average Salary by Department
   - Filter and Display IT Department Employees
   - Add 10% Bonus to Salaries
   - Find Maximum Salary by Age
   - Perform Self-Join on Employee Data
   - Calculate Average Employee Age
   - Calculate Total Salary by Department

5. **Closing Remarks**

   Ensure all file paths and configurations within `employee_data_analysis.py` are adjusted according to your local setup and file locations.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
