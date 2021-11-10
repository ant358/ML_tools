def get_ideal_class_size(df, label):
    """For binary classes. 
    Work out what the balanced 
    class size would be"""
    cl0 = df[label].value_counts()[0]
    cl1 = df[label].value_counts()[1]
    diff = abs(cl0 - cl1)/2
    ideal = min(cl0, cl1) + diff
    return ideal

def get_balanced_df(df, label):
    """For binary classes. 
    Return a balanced dataframe. 
    Under and over sample to balance the class"""
    ideal_size = get_ideal_class_size(df, label)
    if df[label].value_counts()[0] > df[label].value_counts()[1]:
        df_0 = df[df[label]==0].sample(int(ideal_size))
        df_1 = df[df[label]==1].sample(int(ideal_size), replace=True)
    else:
        df_0 = df[df[label]==0].sample(int(ideal_size), replace=True)
        df_1 = df[df[label]==1].sample(int(ideal_size))
    balanced_df = pd.concat([df_0, df_1])
    return balanced_df
