from collections import Counter

def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = [word for word in re.findall(r'\b\w+\b', text) if len(word) >= 4]

    four_letter_words = [word[:4] for word in words]

    most_common_words = Counter(four_letter_words).most_common(5)

    return most_common_words

if __name__ == "__main__":
    filename = 'input.txt' 
    print(count_words(filename))