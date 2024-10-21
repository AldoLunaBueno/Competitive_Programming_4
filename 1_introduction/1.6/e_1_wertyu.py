qwerty = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
while True:
    try:
        s = input()
    except EOFError:
        break
    for c in s:
        if c == " ":
            print(" ", end="")
        else:
            i = qwerty.index(c)
            print(qwerty[i-1], end="")
    print()