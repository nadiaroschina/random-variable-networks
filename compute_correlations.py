import pandas as pd
from scipy.stats import pearsonr, kendalltau

def compute_pearson_correlation(df):
    correlations = {}
    for col1 in df.columns:
        for col2 in df.columns:
            if col1 != col2:
                correlations[(col1, col2)] = pearsonr(df[col1], df[col2]).statistic
    return correlations


def compute_kendall_correlation(df):
    correlations = {}
    for col1 in df.columns:
        for col2 in df.columns:
            if col1 != col2:
                correlations[(col1, col2)] = kendalltau(df[col1], df[col2]).statistic
    return correlations

