import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('../data/sales_data_10k.csv')

# Total Revenue
total_revenue = df['revenue'].sum()
print("Total Revenue:", total_revenue)

# Revenue by Region
region_sales = df.groupby('region')['revenue'].sum()
print("\nRevenue by Region:\n", region_sales)

# Top Products
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
print("\nTop Products:\n", top_products)

# Plot
region_sales.plot(kind='bar')
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.show()