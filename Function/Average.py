def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

nums = [10, 20, 30, 40, 50]
result = calculate_average(nums)
print("Average:", result)
