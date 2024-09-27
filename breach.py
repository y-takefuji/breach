import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('breach_report.csv')

# Display unique entity types
unique_entity_types = df['Covered Entity Type'].unique()
print("Unique Entity Types:")
for i, entity in enumerate(unique_entity_types, 1):
    print(f"{i}. {entity}")

# User selects an entity type by number
selected_number = int(input("Select an entity type by number: "))
selected_entity_type = unique_entity_types[selected_number - 1]

# Filter data by selected entity type
filtered_df = df[df['Covered Entity Type'] == selected_entity_type]

# Convert 'Breach Submission Date' to datetime
filtered_df['Breach Submission Date'] = pd.to_datetime(filtered_df['Breach Submission Date'])

# Extract month and year from 'Breach Submission Date'
filtered_df['Month'] = filtered_df['Breach Submission Date'].dt.to_period('M')

# Sum monthly affected individuals by breach type
monthly_sum = filtered_df.groupby(['Month', 'Type of Breach'])['Individuals Affected'].sum().unstack()

monthly_sum.to_csv(f'{selected_entity_type}_monthly_sum.csv')
# Plot the graph
plt.figure(figsize=(10, 6))
linestyles = ['-', '--', '-.', ':']
widths = [1, 2]
num_lines = len(monthly_sum.columns)
for i, (breach_type, data) in enumerate(monthly_sum.items()):
    linestyle = linestyles[i % len(linestyles)]
    width = widths[(i // len(linestyles)) % len(widths)]
    plt.plot(data.index.to_timestamp(), data.values, label=breach_type, linestyle=linestyle, linewidth=width, color='black')

plt.xlabel('Month')
plt.ylabel('Individuals Affected')
plt.title(f'Monthly Affected Individuals by Breach Type for {selected_entity_type}')
plt.legend()
plt.grid(True)

# Save the figure with the name of the selected entity type
plt.savefig(f'{selected_entity_type}.png',dpi=300)
plt.show()

