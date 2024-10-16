import pytest
import subprocess
import sys

# PATHS ARE ALL YOU NEED TO CHANGE:
PATH_TO_SCRIPT = "script_to_test.py"
PATH_TO_TEST_CASES = "test_cases.txt"

def load_test_cases(file_name):
    # Read the file and separate the test cases by '==='
    with open(file_name, "r") as f:
        content = f.read().strip()
    
    cases = content.split('===')
    test_cases = []
    
    for case in cases:
        # Split each case into input and output using '---'
        input_data, expected = case.strip().split('---')
        test_cases.append((input_data.strip(), expected.strip()))
    
    return test_cases

# Load test cases from file
test_cases = load_test_cases(PATH_TO_TEST_CASES)

@pytest.mark.parametrize("input_data, expected", test_cases)
def test_multiple_cases(input_data, expected):
    _test_from_data(input_data, expected)

def _test_from_data(input_data, expected):
    # Run the script as a subprocess, pass input and get result
    result = subprocess.run(
        [sys.executable, # get the current Python interpreter
         PATH_TO_SCRIPT],
        input=input_data,
        text=True,
        capture_output=True
    )
    out = result.stdout.strip()
    
    # Compare the output with the expected result
    assert out == expected