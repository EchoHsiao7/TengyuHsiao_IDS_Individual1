from main import analyze_column

def test_analyze_column():
    """
    Simple test to check that analyze_column runs without error.
    """
    try:
        analyze_column("Steam_2024_bestRevenue_1500.csv", "price")
    except Exception as e:
        assert False, f"analyze_column raised an exception: {e}"

if __name__ == "__main__":
    test_analyze_column()