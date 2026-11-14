# ============================================================
# DAY 10: Pandas: Filtering, GroupBy, Missing Values
# ============================================================

from pathlib import Path

import pandas as pd

print("\n========== DAY 10 ==========")

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Hafsa"],
    "Age": [20, 22, 21, 23],
    "Department": ["AI", "AI", "Web", "Web"],
    "Score": [85, 90, None, 95]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# Filtering
print("\nStudents with Age > 21:")
print(df[df["Age"] > 21])

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values
df["Score"] = df["Score"].fillna(0)

print("\nAfter Filling Missing Values:")
print(df)

# GroupBy
print("\nAverage Score by Department:")
print(df.groupby("Department")["Score"].mean())

# CSV: save and load
df.to_csv(Path(__file__).parent / "students.csv", index=False)
loaded = pd.read_csv(Path(__file__).parent / "students.csv")
print("\nLoaded from CSV:")
print(loaded.head())

# Merge: join two tables on a shared column
departments = pd.DataFrame({
    "Department": ["AI", "Web"],
    "Head": ["Dr. Khan", "Ms. Fatima"],
})
merged = df.merge(departments, on="Department", how="left")
print("\nMerged with department heads:")
print(merged)

# Sorting and describing
print("\nTop scorers:")
print(df.sort_values("Score", ascending=False).head(2))
print("\nQuick statistics:")
print(df.describe())
