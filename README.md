#Hospital Data Cleaning and Visualization Project
->Overview
This project demonstrates my ability to work with real-world messy data, perform data cleaning using Pandas, and extract actionable insights through Matplotlib visualizations. I worked with a large, unstructured hospital dataset (550+ rows) containing patient information, billing details, departments, and admission records. The goal was to clean, transform, and visualize this data to make it analysis-ready.
->Task 1 – Data Understanding
• Imported the dataset (Hospital_Patient_Data_Messy.csv) using Pandas.
• Explored the dataset with .info() and .describe() to identify missing values, incorrect data types, and inconsistent formatting.
• Observed real-world data issues like duplicate entries, mixed date formats, inconsistent text (e.g., Cardio, cardiology), and missing billing data.
->Task 2 – Data Cleaning (Using Pandas)
• Removed duplicate rows and standardized text formatting.
• Handled missing values by filling them with median or mode depending on data type.
• Cleaned numeric columns (Bill Amount, Room No, Age) by removing symbols (₹, commas) and converting them to proper numeric data types.
• Corrected spelling variations in departments (e.g., Ortho → Orthopedics, Gynacology → Gynecology).
• Converted mixed date formats into a consistent datetime structure using pd.to_datetime().
• Filtered out invalid data like unrealistic ages or negative bill amounts.
• Exported the final cleaned dataset as Hospital_Patient_Data_Cleaned.csv.
->Task 3 – Data Visualization (Using Matplotlib & NumPy)
Created insightful charts to summarize hospital performance and patient demographics:
1. Bar Chart – Number of patients in each department
2. Pie Chart – Patient distribution by city
3. Line Chart – Average bill amount per department
4. Histogram – Age distribution of patients
5. Scatter Plot – Relationship between patient age and bill amount
Each chart was designed using Matplotlib, focusing on clarity and interpretability without external styling libraries.
->Key Insights
• Departments like Cardiology and Orthopedics had the highest patient volume.
• Cities like Mumbai and Pune contributed the most patients.
• Average bill amounts varied significantly across departments, highlighting possible differences in treatment costs.
