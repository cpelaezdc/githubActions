def add(a, b):
  """This function adds two numbers and returns the result."""
  if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
      raise TypeError("Both inputs must be numbers (int or float)")
  return a + b