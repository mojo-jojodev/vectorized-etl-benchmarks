import pandas as pd
import polars as pl
import numpy as np
import time

# Create 5M rows locally for testing
data = {'id': np.arange(5000000), 'value': np.random.randn(5000000), 'category': np.random.choice(['A', 'B', 'C', 'D'], 5000000)}

print("Evaluating Pandas...")
t0 = time.time()
df = pd.DataFrame(data)
res_pd = df.groupby('category')['value'].mean()
print(f"Pandas took: {time.time() - t0:.4f}s")

print("Evaluating Polars (Rust)...")
t1 = time.time()
lf = pl.DataFrame(data)
res_pl = lf.group_by('category').agg(pl.col('value').mean())
print(f"Polars took: {time.time() - t1:.4f}s")
