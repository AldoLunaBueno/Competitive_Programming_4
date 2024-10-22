
NUM_FINGERS = 10

FINGERS_PER_NOTE = {
    "c": [2, 3, 4, 7, 8, 9, 10],
    "d": [2, 3, 4, 7, 8, 9],
    "e": [2, 3, 4, 7, 8],
    "f": [2, 3, 4, 7],
    "g": [2, 3, 4],
    "a": [2, 3],
    "b": [2],
    "C": [3],
    "D": [1, 2, 3, 4, 7, 8, 9],
    "E": [1, 2, 3, 4, 7, 8],
    "F": [1, 2, 3, 4, 7],
    "G": [1, 2, 3, 4],
    "A": [1, 2, 3],
    "B": [1, 2],
}

def get_fingers(note: str):
    return [finger in FINGERS_PER_NOTE[note] for finger in range(1, NUM_FINGERS+1)]

num_cases = int(input())
for _ in range(num_cases):
    song = input().strip()
    finger_count = [0] * NUM_FINGERS
    pressed_fingers = [False] * NUM_FINGERS
    for note in song:
        next_pressed = get_fingers(note)
        for i, (f1, f2) in enumerate(zip(pressed_fingers, next_pressed)):
            if (not f1) and f2:
                finger_count[i] += 1
        pressed_fingers = next_pressed
    print(*finger_count)