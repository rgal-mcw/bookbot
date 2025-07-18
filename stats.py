def get_num_words(filepath):
    with open(filepath) as f:
        book = f.read()
        book_string = book.split()
        book_len = len(book_string)
        return f"{book_len} words found in the document"

def counting_chars(filepath):
    book_dict = {}
    with open(filepath) as f:
        book = f.read()
        book_lower = list(book.lower())
        unique_char = set(book_lower)

        print(unique_char)

        for i in unique_char:
            book_dict[i] = book_lower.count(i)

        return book_dict
        


