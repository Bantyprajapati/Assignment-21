# Write a recursive python function to print first N odd natural numbers in reverse order
def print_odd_numbers_reverse(n):
    if n > 0:
        print((2 * n) - 1)
        print_odd_numbers_reverse(n-1)

# Test the function
N = 5
print("First", N, "odd natural numbers in reverse order:")
print_odd_numbers_reverse(N)
