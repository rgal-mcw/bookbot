def get_num_words(filepath):
    with open(filepath) as f:
        book = f.read()
        book_string = book.split()
        book_len = len(book_string)
        return f"{book_len}"

def counting_chars(filepath):
    book_dict = {}
    with open(filepath) as f:
        book = f.read()
        book_lower = list(book.lower())
        unique_char = set(book_lower)
        
        for i in unique_char:
            book_dict[i] = book_lower.count(i)

        return book_dict
        

def sort_on(items):
    return items["num"]


def report_chars(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")

    num_words = get_num_words(filepath)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    
    book_dict = counting_chars(filepath) 

    letters = list()
    for letter in book_dict:
        baby_dict = {"letter":letter, "num":book_dict[letter]}
        letters.append(baby_dict)
    letters.sort(reverse=True, key=sort_on)

    for i in letters:
        if i["letter"].isalpha() == True:
            print(f"{i["letter"]}: {i["num"]}")
