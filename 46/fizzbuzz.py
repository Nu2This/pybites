def fizzbuzz(num):
    for x in range(num):
        if x % 3 == 0:
            return 'Fizz'
        if x % 5 == 0:
            return 'Buzz'
        else:
            return x

if __name__ == '__main__':
    fizzbuzz(20)
