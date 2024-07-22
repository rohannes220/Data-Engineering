# Airfoil Noise Prediction ML Pipeline Project

## Scenario

You are a data engineer at an aeronautics consulting company. Your task is to build a simple ML pipeline to predict the sound level of airfoils using a modified version of the NASA Airfoil Self Noise dataset. The pipeline should involve data cleaning, model training, and evaluation.

## Objectives

### Part 1: Perform ETL Activity
1. Load a CSV dataset.
2. Remove duplicates and rows with null values.
3. Store the cleaned data in a new CSV file.

### Part 2: Create a Machine Learning Model
1. Train a simple linear regression model.

### Part 3: Evaluate the Model
1. Evaluate the model using Mean Squared Error (MSE).

## Setup

You will need the following libraries:
- `pandas`
- `scikit-learn`

Install them using:
```python
!pip install pandas scikit-learn -q
```

## Part 1: Perform ETL Activity

### Task 1: Import Required Libraries
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
```

### Task 2: Load the CSV File into a DataFrame
Download the dataset and save it locally as `airfoil_self_noise.csv`.

```python
df = pd.read_csv('/mnt/data/airfoil_self_noise.csv')
print(df.head())
```

### Task 3: Remove Duplicates and Null Values
```python
df = df.drop_duplicates().dropna()
print(df.shape)
```

### Task 4: Save the Cleaned Data
```python
df.to_csv('NASA_airfoil_noise_cleaned.csv', index=False)
```

## Part 2: Create a Machine Learning Model

### Task 1: Split the Data
```python
X = df.drop('SoundLevel', axis=1)
y = df['SoundLevel']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```

### Task 2: Train a Linear Regression Model
```python
model = LinearRegression()
model.fit(X_train, y_train)
```

## Part 3: Evaluate the Model

### Task 1: Make Predictions and Evaluate
```python
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
```

## Summary

This project involves loading a dataset, cleaning it, building a simple linear regression model, and evaluating the model. The steps are designed to be straightforward and manageable for someone with two weeks of experience.

## Dataset

The dataset used in this project can be found in the file `airfoil_self_noise.csv`. Ensure to download and use this file for the ETL activities and model building.
