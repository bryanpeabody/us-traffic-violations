import pandas as pd
import matplotlib.pyplot as plt

# Import the CSV into a dataframe
df = pd.read_csv('./data/traffic_violations_with_index.csv')

# Rename columns
df.rename(columns={'Violation Type': 'Violation_Type'}, inplace=True)

# Select the columns that we care about
subset = df[["RowID", "Color", "Violation_Type"]]

# Get counts for each color and sort it desc
counts = subset.groupby('Color')['RowID'].nunique().sort_values(ascending=False).reset_index(name='Count')

# Take the top 7
x_colors = counts['Color'].head(7)
y_counts = counts['Count'].head(7) 

# Setup the bar chart
plt.bar(x_colors, y_counts, color='green')
plt.xlabel('Car Color', labelpad=15)
plt.ylabel('Total Stops', labelpad=15)
plt.title('Total Traffic Stops by Car Color')

# Show the chart
plt.show()
