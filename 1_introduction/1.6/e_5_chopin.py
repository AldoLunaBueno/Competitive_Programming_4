note_equal_to = {
    "A#": "Bb",
    "C#": "Db",
    "D#": "Eb",
    "F#": "Gb",
    "G#": "Ab",
    "Bb": "A#",
    "Db": "C#",
    "Eb": "D#",
    "Gb": "F#",
    "Ab": "G#"
}

i = 1
while True:
    try:
        note, tonality = input().split()
    except EOFError:
        break
    if note in note_equal_to:
        print(f"Case {i}: {note_equal_to[note]} {tonality}")
    else:
        print(f"Case {i}: UNIQUE")
    i += 1