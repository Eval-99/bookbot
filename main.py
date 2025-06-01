import sys
from stats import get_book_text, count_book_char, sort_results

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    text = get_book_text(sys.argv[1])

    # Word count
    word_count = 0
    for _ in text.split():
        word_count += 1

    # Dict with all characters in book
    char_dict = count_book_char(text)
    # Sorted list of dicts with all characters
    char_sorted = sort_results(char_dict)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {word_count} total words')
    print('--------- Character Count -------')
    for char in char_sorted:
        print(f'{char['key']}: {char['val']}')
    print('============= END ===============')

main()
