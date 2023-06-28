# Write a recursive python function to print first N odd natural numbers
def print_odd_numbers(n):
    if n > 0:
        print_odd_numbers(n-1)
        print((2 * n) - 1)

# Test the function
N = 5
print("First", N, "odd natural numbers:")
print_odd_numbers(N)
