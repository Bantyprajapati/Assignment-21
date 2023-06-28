# Write a recursive python function to print cubes of first N natural numbers
def print_cube_numbers(n):
    if n > 0:
        print_cube_numbers(n-1)
        print(n ** 3)

# Test the function
N = 5
print("Cubes of the first", N, "natural numbers:")
print_cube_numbers(N)
