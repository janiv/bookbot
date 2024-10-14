def word_count(book: str)-> int:
    count = len(book.split())
    return count


def char_count(book: str)-> dict:
    lcase = book.lower()
    chars = {}
    for letter in lcase:
        if letter in chars:
            chars[letter] += 1
        else:
            chars[letter] = 1
    keys = list(chars.keys())
    keys.sort()
    sorted_chars = {i: chars[i] for i in keys}
    return sorted_chars


def read_file(file_location:str)->str:
    f = open(file_location)
    return f.read()


def report(file_location:str ):
    book = read_file(file_location)
    word_c = word_count(book)
    char_c = char_count(book)
    letters = "abcdefghijklmnopqrstuvwxyz"
    print(f"--- Begin report of {file_location} ---")
    print(f'{word_c} words found in the document')
    print()
    l_count = {}
    for l in letters:
        count = char_c[l]
        l_count[l] = count
    val_sorted = {k: v for k,v in sorted(l_count.items(), key=lambda item:item[1], reverse=True)}
    for k,v in val_sorted.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")

file= "books/frankenstein.txt"
report(file)

