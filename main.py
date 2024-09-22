"""
This module reads a csv file and produce some useful statistics from it.
"""

from lib import analyze_column

if __name__ == "__main__":
    analyze_column("Steam_2024_bestRevenue_1500.csv", "price")
    
    