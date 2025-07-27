# --- Import Required Libraries ---
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import os

# --- Setup relative paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'airfoil_self_noise.csv')
CLEANED_PATH = os.path.join(BASE_DIR, 'NASA_airfoil_noise_cleaned.csv')

# --- Load the CSV File ---
df = pd.read_csv(DATA_PATH)
print("First 5 rows of the dataset:")
print(df.head())

# --- Remove Duplicates and Null Values ---
df = df.drop_duplicates().dropna()
print("Shape of the dataset after cleaning:")
print(df.shape)

# --- Save the Cleaned Data ---
df.to_csv(CLEANED_PATH, index=False)
print(f"Cleaned data saved to '{CLEANED_PATH}'")

# --- Split the Data ---
X = df.drop('SoundLevel', axis=1)
y = df['SoundLevel']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Data split into training and testing sets.")

# --- Train a Linear Regression Model ---
model = LinearRegression()
model.fit(X_train, y_train)
print("Linear regression model trained.")

# --- Make Predictions and Evaluate ---
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
