class Employee:
    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    def manager_info(self):
        print("\nManager Details")
        self.display()


managers = []

for i in range(10):
    print("\nEnter details for Manager", i + 1)
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n--- Managers Information ---")

for m in managers:
    m.manager_info()