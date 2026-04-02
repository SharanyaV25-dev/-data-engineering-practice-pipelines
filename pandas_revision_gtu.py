import pandas as pd

# -----------------------------
# Step 1: Create Raw Data
# -----------------------------
data = [
    {"name": "Annie ", "city": "Chennai", "salary": 50000},
    {"name": "Balu", "city": "bangalore", "salary": 60000},
    {"name": "Cheran", "city": "Chennai", "salary": None},
    {"name": "Dhruv", "city": "Bangalore", "salary": 80000},
    {"name": "Esha", "city": "Hyderabad", "salary": 55000},
    {"name": "Esha", "city": "Hyderabad", "salary": 55000}
]

df = pd.DataFrame(data)

# -----------------------------
# Step 2: Data Cleaning
# -----------------------------

# Standardize names (remove spaces + lowercase)
df["name"] = df["name"].str.lower().str.strip()

# Standardize city names (handle case issues)
df["city"] = df["city"].str.lower().str.capitalize()

# Handle missing salary values
df["salary"] = df["salary"].fillna(0)

# Remove duplicate records
df = df.drop_duplicates()

# -----------------------------
# Step 3: Data Transformation
# -----------------------------

# Add bonus column (10% of salary)
df["salary_bonus"] = df["salary"] * 0.1

# Categorize employees based on salary
df["category"] = df["salary"].apply(lambda x: "High" if x > 60000 else "Low")

# Sort data by salary descending
df = df.sort_values(by="salary", ascending=False)

print("Cleaned & Transformed Data:")
print(df)

# -----------------------------
# Step 4: Create Department Data
# -----------------------------
df_dept = pd.DataFrame([
    {"city": "Chennai", "region": "South"},
    {"city": "Bangalore", "region": "South"},
    {"city": "Hyderabad", "region": "South"}
])

# -----------------------------
# Step 5: Merge DataFrames
# -----------------------------

# Left join to add region info
df_merged = pd.merge(df, df_dept, on="city", how="left")

print("\nFinal Merged Data:")
print(df_merged)