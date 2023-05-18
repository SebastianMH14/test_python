#!python

def selection_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers


if __name__ == "__main__":
    print(selection_sort([1, 3, 2, 4, 5, 7, 6, 8, 9, 10]))
    print(selection_sort([17, 4, 12, 6, 1, 20, 10, 19, 13, 7, 15, 3, 9, 2, 16, 11, 5, 14, 8, 18]
                         ))
