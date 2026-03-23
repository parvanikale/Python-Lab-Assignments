# Input prices from user
prices = tuple(map(int, input("Enter item prices separated by space: ").split()))

# Total items sold
print("Total items sold:", len(prices))

# Cheapest item
print("Cheapest item price:", min(prices))

# Costliest item
max_price = max(prices)
print("Costliest item price:", max_price)

# Ascending order
print("Prices in ascending order:", tuple(sorted(prices)))

# Number of costliest items sold
count_max = prices.count(max_price)
print("Number of costliest items sold:", count_max)