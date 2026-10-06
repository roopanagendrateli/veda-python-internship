# Veda Technology - Python Programming Internship
# Task 6: Generate a Multiplication Table

print("========================================")
print("       MULTIPLICATION TABLE")
print("========================================")

# Get the number from the user
number = int(input("Enter the number: "))

# Get the multiplication limit from the user
limit = int(input("Enter the multiplication limit: "))

print()
print(f"Multiplication Table of {number}")
print("----------------------------------------")

# Generate the multiplication table
for i in range(1, limit + 1):
    result = number * i
    print(f"{number} x {i} = {result}")

print("----------------------------------------")
print("Table generated successfully!")