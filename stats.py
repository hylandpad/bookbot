import sys
def get_book_text():
    filepath = sys.argv[1]
    with open(filepath) as f:
        file_contents = f.read().lower()
        word_count = len(file_contents.split())
        letter_count = {}
        letters_list = []
        sorted_chars = ''' '''

        for letter in file_contents:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        for key, value  in letter_count.items():
            letters_list.append({"character": key, "count": value})
        
        def sort_on(items):
            return items["count"]

        letters_list.sort(key=sort_on, reverse=True)

        for letter in letters_list:
            if letter["character"].isalpha():
                 sorted_chars += f"{letter["character"]}: {letter["count"]} \r\n"
        


    output = (f'''
    ============ BOOKBOT ============
    Analyzing book found at {filepath}
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------
    {sorted_chars}
    ============= END ===============
    '''
    )

    return (output)