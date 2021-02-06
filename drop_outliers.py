
def dump_by_quantiles(df, q_low = 0.01 , q_high = 0.99):
    """Inputs:
        df : A Pandas dataframe
        q_low: float,  the lower quantile cut off
        q_high: float, the higher quantile cut off"""

    # create a df of the high and low outliers
    quant_df = df.quantile([q_low, q_high])
    print('Row count before outlier removal', len(df))
    # filter the data by the quant_df - note breaks the memory limit if done together
    df = df[df >= quant_df.loc[0.01]].dropna()
    df = df[df <= quant_df.loc[0.99]] .dropna()
    print('Row count after outlier removal', len(df))
    return df
