def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    out = ''
    for item in input_string:
        if item.isalnum() or item == ' ':
            out += item
    return out

if __name__ == '__main__':
    print(remove_punctuation('Hello, I am Tim.'))
