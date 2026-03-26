import pandas as pd

data = {
 'cut':['Ideal','Premium','Good','Premium','Good'],
 'price':[326,326,327,334,335],
 'x':[3.95,3.89,4.05,4.20,4.34],
 'y':[3.98,3.84,4.07,4.23,4.35],
 'z':[2.43,2.31,2.31,2.63,2.75]
}

df = pd.DataFrame(data)

# Mean price
print(df.groupby('cut')['price'].mean())

# Count, min, max
print(df.groupby('cut')['price'].agg(['count','min','max']))

# Average x,y,z
print(df[['x','y','z']].mean())