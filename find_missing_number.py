def find_num(arr):
    #[9, 3, 7, 5, 6, 4, 2, 1] n = 9
    n = len(arr) + 1
    sum_n = n * (n+1) // 2
    i = 0
    
    while i < len(arr):
        sum_n = sum_n - arr[i]
        i += 1

    return sum_n

def main():
    arr = find_num([9, 3, 8, 5, 6, 4, 2, 1])
    print(arr)


if __name__ == '__main__':
    main()