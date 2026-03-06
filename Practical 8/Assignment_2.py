# Program to copy python file without comments

source = input("Enter source python file name: ")
destination = input("Enter destination file name: ")

# Read source file
with open(source, 'r') as f1:
    lines = f1.readlines()

# Write lines without comments
with open(destination, 'w') as f2:
    for line in lines:
        if not line.strip().startswith("#"):
            f2.write(line)

# Print contents of source file
print("\nSource File Content:")
with open(source, 'r') as f1:
    print(f1.read())

# Print contents of destination file
print("\nDestination File Content (without comments):")
with open(destination, 'r') as f2:
    print(f2.read())