import pandas as pd

def calculate_statistics(df, column_name):
    """
    Calculate mean, median, and standard deviation for a specified column.
    """
    mean_value = df[column_name].mean(numeric_only=True)
    median_value = df[column_name].median(numeric_only=True)
    std_value = df[column_name].std(numeric_only=True)
    
    print(f"{column_name} Statistics:\n")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_value}")
    
    return mean_value, median_value, std_value


def analyze_column(csv_file, column_name):
    """
    Load the CSV file, calculate statistics, and plot a histogram for a given column.
    """
    df = pd.read_csv(csv_file)
    calculate_statistics(df, column_name)



