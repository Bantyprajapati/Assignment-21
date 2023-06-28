# Write a recursive python function to print first N even natural numbers.
def print_even_numbers(n):
    if n > 0:
        print_even_numbers(n-1)
        print(2 * n)

# Test the function
N = 5
print("First", N, "even natural numbers:")
print_even_numbers(N)
