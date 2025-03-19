from stats import get_num_words, get_num_of_characters, char_dict_sort
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_book = sys.argv[1]

num_words = get_num_words(path_to_book)
char_dict = get_num_of_characters(path_to_book)
sorted_char_dict = char_dict_sort(char_dict)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {path_to_book}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for char, count in sorted_char_dict.items():
    print(f"{char}: {count}")



    