# Write a recursive python function to print a number in reverse order.
def print_number_reverse(n):
    if n > 0:
        print(n % 10, end="")
        print_number_reverse(n // 10)

# Test the function
number = 12345
print("Number in reverse order:")
print_number_reverse(number)
