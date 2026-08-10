import dask.dataframe as dd

df = dd.from_pandas(
    __import__("pandas").DataFrame({"x": [1, 2, 3, 4]}),
    npartitions=2
)
print(df.x.sum().compute())
