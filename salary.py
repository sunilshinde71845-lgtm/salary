
def calculate_salary():
    basic_salary = 50000
    hra = basic_salary * 20 / 100
    da = basic_salary * 10 / 100
    gross_salary = basic_salary + hra + da

    return gross_salary


if __name__ == "__main__":
    print("Employee Salary Calculator")
    print("Basic Salary: 50000")
    print("HRA: 10000")
    print("DA: 5000")
    print("Gross Salary:", calculate_salary())
