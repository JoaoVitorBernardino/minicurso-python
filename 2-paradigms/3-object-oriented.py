class Calculator:
    def __init__(self, list):
        self.list = list
    
    def total_sum(self):
        total = 0

        for num in self.list:
            total += num
        
        return total

numbers = [1, 2, 3, 4, 5]
calculator = Calculator(numbers)
print(calculator.total_sum())