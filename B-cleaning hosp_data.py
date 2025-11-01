import pandas as pd
import numpy as np

# ---------- Step 1: Load the messy CSV file ----------
df = pd.read_csv("Hospital_Patient_Data_Messy.csv")

print("Original shape:", df.shape)
print(df.head())

# ---------- Step 2: Remove duplicate rows ----------
df = df.drop_duplicates()

# ---------- Step 3: Handle missing values ----------
# Replace 'missing', '-', 'NA', and blank spaces with NaN
df.replace(['missing', '-', 'NA', 'na', 'NaN', ' ', ''], np.nan, inplace=True)

# Convert numeric-like columns properly
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

df['Bill_Amount'] = pd.to_numeric(
    df['Bill_Amount'].astype(str).str.replace('[₹,]', '', regex=True),
    errors='coerce'
)

df['Room_No'] = pd.to_numeric(df['Room_No'], errors='coerce')

# Fill missing numeric values
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Bill_Amount'].fillna(df['Bill_Amount'].median(), inplace=True)
df['Room_No'].fillna(df['Room_No'].mode()[0], inplace=True)

# Fill missing text values
for col in ['Name', 'Department', 'Doctor', 'Feedback', 'Contact_No', 'City', 'Status']:
    df[col].fillna('Unknown', inplace=True)

# ---------- Step 4: Fix text formatting ----------
df['Department'] = df['Department'].str.strip().str.title()
df['Doctor'] = df['Doctor'].str.strip().str.title().str.replace('Dr ', 'Dr. ', regex=False)
df['City'] = df['City'].str.strip().str.title()
df['Status'] = df['Status'].str.strip().str.capitalize()
df['Feedback'] = df['Feedback'].str.strip().str.capitalize()

# Correct spelling errors in Department
df['Department'].replace({
    'Cardio': 'Cardiology',
    'Cardio.': 'Cardiology',
    'Ortho': 'Orthopedics',
    'Neuro': 'Neurology',
    'Gynacology': 'Gynecology',
    'Gynae': 'Gynecology'
}, inplace=True)

# ---------- Step 5: Standardize Gender ----------
df['Gender'] = df['Gender'].astype(str).str.strip().str.capitalize()
df['Gender'].replace({
    'Male': 'M',
    'Female': 'F'
}, inplace=True)

# ---------- Step 6: Fix date columns ----------
df['Admission_Date'] = pd.to_datetime(df['Admission_Date'], errors='coerce', dayfirst=True)
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'], errors='coerce', dayfirst=True)

# ---------- Step 7: Remove unrealistic values ----------
df = df[df['Age'].between(0, 120)]
df = df[df['Bill_Amount'] > 0]

# ---------- Step 8: Final touch ----------
df.reset_index(drop=True, inplace=True)

# ---------- Step 9: Save cleaned file ----------
df.to_csv("Hospital_Patient_Data_Cleaned.csv", index=False)

print("\nData cleaning completed successfully!")
print("New shape:", df.shape)
print("File saved as: Hospital_Patient_Data_Cleaned.csv")
