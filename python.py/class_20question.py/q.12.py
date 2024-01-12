class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage:
n_value = 50
divisible_by_seven_instance = DivisibleBySeven(n_value)

# Using the generator to iterate numbers divisible by 7
for num in divisible_by_seven_instance.generate_numbers():
    print(num)
