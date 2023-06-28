# Write a recursive python function to print squares of first N natural numbers
def print_square_numbers(n):
    if n > 0:
        print_square_numbers(n-1)
        print(n ** 2)

# Test the function
N = 5
print("Squares of the first", N, "natural numbers:")
print_square_numbers(N)
