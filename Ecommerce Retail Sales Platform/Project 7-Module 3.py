import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import length
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# --- Initialize Spark session ---
spark = SparkSession.builder.appName("Search Term Analysis").getOrCreate()

# --- Load dataset ---
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv"
search_terms_df = spark.read.csv(url, header=True, inferSchema=True)

# --- Step 1: Print number of rows & columns ---
rows = search_terms_df.count()
columns = len(search_terms_df.columns)
print(f"Number of rows: {rows}, Number of columns: {columns}")

# --- Step 2: Show top 5 rows ---
search_terms_df.show(5)

# --- Step 3: Print schema (check data types) ---
search_terms_df.printSchema()

# --- Step 4: Count how many times 'gaming laptop' was searched ---
gaming_laptop_count = search_terms_df.filter(search_terms_df.searchterm == 'gaming laptop').count()
print(f"'gaming laptop' was searched {gaming_laptop_count} times")

# --- Step 5: Show top 5 most frequent search terms ---
top_5_terms = search_terms_df.groupBy('searchterm').count().orderBy('count', ascending=False)
top_5_terms.show(5)

# --- Step 6: Add a column for search term length ---
search_terms_df = search_terms_df.withColumn('searchterm_length', length(search_terms_df['searchterm']))

# --- Step 7: Prepare data for linear regression ---
vectorAssembler = VectorAssembler(inputCols=['count'], outputCol='features')
vsearch_terms_df = vectorAssembler.transform(search_terms_df).select(['features', 'searchterm_length'])

# --- Step 8: Split data into training and test sets ---
train_df, test_df = vsearch_terms_df.randomSplit([0.8, 0.2])

# --- Step 9: Train linear regression model ---
lr = LinearRegression(featuresCol='features', labelCol='searchterm_length')
lr_model = lr.fit(train_df)

# --- Step 10: Make predictions ---
predictions = lr_model.transform(test_df)
predictions.select('features', 'searchterm_length', 'prediction').show(5)

# --- Step 11: Evaluate model using RMSE ---
evaluator = RegressionEvaluator(labelCol="searchterm_length", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE) on test data = {rmse}")

# --- Step 12: Predict lengths for the entire dataset ---
search_terms_predictions = lr_model.transform(vsearch_terms_df)
search_terms_predictions.select('features', 'searchterm_length', 'prediction').show(5)
