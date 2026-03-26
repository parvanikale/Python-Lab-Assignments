import matplotlib.pyplot as plt

months = [1,2,3,4,5,6]
profit = [1000,1500,1200,1800,2000,1700]

# Line Plot
plt.plot(months, profit)
plt.title("Monthly Profit")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.show()

# Multiline
facecream = [250,300,280,350,400,380]
facewash = [200,250,230,300,320,310]

plt.plot(months, facecream, label="Facecream")
plt.plot(months, facewash, label="Facewash")
plt.legend()
plt.show()

# Bar Chart
plt.bar(["Facecream","Facewash"], [sum(facecream), sum(facewash)])
plt.show()

# Pie Chart
plt.pie([sum(facecream), sum(facewash)],
        labels=["Facecream","Facewash"],
        autopct='%1.1f%%')
plt.show()