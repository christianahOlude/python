def get_sum(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

lst = [1,7,8,9]
print(get_sum(lst))