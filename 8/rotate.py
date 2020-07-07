def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    print(string[n:] + string[:n])
    return string[n:] + string[:n]
    pass


if __name__ == '__main__':
    rotate('Penis and vagina', 3)
    rotate('Penis and vagina', -3)
