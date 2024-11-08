pairs = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def solve(s: str) -> str:
    stack = []
    for i, c in enumerate(s):
        if c == " ":
            continue
        if c not in pairs:
            stack.append(c)
            continue
        if not stack or stack[-1] != pairs[c]:
            return f"{c} {i}"
        stack.pop()
    return "ok so far"

n = int(input())
s = input()
print(solve(s))