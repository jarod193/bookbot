import sys
from stats import count_words
from stats import count_characters
from stats import sorted_list

def get_book_text(path):
    with open(path) as f:
        return f.read()




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    book_text = get_book_text(path)

    print("----------- Word Count ----------")
    print(f"Found {count_words(book_text)} total words")

    print("--------- Character Count -------")
    sorted_items = sorted_list(count_characters(book_text))
    for item in sorted_items:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()