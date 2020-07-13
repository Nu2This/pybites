def fizzbuzz(num, ret):
    for x in range(num):
        if x % ret == 0:
            return 'Fizz'
        if x % ret == 0:
            return 'Buzz'
        else:
            return x

if __name__ == '__main__':
    fizzbuzz(20)
