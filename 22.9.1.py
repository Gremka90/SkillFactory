def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        return middle
    elif element < array[middle]:

        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

array= list(map(int, input('Введите массив чисел через пробел: ').split()))
number = int(input('Введите число: '))

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)
left = int(array[0])
right = int(array[-1])
if number < left or number > right:
    print('Число отсутствует')
else:
    print(binary_search(array,number, 0, len(array)-1))