from collections import Counter

# put your file name here:
FILENAME = r"C:\Users\Vansh\Downloads\book.txt"
# read the file
with open(FILENAME, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

# count emojis / symbols (ignores spaces and newlines)
tokens = [ch for ch in text if not ch.isspace()]
freqs = Counter(tokens)

# show results sorted by most common
for emoji, count in freqs.most_common():
    print(emoji, ":", count)
