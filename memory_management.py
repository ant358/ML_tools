import numpy as np
import pandas as pd

def reduce_memory_usage(df):
    """Reduce the memory used by a pandas dataframe
    """

    start_memory = round(df.memory_usage().sum() / 1024**2, 2)
    print(f"Memory usage of dataframe is {start_memory} MB")
    print("Reducing Memory")

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != 'object':
            # get the min max number in the column
            c_min = df[col].min()
            c_max = df[col].max()

            # sort the integers out
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)

                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)

                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)

                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)

            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)

                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                     pass
        else:
            df[col] = df[col].astype('category')

    end_memory = round(df.memory_usage().sum() / 1024**2, 2)
    print(f"Memory usage of dataframe after reduction {end_memory} MB")
    percent_reduced = round(100 * (start_memory - end_memory) / start_memory, 2)
    print(f"Reduced by {percent_reduced} % ")
    return df
    
    
def mem_used(df):
    """How much memory is that dataframe using?
    Useful on sites like kaggle"""
    size_mb = df.memory_usage().sum() / 1024 / 1024
    print("Test memory size: %.2f MB" % test_size_mb)
    
def convert_to_sparse(df):
    """Save memory by converting dataframes to sparse arrays"""
    return df.replace(0, np.nan).to_sparse()

