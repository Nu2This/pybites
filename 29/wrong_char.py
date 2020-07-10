
alphanumeric = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def get_index_different_char(chars):
    an = 0
    nan = 0

    for i, char in enumerate(chars):
        print(i, char)
        if str(char).isalnum():
            an +=1
            print(an)
        else:
            nan +=1
            print(nan)
    if an > nan:
        for i, char in enumerate(chars):
            if not str(char).isalnum():
                print(i)
                return i
    else:
        for i, char in enumerate(chars):
            if str(char).isalnum():
                print(i)
                return i

   # for item in chars:
   #     if str(item).isalnum():
   #         an += 1
   #     else:
   #         nan +=1
   # index = 0

   # if an < nan:
   #     for item in chars:
   #         if str(item).isalnum():
   #             index += 1
   #         print(index)
   # if an > nan:
   #     for item in chars:
   #         if str(item).isalnum():


if __name__ == '__main__':
    inputs = (
        ['A', 'f', '.', 'Q', 2],
        ['.', '{', ' ^', '%', 'a'],
        [1, '=', 3, 4, 5, 'A', 'b', 'a', 'b', 'c'],
        ['=', '=', '', '/', '/', 9, ':', ';', '?', '¡'],
        list(range(1,9)) + ['}'] + list('abcde'),  # noqa E230
        [2, '.', ',', '!']
    )
    get_index_different_char(inputs[1])
