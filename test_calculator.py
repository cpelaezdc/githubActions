# test_calculator.py
import pytest  # Import pytest
from calculator import add # Import the function we want to test

# Test Case 1: Adding two positive integers
def test_add_positive_integers():
  """Tests adding two positive integers."""
  assert add(2, 3) == 5

# Test Case 2: Adding a positive and a negative integer
def test_add_positive_and_negative():
  """Tests adding a positive and a negative integer."""
  assert add(5, -3) == 2
  assert add(-7, 4) == -3

# Test Case 3: Adding floats
def test_add_floats():
    """Tests adding two floating-point numbers."""
    # Use pytest.approx for floating point comparisons due to potential precision issues
    assert add(0.1, 0.2) == pytest.approx(0.3)

# Bonus Test Case 4: Testing the type error
def test_add_invalid_input():
    """Tests that a TypeError is raised for non-numeric input."""
    with pytest.raises(TypeError):
        add("a", 3)
    with pytest.raises(TypeError):
        add(5, "b")
    with pytest.raises(TypeError):
        add(None, 2)