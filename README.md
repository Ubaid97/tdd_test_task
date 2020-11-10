# TDD task
**Steps**
- Created new file to write tests
    - include 'test' in the filename
    - import class containing functions to be tested: ```from functions import Functions```
    - import unittest module
    - import pytest module
    - pip install pytest
- Create a class with syntax:
```python
Class TestClass(unittest.TestCase):
```
- Create new instance of class to be tested
```python
t1 = Functions()
```
- Write test function
    - function name should start with 'test'
    - Use appropriate assert conditions:
```python
    def test_divisible_by(self):
        # Boolean: returns True if the first number passed in to the divisible by function is divisible by the second number. False otherwise
        self.assertTrue(self.t1.divisible_by(6, 3)) # 6 is divisible by 3 - should return True
        self.assertFalse(self.t1.divisible_by(6, 5)) # 6 isn't divisible by 5, should return False
```
- Create new file to write code that will pass tests
    - same name as the class imported in the test class
    - write function to pass test case:
 ```python
    # function takes in two numbers. Returns True if dividing the first by the second has a remainder of 0. False otherwise
    def divisible_by(self, num1, num2):
        return num1 % num2 == 0
```
- Repeat steps for any other functionality to be implemented
- Run tests using ```pytest -v``` 