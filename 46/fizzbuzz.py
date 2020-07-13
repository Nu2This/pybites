def fizzbuzz(num):
    for x in range(num + 1):
        print(x)
        if x % 3 == 0:
            print('Fizz')
        if x % 5 == 0:
            print('Buzz')
        else:
            print(x)

if __name__ == '__main__':
    fizzbuzz(20)
