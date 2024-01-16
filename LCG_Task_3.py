def linear_congruential_generator(a, b, c, M, num_values):
    random_values = []
    x = c  # Initial seed
    
    for _ in range(num_values):
        x = (a * x + b) % M
        random_values.append(x)
    
    return random_values

# Example usage
a = 1       # Multiplicative constant
b = 3       # Additive constant
c = 0       # Seed
M = 10       # Modulus
num_values = 12

random_sequence = linear_congruential_generator(a, b, c, M, num_values)
print(f"Random sequence: {random_sequence}")
