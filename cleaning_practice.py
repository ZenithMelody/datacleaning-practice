import pandas as pd
import numpy as np

# --- CREATION OF MESSY DATA ---
raw_data = {
    'Name': ['  John Doe  ', 'Jane Smith', 'Bob', 'Alice  ', np.nan, '  John Doe  '], # Whitespaces, NaN and a duplicate
    'Age': ['25', '30', 'Unknown', '22', '45', '25'],                         # "Unknown" is a str, not a number
    'Salary': ['$50,000', '$60,000', '45000', '$70,000', '52000', '$50,000'],       # Dollar signs and commas everywhere
    'Joined': ['2020-01-01', '2019/05/20', '2021-02-15', '2020-01-01', '2022-08-10', '2020-01-01']
}

df = pd.DataFrame(raw_data)

print("--- BEFORE CLEANING ---")
print(df)
print("\n--- DATA TYPES ---")
print(df.dtypes)

df['Name'] = df['Name'].str.strip()
# "Drop rows if 'Name' column is empty (handling NaN)"
df = df.dropna(subset=['Name'])

df['Salary'] = df['Salary'].str.replace('$', '').str.replace(',', '').astype(int)

# Str ->S Int, "Unknown" -> NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df['Joined'] = pd.to_datetime(df['Joined'])

df = df.drop_duplicates()

print("--- AFTER CLEANING ---")
print(df)
print("\n--- DATA TYPES ---")
print(df.dtypes)