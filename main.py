import sys
from stats import get_number_words
from stats import get_number_chars
from stats import get_sorted_list_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_to_analyze = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at", book_to_analyze)
    print("----------- Word Count ----------")
    print("Found", get_number_words(get_book_text(book_to_analyze)), "total words")
    print("--------- Character Count -------")
    all_chars = get_sorted_list_dict(get_number_chars(get_book_text(book_to_analyze)))
    for c in all_chars:
        if c["char"].isalpha():
            print(c["char"] + ":", c["num"])
    print("============= END ===============")


main()
