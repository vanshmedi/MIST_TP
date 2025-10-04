mapping = {
    "😍": "E",
    "🤡": "T",
    "😙": "A",
    "🥶": "O",
    "👂": "I",
    "🥴": "N",
    "🥺": "S",
    "😢": "H",
    "😉": "R",
    "🙀": "D",
    "🥳": "L",
    "👧": "C",
    "😡": "U",
    "😎": "M",
    "🤩": "F",
    "😃": "W",
    "🙄": "G",
    "🤐": "P",
    "😵": "Y",
    "🤪": "B",
}

# Change to your actual file path
FILENAME = r"C:\Users\Vansh\Downloads\book.txt"

with open(FILENAME, "r", encoding="utf-8", errors="ignore") as f:
    text = f.read()

decoded = ""
for ch in text:
    if ch in mapping:
        decoded += mapping[ch]
    else:
        decoded += ch  # keep punctuation etc

print(decoded[:2000])  # print first 2000 chars to preview
