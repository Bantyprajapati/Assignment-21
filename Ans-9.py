# Write a recursive python function to print first N multiples of a given number.
def print_multiples_of_number(number, n):
    if n > 0:
        print_multiples_of_number(number, n-1)
        print(number * n)

# Test the function
N = 5
given_number = 3
print("First", N, "multiples of", given_number, ":")
print_multiples_of_number(given_number, N)
