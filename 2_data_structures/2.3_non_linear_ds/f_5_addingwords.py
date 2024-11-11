# Adding Words - Kattis

# This problem simulates the basic capability of a code interpreter and adds something else.
# We lookup the value of a given name, but we also lookup the name for a calculated value.
# We need each name given in the calculation to be previously defined. 
# This was my 30 minutes bug, because I wasn't verifying the first operand of the calculations.

import sys

value_to_name = {}
name_to_value = {}

for line in sys.stdin:
    line = line.strip()
    command, *tokens = line.split()
    if command == "calc":
        args = tokens[::2]
        ops = ["+"] + tokens[1:-1:2]
        result = 0
        all_name_found = True
        for i in range(len(args)):
            if args[i] not in name_to_value:
                all_name_found = False
                break
            if ops[i] == "+":
                result += name_to_value[args[i]]
            else:
                result -= name_to_value[args[i]]
        name = "unknown"
        if all_name_found and result in value_to_name:
            name = value_to_name[result]                   
        print(f"{line[5:]} {name}")
    elif command == "def":
        name = tokens[0]
        value = int(tokens[1])
        if name in name_to_value:
            old_value = name_to_value[name]
            del value_to_name[old_value]
        name_to_value[name] = value
        value_to_name[value] = name
    elif command == "clear":
        name_to_value = {}
        value_to_name = {}