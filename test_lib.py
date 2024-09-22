import pandas as pd
import pytest
from lib import calculate_statistics

# Mock data for testing
mock_data = pd.DataFrame({
    "price": [10, 20, 30, 40, 50]
})

def test_calculate_statistics():
    mean, median, std = calculate_statistics(mock_data, "price")
    
    assert mean == pytest.approx(30.0, 0.01)
    assert median == 30
    assert std == pytest.approx(15.81, 0.01)

    
if __name__ == "__main__":
    test_calculate_statistics()
