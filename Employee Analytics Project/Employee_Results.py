from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, DateType
from pyspark.sql.functions import col, max as spark_max, avg

# --- Initialize Spark session ---
spark = SparkSession.builder.appName("EmployeeData").getOrCreate()

# --- Define schema for employees.csv ---
schema = StructType([
    StructField("EmployeeID", IntegerType(), True),
    StructField("Name", StringType(), True),
    StructField("Department", StringType(), True),
    StructField("Salary", FloatType(), True),
    StructField("JoiningDate", DateType(), True),
    StructField("Age", IntegerType(), True)
])

# --- Setup relative path for CSV ---
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'data', 'employees.csv')

# --- Task 1: Read CSV into DataFrame ---
employees_df = spark.read.csv(CSV_PATH, header=True, schema=schema)
employees_df.show()

# --- Task 2: Display schema ---
employees_df.printSchema()

# --- Task 3: Create temporary view ---
employees_df.createOrReplaceTempView("employees")

# --- Task 4: Execute SQL query (all records) ---
spark.sql("SELECT * FROM employees").show()

# --- Task 5: Average Salary by Department ---
avg_salary_by_department_df = spark.sql("""
    SELECT Department, AVG(Salary) AS AverageSalary
    FROM employees
    GROUP BY Department
""")
avg_salary_by_department_df.show()

# --- Task 6: Filter IT Department Employees ---
it_employees_df = employees_df.filter(employees_df.Department == 'IT')
it_employees_df.show()

# --- Task 7: Add 10% Bonus to Salaries ---
employees_with_bonus_df = employees_df.withColumn("SalaryAfterBonus", col("Salary") * 1.10)
employees_with_bonus_df.show()

# --- Task 8: Maximum Salary by Age ---
max_salary_by_age_df = employees_df.groupBy("Age").agg(spark_max("Salary").alias("MaxSalary"))
max_salary_by_age_df.show()

# --- Task 9: Self-Join on Employee Data ---
self_joined_df = employees_df.alias("emp1").join(employees_df.alias("emp2"),
                                                 col("emp1.EmployeeID") == col("emp2.EmployeeID"))
self_joined_df.show()

# --- Task 10: Average Employee Age ---
avg_age_df = employees_df.agg(avg("Age").alias("AverageAge"))
avg_age_df.show()

# --- Task 11: Total Salary by Department ---
total_salary_by_department_df = employees_df.groupBy("Department").agg({"Salary": "sum"}) \
                                            .withColumnRenamed("sum(Salary)", "TotalSalary")
total_salary_by_department_df.show()

# --- Stop Spark session ---
spark.stop()
