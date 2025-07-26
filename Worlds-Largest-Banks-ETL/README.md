
# World's Largest Banks Data ETL Project

## Overview

This project demonstrates the process of extracting, transforming, and loading (ETL) data related to the world's largest banks by market capitalization. The project includes the following steps:

1. Extracting data from a specified URL.
2. Transforming the data by converting market capitalization values to different currencies.
3. Loading the transformed data into a CSV file and an SQL database.
4. Logging progress at various stages of the ETL process.

## Project Scenario

As a data engineer hired by a research organization, your task is to create a script that compiles a list of the top 10 largest banks in the world ranked by market capitalization in billion USD. The data needs to be transformed and stored in GBP, EUR, and INR based on provided exchange rates. The final data is saved locally as a CSV file and as a table in an SQL database.

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `pandas`
  - `beautifulsoup4`
  - `sqlite3`

You can install the required libraries using pip:

```bash
pip install requests pandas beautifulsoup4
```

## Data Sources

- Bank data URL: [Wikipedia List of Largest Banks](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)
- Exchange rate CSV: [Exchange Rate CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)

## File Structure

- `banks_project.py`: Main script for the ETL process.
- `code_log.txt`: Log file for recording the progress of the script.

## Instructions

1. Clone this repository or download the `banks_project.py` file to your local machine.
2. Run the script using Python:

```bash
python banks_project.py
```

## Functions

### log_progress(message)
Logs the progress of the code at different stages in the file `code_log.txt`.

### extract()
Extracts the tabular information from the given URL under the heading 'By market capitalization' and saves it to a DataFrame.

### transform(df, exchange_rates)
Transforms the DataFrame by adding columns for Market Capitalization in GBP, EUR, and INR, rounded to 2 decimal places, based on the exchange rate information.

### load_to_csv(df, path)
Loads the transformed DataFrame to an output CSV file.

### load_to_db(df, db_name, table_name)
Loads the transformed DataFrame to an SQL database table.

### run_query(db_name, query)
Runs a query on the database table and returns the result as a DataFrame.

### verify_log()
Verifies that the log entries have been completed at all stages by checking the contents of the file `code_log.txt`.

## Example Usage

The script will perform the following operations:

1. Extract data from the specified URL.
2. Transform the data using exchange rates.
3. Load the transformed data into a CSV file.
4. Load the data into an SQL database.
5. Run a sample query on the database.
6. Verify log entries to ensure all stages were logged correctly.

## Output

- A CSV file named `Largest_banks_data.csv` containing the processed data.
- An SQL database named `Banks.db` with a table `Largest_banks` containing the processed data.
- Log entries in `code_log.txt` documenting the progress of each stage.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

This project is part of the IBM Skills Network course on Coursera. The data and instructions were provided as part of the course content
