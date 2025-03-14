
from data.split import (
    process_split_ratio,
)

def data_split(data, ratio=0.75, seed=42):
    # Splits of the input data as pyspark.sql.DataFrame.
    multi_split, ratio = process_split_ratio(ratio)

    if multi_split:
        return data.randomSplit(ratio, seed=seed)
    else:
        return data.randomSplit([ratio, 1 - ratio], seed=seed)