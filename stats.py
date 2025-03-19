def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read().lower()

def get_num_words(path_to_book):
    book_text = get_book_text(path_to_book)
    num_words = len(book_text.split())
    return num_words

def get_num_of_characters(path_to_book):
    book_text = get_book_text(path_to_book)
    char_dict = {}
    for char in book_text:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def char_dict_sort(char_dict):
    sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_char_dict
    
    