# SwiftAuto Traders Car Sales and Profits Analysis

## Project Overview
This project involves analyzing car sales and profits for SwiftAuto Traders, a chain of car dealerships. As a data scientist, your task is to create visualizations and present them as a dashboard/report to provide insights on car sales and profits for each dealer.

## Dataset
The dataset used in this lab is a modified subset provided specifically for this lab exercise. Ensure you use the dataset provided with the lab instructions.

### CSV File
The CSV file used in this project is `SalesData.csv`. It contains the following columns:
- **Dealer ID**: Unique identifier for each dealer.
- **Car Sold**: Model of the car sold.
- **Quantity Sold**: Total quantity of cars sold.
- **Cost to Buy**: Cost price of the car.
- **Cost to Sell**: Selling price of the car.
- **Recalls**: Number of recalls per car model.
- **Customer Sentiment**: Sentiment of customer reviews (Positive, Neutral, Negative).
- **Sale Month**: Month of the car sale.
- **Affected System**: The system affected by recalls (e.g., Brakes, Electrical, Engine, Transmission).
- **Profit**: Profit made from selling the car.

## Objective
The objective is to analyze historical trends in car sales and provide insights on car sales and profits for each dealer. You will create visualizations using either IBM's Cognos Analytics or Google's Looker Studio.

## Tasks
### Task 1: Sales Dashboard/Report Page
Create a dashboard/report page titled **Sales** to capture the following KPI metrics:
- **Profit**: Format to 1 decimal place in millions of US dollars.
- **Quantity Sold**: Total quantity of cars sold.
- **Bar Chart**: Quantity sold by car model.
- **Average Quantity Sold**: Average number of cars sold.

### Task 2: Profit by Dealer ID
Develop a column chart to display **Profit by Dealer ID** in the Sales dashboard/report page, sorted in ascending order.

### Task 3: Service Dashboard/Report Page
Create another dashboard/report page titled **Service** to capture the following KPI metrics:
- **Column Chart**: Number of recalls per car model.
- **Treemap**: Customer sentiment comparing positive, neutral, and negative reviews.
- **Line and Column Chart**: Quantity of cars sold per month compared to profit.
- **Heatmap/Pivot Table**: Number of recalls by model and affected system.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
The data used in this project is publicly available from the IBM Accelerator Catalog. The terms of use for this data are located at [IBM Developer Terms of Use](https://developer.ibm.com/terms/ibm-developer-terms-of-use/).
