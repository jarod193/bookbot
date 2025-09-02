def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    to_lower = text.lower()
    book_count = {}
    for char in to_lower:
            book_count[char] = book_count.get(char, 0) + 1
    return book_count

def sorted_list(character_dictionary):
    result = []
    for character, count in character_dictionary.items():
        result.append({"char": character, "num": count})
    def sort_on(item):
        return item["num"]
    result.sort(reverse=True, key=sort_on)
    return result