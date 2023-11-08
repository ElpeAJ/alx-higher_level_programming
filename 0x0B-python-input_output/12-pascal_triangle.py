#!/usr/bin/python3


def pascal_triangle(n):
    """
    Parameter
    n : integer
    """
    myList = []
    left = 1
    right = 1

    if n <= 0:
        return myList
    for i in range(n):
        myList.append([1] * (i + 1))

    for row in range(2, n):
        for col in range(1, row):
            left = myList[row - 1][col - 1]
            right = myList[row - 1][col]
            myList[row][col] = left + right

    return (myList)
