import pandas as pd

# Load the data
df = pd.read_csv('breach_report.csv')

# Convert 'Breach Submission Date' to datetime
df['Breach Submission Date'] = pd.to_datetime(df['Breach Submission Date'])

# Extract year and month from 'Breach Submission Date'
df['YearMonth'] = df['Breach Submission Date'].dt.to_period('M')
df['Year'] = df['Breach Submission Date'].dt.year

# Filter data for the years 2022 to 2024
filtered_df = df[(df['Year'] >= 2022) & (df['Year'] <= 2024)]

# Sum affected individuals by month for each year
monthly_sum = filtered_df.groupby(['Year', 'YearMonth'])['Individuals Affected'].sum()

# Find the month with the most affected individuals for each year
most_affected_months = monthly_sum.groupby('Year').idxmax()
most_affected_counts = monthly_sum.groupby('Year').max()

# Display the results
for year in most_affected_months.index:
    print(f"The most affected month in {year} is {most_affected_months[year][1]} with {most_affected_counts[year]} individuals affected.")

# Save the monthly sum data as a CSV file
monthly_sum.to_csv('monthly_affected_individuals_2022_2024.csv')

