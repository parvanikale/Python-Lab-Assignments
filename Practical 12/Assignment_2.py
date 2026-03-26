import pandas as pd

df = pd.read_excel("employee.xlsx")

# Automotive employees
print(df[df['Department']=="Automotive"])

# Search by ID
eid = int(input("Enter ID: "))
print(df[df['EmployeeID']==eid])

# Developers
print(df[df['Designation']=="Developer"])