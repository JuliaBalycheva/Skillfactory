def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return -1  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину

    if array[middle] < element and array[middle+1] >= element:  # если элемент в середине,
        return middle  # возвращаем этот индекс


    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers_str = input('введите числа через пробел: ')
number_str = input('введите любое число: ')

numbers = list(map(int, numbers_str.split()))
number = int(number_str)

bubbleSort(numbers)
result = binary_search(numbers, number, 0, len(numbers)-1)

if(result == -1):
    print('элемент не найден')
else:
    print('номер позиции элемента % d' % result)




