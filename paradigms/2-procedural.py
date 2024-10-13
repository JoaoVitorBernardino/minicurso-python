def total_sum(list):
    total = 0
    
    for num in list:
        total += num

    return total

numbers = [1, 2, 3, 4, 5]
print(total_sum(numbers))