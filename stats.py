def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read().lower()

def get_num_words():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document")

def get_num_of_characters():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    char_dict = {}
    for char in book_text:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict
    
    