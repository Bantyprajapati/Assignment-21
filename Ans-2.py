# Write a recursive python function to print first N natural numbers in reverse order.
def print_natural_numbers_reverse(n):
    if n > 0:
        print(n)
        print_natural_numbers_reverse(n-1)

# Test the function
N = 10
print("First", N, "natural numbers in reverse order:")
print_natural_numbers_reverse(N)
