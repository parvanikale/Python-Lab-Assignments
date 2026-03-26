import pandas as pd

data = {
    'State': ['Maharashtra','Gujarat','Karnataka','Tamil Nadu','Rajasthan'],
    'Area': [307713,196244,191791,130058,342239],
    'Population': [112374333,60439692,61095297,72147030,68548437]
}

df = pd.DataFrame(data)

print("\nComplete Data:")
print(df)

# Largest area
print("Largest Area State:")
print(df.loc[df['Area'].idxmax()]['State'])

# Largest population
print("Largest Population State:")
print(df.loc[df['Population'].idxmax()]['State'])

# Density
df['Density'] = df['Population'] / df['Area']

print("\nDensity:")
print(df[['State','Density']])

# Highest density
print("Highest Density State:")
print(df.loc[df['Density'].idxmax()]['State'])