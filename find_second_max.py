def find_second_max(arr):
    # input [13, 34, 2, 34, 33, 1]
    # ouput 33
    """
    Implementar El valor MInimo Posible para cada variable como inicio
    """
    max_int = -2147483648
    second_max = -2147483648

    for n in range(len(arr)):
        if arr[n] > max_int:
            second_max = max_int
            max_int = arr[n]
        elif arr[n] > second_max and arr[n] != max_int:
            second_max = arr[n]

    return second_max

def find_second_min(arr):
    # input [13, 34, 2, 34, 33, 1]
    # ouput 33
    min_int = 2147483648
    second_min = 2147483648

    for i in range(len(arr)):
        if arr[i] < min_int:
            second_min = min_int
            min_int = arr[i]

    return second_min


def main():
    arr_max = find_second_max([13, 34, 2, 34, 33, 1])
    arr_min = find_second_min([13, 34, 2, 34, 33, 2, 1])

    print(arr_min)
    print(arr_max)


if __name__ == '__main__':
    main()