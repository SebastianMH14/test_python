#!python

def compare_lists(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

if __name__ == "__main__":
    print(compare_lists([1, 2, 3, 10, 20, 40, 50, "azul"], [1, 2, 3, 10, 40, 50, "azul", "verde"]))
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    result = compare_lists(list1, list2)
    print(result)