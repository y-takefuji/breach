import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('breach_report.csv')

# Convert 'Breach Submission Date' to datetime
df['Breach Submission Date'] = pd.to_datetime(df['Breach Submission Date'])

# Sum total affected individuals over dates
total_affected = df.groupby('Breach Submission Date')['Individuals Affected'].sum()

# Save the total affected data as a CSV file
total_affected.to_csv('total_affected.csv')

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(total_affected.index, total_affected.values, label='Total Affected', linestyle='-', linewidth=1, color='black', marker=' ')

plt.xlabel('Date')
plt.ylabel('Individuals Affected')
plt.title('Total Affected Individuals Over Time')
plt.legend()
plt.grid(True)

# Save the figure
plt.savefig('total_affected.png', dpi=300)
plt.show()

