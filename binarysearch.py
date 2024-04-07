# Binary search using the iterative method 

def binarysearch(array, key_element):
    """ 
    Array = [10, 23, 4, 6, 9, 11, 3, 7, 5, 2, 8]
             1                6               11
    """
    array.sort()
    high = len(array) #15
    low = 1
   

    while(low <= high):
        middle = int((low + high) / 2) #8 [7]
        if(key_element == array[middle - 1]):
            indice = middle - 1
            return f'The element {key_element} has been found on indice {indice}'
        if(key_element < array[middle - 1]):
            high = middle - 1
        else:
            low = middle + 1
    return False

# Binary search using the recursive method
def recursivebinarysearch(array, low, high, key_element):
    
    array.sort()
    if(low == high):
        """ Mean If there is a single element there its considered as a small problem, so We solve 
        it """
        if(array[low] == key_element):
            return f'The element {key_element} has been found'
        else:
            return 'Not found'
    else:
        middle = int((low + high) / 2)
        if(key_element == array[middle]):
             return f'The element {key_element} has been found'
        if(key_element < array[middle]):
            return recursivebinarysearch(array, low, middle-1, key_element)
        else:
            return recursivebinarysearch(array, middle+1, high, key_element)

def main():
    array = [10, 23, 4, 6, 9, 11, 3, 7, 5, 2, 8, 45, 21, 0, 12, 27]
    bsearch = binarysearch(array, 45)
    rbsearch = recursivebinarysearch(array, 0, len(array)-1, 112)
    print(rbsearch)

if __name__ == '__main__':
    main()