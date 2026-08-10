import polars as pl

df = pl.DataFrame({"name": ["A", "B", "C"], "score": [80, 95, 72]})
print(df.filter(pl.col("score") > 75))
