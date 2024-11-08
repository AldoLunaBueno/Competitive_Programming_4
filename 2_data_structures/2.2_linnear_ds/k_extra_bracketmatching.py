pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def solve(s: str) -> str:
    stack = []
    for c in s:
        if c not in pairs:
            stack.append(c)
            continue
        if not stack or stack[-1] != pairs[c]:
            return "Invalid"
        stack.pop()
    if stack:
        return "Invalid"
    return "Valid"

n = int(input())
s = input()
print(solve(s))