import matplotlib.pyplot as plt

companies = ["Microsoft","Google","Amazon","IBM","Infosys"]
recruitments = [120,150,180,90,200]

# Bar chart
plt.bar(companies, recruitments)
plt.title("Recruitment Data")
plt.show()

# Pie chart
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.show()

# Doughnut chart
plt.pie(recruitments, labels=companies)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.show()

# Comparison
plt.bar(["IBM","Infosys"], [90,200])
plt.show()