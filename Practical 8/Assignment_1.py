source_file = input("Enter source file name: ")
destination_file = input("Enter destination file name: ")

with open(source_file, 'r') as f1:
    data = f1.read()

data_upper = data.upper()

with open(destination_file, 'w') as f2:
    f2.write(data_upper)

print("Content copied in uppercase successfully.")