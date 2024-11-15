import pytest
import subprocess

# PATHS ARE ALL YOU NEED TO CHANGE:
PATH_TO_SCRIPT = "b_5_different.js"  # Update to your JavaScript file
PATH_TO_TEST_CASES = "test_b_5_different.txt"

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
    # Run the JavaScript script as a subprocess
    result = subprocess.run(
        ["node", PATH_TO_SCRIPT],  # Use 'node' to run JavaScript files
        input=input_data,
        text=True,
        capture_output=True
    )
    out = result.stdout.strip()
    err = result.stderr
    
    print(err)

    # Compare the output with the expected result
    assert out == expected
