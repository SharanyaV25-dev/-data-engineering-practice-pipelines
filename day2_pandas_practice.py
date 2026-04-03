import pandas as pd
data = pd.DataFrame([
    {"name": "Annie", "city": " chennai", "salary": 50000},
    {"name": "Balu", "city": "bangalore ", "salary": None},
    {"name": "Annie", "city": "Chennai", "salary": 50000},
    {"name": "David", "city": " Hyderabad ", "salary": 80000},
    {"name": "Esha", "city": None, "salary": 55000}
])
#Q1 - Handling missing city (replace with "Unknown")
data["city"] = data["city"].fillna("Unknown")
#Q2 - Cleaning city column
data["city"] = data["city"].str.strip().str.lower().str.capitalize()
#Q3 - Handling missing salary using mean
data["salary"] =  data["salary"].fillna(data["salary"].mean().round(2))
#Q4 - Removing duplicates records
data = data.drop_duplicates()
#Q5 - Create column: salary_category (High/Low)
data["salary_category"] = data["salary"].gt(60000).map({True:"High", False:"Low"})
#Q6 - Sort by salary descending
data = data.sort_values(by = "salary",ascending = False)
#Q7 - Creating another dataframe and merging with main dataframe
dept = pd.DataFrame([
    {"city": "Chennai", "region": "South"},
    {"city": "Bangalore", "region": "South"},
    {"city": "Hyderabad", "region": "South"},
    {"city": "Unknown", "region": "Unknown"}
])
data = pd.merge(data,dept,on = "city",how = "left")
print(data)