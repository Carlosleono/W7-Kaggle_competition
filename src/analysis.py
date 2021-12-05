def removeoutliers(df, listvars, z):
    """
    This function removes outliers from a dataframe based on its zscore
    """
    from scipy import stats
    import numpy as np
    for var in listvars:
        df1 = df[np.abs(stats.zscore(df[var])) < z]
    return df1