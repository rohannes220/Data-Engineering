import os
# Import necessary modules
from pyspark.sql import SparkSession
from pyspark.sql.functions import length
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

# Initialize Spark session
spark = SparkSession.builder.appName("Search Term Analysis").getOrCreate()

# Step 3: Download and Load the Dataset
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv"
search_terms_df = spark.read.csv(url, header=True, inferSchema=True)

# Step 4: Print the number of rows and columns (shape)
rows = search_terms_df.count()
columns = len(search_terms_df.columns)
print(f"Number of rows: {rows}, Number of columns: {columns}")

# Step 5: Print the top 5 rows
search_terms_df.show(5)

# Step 6: Find out the datatype of the column `searchterm`
search_terms_df.printSchema()

# Step 7: How many times was the term `gaming laptop` searched?
gaming_laptop_count = search_terms_df.filter(search_terms_df.searchterm == 'gaming laptop').count()
print(f"'gaming laptop' was searched {gaming_laptop_count} times")

# Step 8: Print the top 5 most frequently used search terms
top_5_terms = search_terms_df.groupBy('searchterm').count().orderBy('count', ascending=False)
top_5_terms.show(5)

# Additional Analysis
# Adding a new column for the length of the search term
search_terms_df = search_terms_df.withColumn('searchterm_length', length(search_terms_df['searchterm']))

# Prepare the data for training the model
vectorAssembler = VectorAssembler(inputCols=['count'], outputCol='features')
vsearch_terms_df = vectorAssembler.transform(search_terms_df)
vsearch_terms_df = vsearch_terms_df.select(['features', 'searchterm_length'])

# Split the data into training and test sets
train_df, test_df = vsearch_terms_df.randomSplit([0.8, 0.2])

# Train a simple linear regression model
lr = LinearRegression(featuresCol='features', labelCol='searchterm_length')
lr_model = lr.fit(train_df)

# Make predictions on the test data
predictions = lr_model.transform(test_df)
predictions.select('features', 'searchterm_length', 'prediction').show(5)

# Evaluate the model
evaluator = RegressionEvaluator(labelCol="searchterm_length", predictionCol="prediction", metricName="rmse")
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE) on test data = {rmse}")

# Predict the length of search terms in the dataset
search_terms_predictions = lr_model.transform(vsearch_terms_df)
search_terms_predictions.select('features', 'searchterm_length', 'prediction').show(5)
