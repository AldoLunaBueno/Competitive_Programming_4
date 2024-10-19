# Hissing Microphone - Kattis

def solve(s: str):
    for i in range(len(s)-1):
        if s[i:i+2] == "ss":
            print("hiss")
            return
    print("no hiss")

s = input()
solve(s)
    