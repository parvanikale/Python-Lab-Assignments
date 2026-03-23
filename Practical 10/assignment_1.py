import pandas as pd

df = pd.read_csv("books.csv")

print("\nComplete Report:")
print(df)

author_name = input("\nEnter author name: ")
print(df[df['author'] == author_name])

publisher_name = input("\nEnter publisher name: ")
print(df[df['publisher'] == publisher_name])

print("\nCheapest Book:")
print(df.loc[df['price'].idxmin()])

print("\nCostliest Book:")
print(df.loc[df['price'].idxmax()])

print("\nSorted by Year:")
print(df.sort_values(by='year'))