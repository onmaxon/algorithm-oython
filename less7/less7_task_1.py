import random

numbers = [random.randint(-100, 100) for _ in range(10)]


def bubble_sort(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print('Исходный массив:', numbers)
print('Отсортированный:', bubble_sort(numbers))
