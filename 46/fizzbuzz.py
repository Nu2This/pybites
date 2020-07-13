def fizzbuzz(num):
        if num % 3 == 0 and num % 5 ==0:
            return str('Fizz Buzz')
        if num % 3 == 0:
            print('Fizz')
            return str('Fizz')
        if num % 5 == 0:
            print('Buzz')
            return str('Buzz')
        else:
            print(num)
            return int(num)

if __name__ == '__main__':
    fizzbuzz(20)
