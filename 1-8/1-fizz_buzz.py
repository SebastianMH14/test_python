#!python

def fizz_buzz(num):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    return num


if __name__ == "__main__":
    print(fizz_buzz(12))
    print(fizz_buzz(20))
    print(fizz_buzz(45))
    print(fizz_buzz(8))
