# Python solution file
def perform_integer_division(T, test_cases):
    results = []
    
    for case in test_cases:
        try:
            a, b = case.split()
            num1 = int(a)
            num2 = int(b)
            if num2 == 0:
                raise ZeroDivisionError("integer division or modulo by zero")
            results.append(num1 // num2)
        except ValueError as ve:
            results.append(f"Error Code: {ve}")
        except ZeroDivisionError as zde:
            results.append(f"Error Code: {zde}")
    
    for result in results:
        print(result)

# Reading input
T = int(input().strip())
test_cases = []
for _ in range(T):
    test_cases.append(input().strip())

# Processing each test case
perform_integer_division(T, test_cases)
