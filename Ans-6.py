# Write a recursive python function to print first N even natural numbers in reverse order.
def print_even_numbers_reverse(n):
    if n > 0:
        print(2 * n)
        print_even_numbers_reverse(n-1)

# Test the function
N = 5
print("First", N, "even natural numbers in reverse order:")
print_even_numbers_reverse(N)
