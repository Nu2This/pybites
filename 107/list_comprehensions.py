numbers = [-1, -2, -.5, 0, 1, 2, .5 , .4]

def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    rlist = [number for number in numbers if number % 2 == 0 and number > 0]
    print(rlist)

    return(rlist)
    pass

if __name__ == '__main__':
    filter_positive_even_numbers(numbers)
