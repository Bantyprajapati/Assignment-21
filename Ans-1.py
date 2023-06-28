# Write a recursive python function to print first N natural numbers.
def print_natural_numbers(n):
    if n > 0:
        print_natural_numbers(n-1)
        print(n)

# Test the function
N = 10
print("First", N, "natural numbers:")
print_natural_numbers(N)
