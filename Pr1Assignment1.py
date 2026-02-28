# Employee Salary Program

# Taking input
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

# Calculations
da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

gross_salary = basic + da + hra + ta
net_salary = gross_salary - lic

# Output
print("\n--- Employee Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", dept)

print("\n--- Salary Details ---")
print("Basic Salary:", basic)
print("DA:", da)
print("HRA:", hra)
print("TA:", ta)
print("LIC Deduction:", lic)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)