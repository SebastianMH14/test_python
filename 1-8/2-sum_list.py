#!python

def sum_even_list(num_list):
    total_sum = 0
    for num in num_list:
        if num % 2 == 0:
            total_sum += num
    return total_sum

if __name__ == "__main__":
    print(sum_even_list([1, 3, 5, 7, 9]))
    print(sum_even_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))