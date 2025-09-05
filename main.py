from stats import get_report, count_characters, num_of_words
import sys

if(len(sys.argv) != 2):
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)


def main():
    result = get_book_text(sys.argv[1])
    num_words = num_of_words(result)

    print(f"Found {num_words} total words")
    
    count_words = count_characters(result)
    
    report = get_report(count_words)

    for item in report:
        if(item['char'].isalpha()):
            print(f'{item["char"]}: {item["num"]}')


def get_book_text(file_path):
    with open(file_path) as f:  
        return f.read()

main()