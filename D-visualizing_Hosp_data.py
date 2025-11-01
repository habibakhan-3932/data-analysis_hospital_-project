import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv("Hospital_Patient_Data_Cleaned.csv")

# --------- BAR CHART: Number of patients per department ----------
departments = df['Department'].value_counts().index
dept_counts = df['Department'].value_counts().values

plt.figure(figsize=(10,6))
plt.bar(departments, dept_counts)
plt.title("Number of Patients per Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------- PIE CHART: Patient distribution by city ----------
city_counts = df['City'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(city_counts.values, labels=city_counts.index, autopct='%1.1f%%', startangle=90)
plt.title("Patient Distribution by City")
plt.show()

# --------- LINE CHART: Average Bill Amount per Department ----------
avg_bill = df.groupby('Department')['Bill_Amount'].mean()
departments = avg_bill.index
bills = avg_bill.values

plt.figure(figsize=(10,6))
plt.plot(departments, bills, marker='o')
plt.title("Average Bill Amount per Department")
plt.xlabel("Department")
plt.ylabel("Average Bill Amount (₹)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --------- HISTOGRAM: Distribution of Patient Ages ----------
ages = df['Age'].dropna().values
plt.figure(figsize=(8,5))
plt.hist(ages, bins=10, edgecolor='black')
plt.title("Age Distribution of Patients")
plt.xlabel("Age")
plt.ylabel("Number of Patients")
plt.tight_layout()
plt.show()

# --------- EXTRA (optional): Correlation between Age and Bill ----------
plt.figure(figsize=(8,6))
plt.scatter(df['Age'], df['Bill_Amount'], alpha=0.6)
plt.title("Relationship Between Age and Bill Amount")
plt.xlabel("Age")
plt.ylabel("Bill Amount (₹)")
plt.grid(True)
plt.tight_layout()
plt.show()

print(" Visualization completed successfully!")
