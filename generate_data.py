import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

data = {
    "order_id": range(1, n+1),
    "order_date": pd.date_range(start="2023-01-01", periods=n, freq='h'),
    "region": np.random.choice(["North", "South", "East", "West"], n),
    "product": np.random.choice(["Laptop", "Phone", "Tablet", "Headphones"], n),
    "category": np.random.choice(["Electronics", "Accessories"], n),
    "quantity": np.random.randint(1, 5, n),
    "price": np.random.randint(100, 1000, n)
}

df = pd.DataFrame(data)
df["revenue"] = df["quantity"] * df["price"]

df.to_csv("sales_data_10k.csv", index=False)

print("Dataset created successfully!")