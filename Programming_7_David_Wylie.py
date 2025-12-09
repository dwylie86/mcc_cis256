# David Wylie
# CIS256 Term (Fall 2025)
# Programming Assignment 7 (PA 7)
import pandas as pd

# Load the office_data.csv file into a Pandas DataFrame.
df = pd.read_csv('office_data.csv')

# Handle Missing Values:
# Fill missing values in the Age column with the median age.
df['Age'] = df['Age'].fillna(df['Age'].median()).round()

# Fill missing values in the Salary column with the mean salary.
df['Salary'] = df['Salary'].fillna(df['Salary'].mean()).round()

# Check for and remove any duplicate rows based on all columns.
df = df.drop_duplicates(subset=['ID', 'Name', 'Age', 'Salary', 'Department'])

# Display the cleaned DataFrame to ensure that there
# are no missing values and no duplicate rows.
print(df)
