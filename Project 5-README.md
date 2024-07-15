Employee Data Processing with Apache Spark
Introduction
This project demonstrates various data processing tasks using Apache Spark. The tasks include reading data from a CSV file, defining a schema, performing SQL operations, filtering data, adding new columns, and performing self-joins on a Spark DataFrame. The goal is to master Spark SQL, a powerful component of Apache Spark that allows you to work with structured data using SQL-like queries.

Scenario
You have been tasked by the HR department of a company to create a data pipeline that can take in employee data in a CSV format. Your responsibilities include analyzing the data, applying any required transformations, and facilitating the extraction of valuable insights from the processed data.

Project Overview
Create a DataFrame by loading data from a CSV file and apply transformations and actions using Spark SQL. The project involves performing the following tasks:

Task 1: Generate DataFrame from CSV data.
Task 2: Define a schema for the data.
Task 3: Display schema of DataFrame.
Task 4: Create a temporary view.
Task 5: Execute an SQL query.
Task 6: Calculate Average Salary by Department.
Task 7: Filter and Display IT Department Employees.
Task 8: Add 10% Bonus to Salaries.
Task 9: Find Maximum Salary by Age.
Task 10: Self-Join on Employee Data.
Task 11: Calculate Average Employee Age.
Task 12: Calculate Total Salary by Department.
Task 13: Sort Data by Age and Salary.
Task 14: Count Employees in Each Department.
Task 15: Filter Employees with the letter 'o' in the Name.
Instructions
Task 1: Generate DataFrame from CSV data.

Download the CSV file: employees.csv
Read the CSV file into a DataFrame.
Task 2: Define a schema for the data.

Define a schema and read the CSV file using this schema.
Task 3: Display schema of DataFrame.

Display the schema of the DataFrame.
Task 4: Create a temporary view.

Create a temporary view from the DataFrame.
Task 5: Execute an SQL query.

Execute an SQL query to retrieve data from the temporary view.
Task 6: Calculate Average Salary by Department.

Write an SQL query to calculate the average salary by department and display the result.
Task 7: Filter and Display IT Department Employees.

Apply a filter on the DataFrame to select records where the department is 'IT' and display the filtered DataFrame.
Task 8: Add 10% Bonus to Salaries.

Add a new column named SalaryAfterBonus by adding a 10% bonus to each employee's salary.
Task 9: Find Maximum Salary by Age.

Group the data by age and calculate the maximum salary for each age group.
Task 10: Self-Join on Employee Data.

Join the employees_df DataFrame with itself based on the EmployeeID column.
Task 11: Calculate Average Employee Age.

Calculate the average age of employees.
Task 12: Calculate Total Salary by Department.

Calculate the total salary by department.
Task 13: Sort Data by Age and Salary.

Sort the DataFrame by age and salary.
Task 14: Count Employees in Each Department.

Count the number of employees in each department.
Task 15: Filter Employees with the letter 'o' in the Name.

This project is licensed under the MIT License - see the LICENSE file for details.

