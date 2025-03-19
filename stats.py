def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

def get_num_words():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = len(book_text.split())
    print(f"{num_words} words found in the document")