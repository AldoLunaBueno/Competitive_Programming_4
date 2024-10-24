# Saving Daylight - Kattis

# too easy
while True:
    try:
        *rest, start, end = input().split()
    except EOFError:
        break
    sh, sm = map(int, start.split(":"))
    eh, em = map(int, end.split(":"))
    start = 60*sh + sm
    end = 60*eh + em
    time = end - start
    h = time // 60
    m = time % 60
    print(f"{' '.join(rest)} {h} hours {m} minutes")