
# measurements in point units
HORIZ_SPACE = 10
def calc_font(word_count: int, max_count: int):
    return 8 -(-40*(word_count - 4) // (max_count - 4)) # ceil
def calc_width(word: int, font_size: int):
    num_letters = len(word)
    return -(-(9 * num_letters * font_size) // 16) # ceil

i_cloud = 1
while True:
    max_width, num_words = [int(x) for x in input().split()]
    if num_words == 0:
        break
    words = []
    word_counts = []
    for _ in range(num_words):        
        word, word_count = input().split()
        words.append(word)
        word_counts.append(int(word_count))
    max_count = max(word_counts)

    cloud_height = 0
    curr_line_height = 0
    curr_line_width = 0
    for i, (word, word_count) in enumerate(zip(words, word_counts)):
        font_size = calc_font(word_count, max_count)
        width = calc_width(word, font_size)
        if i == 0:
            curr_line_height = font_size
            curr_line_width = width
            continue
        if curr_line_width + HORIZ_SPACE + width <= max_width:
            curr_line_width += HORIZ_SPACE + width
            if curr_line_height < font_size:
                curr_line_height = font_size
        else: # new line
            cloud_height += curr_line_height
            curr_line_height = font_size
            curr_line_width = width
        if i == num_words-1:
            cloud_height += curr_line_height
    print(f"CLOUD {i_cloud}: {cloud_height}")
    i_cloud += 1
