# Vendor Details & Annual Purchase Report

# Vendor details input
name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

# Monthly purchases
monthly = []

print("\nEnter purchase for 12 months:")
for i in range(12):
    amt = float(input(f"Month {i+1}: "))
    monthly.append(amt)

# Annual calculation
annual_total = sum(monthly)

# Output
print("\n--- Vendor Details ---")
print("Name:", name)
print("Year of Association:", year)
print("Contact:", contact)
print("Email:", email)

print("\n--- Purchase Report ---")
print("Monthly Purchases:", monthly)
print("Annual Purchase Total:", annual_total)