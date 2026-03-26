import pandas as pd

df = pd.read_csv("books.csv")

print("\nComplete Report:")
print(df)

# Author books
author = input("Enter author: ")
print(df[df['author'] == author])

# Publisher books
pub = input("Enter publisher: ")
print(df[df['publisher'] == pub])

# Cheapest & costliest
print("Cheapest Book:")
print(df.loc[df['price'].idxmin()])

print("Costliest Book:")
print(df.loc[df['price'].idxmax()])

# Sort by year
print("Sorted by Year:")
print(df.sort_values('year'))