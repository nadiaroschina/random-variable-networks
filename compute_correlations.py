def compute_pearson_correlation(df):
    edge_weights = {}
    correlation_matrix = df.corr(method="pearson")
    for col1 in correlation_matrix.columns:
        for j, col2 in enumerate(correlation_matrix.columns):
            if col1 != col2:
                edge_weights[(col1, col2)] = correlation_matrix[col1].iloc[j]
    return edge_weights


def compute_kendall_correlation(df):
    edge_weights = {}
    correlation_matrix = df.corr(method="kendall")
    for col1 in correlation_matrix.columns:
        for j, col2 in enumerate(correlation_matrix.columns):
            if col1 != col2:
                edge_weights[(col1, col2)] = correlation_matrix[col1].iloc[j]
    return edge_weights
