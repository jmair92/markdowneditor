def print_book_info(title, author=None, year=None):
    if author is not None and year is not None:
        print('"' + title + '" was written by', author, 'in', year)
    elif author is not None and year is None:
        print('"' + title + '" was written by', author)
    elif author is None and year is not None:
        print('"' + title + '" was written in', year)
    else:
        print('"' + title + '"')

