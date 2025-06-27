from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    output_text = ""
    with open(filepath) as f:
        output_text = f.read()
    return output_text


def print_report():
    filepath = sys.argv[1]
    num_of_words = count_words(get_book_text(filepath))
    characters = sort_characters(count_characters(get_book_text(filepath)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for char in characters:
        c = char["char"]
        num = char["num"]
        if c.isalpha():
            print(f"{c}: {num}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print_report()

main()

