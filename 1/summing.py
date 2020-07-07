def sum_numbers(numbers=None):
    if numbers==None:
        print(sum(range(1, 101)))
        return sum(range(1, 101))
    else:
        add = 0
        for n in numbers:
            add += n

        return add
    pass

if __name__ == '__main__':
    sum_numbers()
