"""
Consider sorting n numbers stored in array A by first finding the smallest element
of A and exchanging it with the element in AŒ1. Then find the second smallest
element of A, and exchange it with AŒ2. Continue in this manner for the first n1
elements of A. Write pseudocode for this algorithm, which is known as selection
sort. What loop invariant does this algorithm maintain? Why does it need to run
for only the first n  1 elements, rather than for all n elements? Give the best-case
and worst-case running times of selection sort in ‚-notation.

"""

def selectionsort(array):
    
    for i in range(len(array)):
        j = len(array) - 1

        while j > i:
            if(array[i] > array[j]):
                array[i], array[j] = array[j], array[i]
            j -= 1
    return array

       


def main():
    a = [32, 4, 41, 0, 7, 11, 5, 3, 2 ,9, 45, 53, 21, 20, 20, 17] #16
    sort_array = selectionsort(a)
    print(sort_array)

if __name__ == '__main__':
    main()