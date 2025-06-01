def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def count_book_char(book_text):
    char_count = {}
    for char in book_text.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_results(results_dict):
    def sort_on(dict):
        return dict['val']
    char_lst = []
    for k,v in results_dict.items():
        if k.isalpha():
            char_lst.append({'key' : k,  'val' : v})

    char_lst.sort(reverse=True, key=sort_on)

    return char_lst
