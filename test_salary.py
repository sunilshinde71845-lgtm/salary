
from salary import calculate_salary

def test_calculate_salary():
    assert calculate_salary() == 65000

def test_gross_salary_is_integer_value():
    assert int(calculate_salary()) == 65000

def test_gross_salary_is_positive():
    assert calculate_salary() > 0
