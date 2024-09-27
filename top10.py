import pandas as pd

# Load the data
df = pd.read_csv('breach_report.csv')

# Group by 'Name of Covered Entity' and sum the affected individuals
top_breached_entities = df.groupby('Name of Covered Entity')['Individuals Affected'].sum().nlargest(10)

# Display the top 10 breached entities with affected individuals
print("Top 10 Breached Entities with Affected Individuals:")
print(top_breached_entities)

# Save the top breached entities data as a CSV file
top_breached_entities.to_csv('top_breached_entities.csv')

