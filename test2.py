def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# 使用例
my_numbers = [1, 2, 3, '4', 5]  # '4'が文字列であるためエラーが発生
result = sum_numbers(my_numbers)
print(f"The total sum is: {result}")