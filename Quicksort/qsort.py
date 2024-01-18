from typing import List


def qsort(elements: List, left: int, right: int):
    if(right>left):
        pos = divide(elements, left, right)
        qsort(elements, left, pos-1)
        qsort(elements, pos+1, right)

def divide(elements: List, left: int, right: int):
    p = elements[right]
    i = left
    j = right-1

    #pseudocode stand größer müsste aber kleiner sein?
    #pseudocode anpassen
    while(True):
        while(elements[i] <= p and i<right):
            i = i+1
        
        while(elements[j] >= p and j>left):
            j = j-1

        if i<j:
            swap(elements, i, j)

        if (i>=j):
            break
    swap(elements, i, right)
    return i

def swap(elements: List, i: int, j: int):
    tmp = elements[i]
    elements[i] = elements[j]
    elements[j] = tmp

def main():
    test = [88, 56, 100, 2, 25, 20, 19]
    qsort(test, 0, len(test)-1)
    print(test)

if __name__ == "__main__":
    main()