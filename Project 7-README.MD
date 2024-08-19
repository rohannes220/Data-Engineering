---

# Data Engineering Capstone Project

This repository contains the code and data for the Data Engineering Capstone Project. In this project, we design and implement a data platform for retail data analytics, integrating OLTP and NoSQL databases, building a data warehouse, and performing data analysis and visualization.

## Project Modules

### Module 1: OLTP Database Design and Data Insertion

In this module, we design an OLTP database for an e-commerce website and populate it with the provided data.

**Steps:**
1. **Create and Connect to the Database:** Using SQLite, create the `sales_data` table and insert data from `data/oltpdata.csv`.
2. **Automate Data Export:** Set up a process to export daily incremental data into the data warehouse.

**Data Source:** `data/oltpdata.csv`

### Module 2: Data Warehouse Setup

In this module, we design the schema for a data warehouse based on the OLTP and NoSQL databases, create fact and dimension tables, and automate data insertion.

**Steps:**
1. **Design Schema:** Create dimension and fact tables based on provided CSV files.
2. **Load Data:** Populate the data warehouse tables with the provided data.
3. **Automate Data Insertion:** Implement ETL processes for daily data updates.

**Data Sources:**
- `data/DimDate.csv`
- `data/DimCategory.csv`
- `data/DimCountry.csv`
- `data/FactSales.csv`

### Module 3: Machine Learning Model

In this module, we create a Spark connection to the data warehouse and deploy a machine learning model for sales projections.

**Steps:**
1. **Create Spark Connection:** Set up Spark to connect to the data warehouse.
2. **Train Model:** Use SparkML to train a model on the sales data.
3. **Make Predictions:** Deploy the model to make sales projections.

### Module 4: NoSQL Database Setup with MongoDB

In this module, we set up a NoSQL database using MongoDB to store catalog data for the e-commerce website, load the data, and perform queries.

**Steps:**
1. **Set Up MongoDB:** Configure MongoDB and create the necessary collections.
2. **Load Data:** Import data from `data/catalog.json` into MongoDB.
3. **Perform Queries:** Execute queries to analyze the catalog data.

**Data Source:** `data/catalog.json`

### Module 5: E-Commerce Data Visualization

In this module, we create a Business Intelligence dashboard using IBM Cognos Analytics to visualize key business metrics.

**Steps:**
1. **Create Dashboard:** Use IBM Cognos to create visualizations for the provided data.
2. **Generate Charts:** Create line charts, pie charts, and bar charts to represent sales data.

**Data Source:** `data/ecommerce.csv`

**Visualizations:** All visualizations can be found in the `ecommerce_visualizations.pdf` document.

## Data Sources

- **`data/oltpdata.csv`**: Transaction data for the OLTP database.
- **`data/DimDate.csv`**: Dimension table containing date information.
- **`data/DimCategory.csv`**: Dimension table containing product category information.
- **`data/DimCountry.csv`**: Dimension table containing country information.
- **`data/FactSales.csv`**: Fact table containing sales data.
- **`data/catalog.json`**: JSON file containing product catalog data.
- **`data/ecommerce.csv`**: CSV file containing e-commerce sales data.

## Conclusion

This capstone project covers various aspects of data engineering, including OLTP and NoSQL database management, data warehousing, machine learning, and data visualization using IBM Cognos Analytics. Each module provides a comprehensive understanding and practical application of these skills.

---

This version provides a concise overview of each module without going into the specifics of the code, while still giving a clear understanding of what each part of the project entails.
