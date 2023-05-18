#!python

def sum_multiples(num):
    total_sum = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    return total_sum


if __name__ == "__main__":
    print(sum_multiples(10))
    # print(sum_multiples(1000)