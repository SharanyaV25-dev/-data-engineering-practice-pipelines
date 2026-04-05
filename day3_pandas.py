import pandas as pd
data = [
    {"name": "Annie ", "city": "Chennai", "salary": 50000},
    {"name": "Balu", "city": "bangalore", "salary": 60000},
    {"name": "Cheran", "city": "Chennai", "salary": None},
    {"name": "Dhruv", "city": "Bangalore", "salary": 80000},
    {"name": "Esha", "city": "Hyderabad", "salary": 55000},
    {"name": "Esha", "city": "Hyderabad", "salary": 55000},
    {"name": "Gugan", "city": "tirunelveli", "salary": 95000},
    {"name": "Sharanya", "city": "tiRuneLveli", "salary": 72000},
    {"name": "Jaggie", "city": "tricHy", "salary": 85000},
    {"name": "Vels", "city": "nagercoiL", "salary": 70000}
]
# Creating dataframe
df = pd.DataFrame(data)
# Finding Total, Avg, Max Salary per city
salary_stats = df.groupby("city").agg(
    total_salary =("salary","sum"),
    avg_salary =("salary","mean"),
    max_salary = ("salary","max")
)
print(salary_stats)
# Adding new column city_avg_salary using transform
df["city_avg_salary"] = df.groupby("city")["salary"].transform("mean")
print(df)
# Filtering cities where avg salary > 60000
high_salary_cities  = df.groupby("city").filter(lambda x:x["salary"].mean() > 60000)
print(high_salary_cities)
# creating a new column above_city_avg (Yes/No)
df["above_city_avg"] = df["salary"] > df["city_avg_salary"]
print(df)
# Sort by salary descending
sorted_df = df.sort_values(by ="salary",ascending = False)
print(sorted_df)
# Creating dept table and merge with employee table
df_dept = pd.DataFrame([
    {"city": "Chennai", "region": "South"},
    {"city": "Bangalore", "region": "North"},
    {"city": "Hyderabad", "region": "North"},
    {"city": "Tirunelveli", "region": "South"},
    {"city": "Nagercoil", "region": "South"}
])
merged_data = pd.merge(df,df_dept,on = "city",how="left")
print(merged_data)