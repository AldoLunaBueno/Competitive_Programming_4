num_words = int(input())
keywords = set()
for kw in range(num_words):
    kw = input().casefold().replace("-", " ")
    keywords.add(kw)
print(len(keywords))