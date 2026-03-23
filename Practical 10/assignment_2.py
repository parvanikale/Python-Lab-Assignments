import pandas as pd

# Create DataFrame
data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Kerala', 'Punjab'],
    'Area': [307713, 196244, 342239, 38863, 50362],   # in sq km
    'Population': [112374333, 60439692, 68548437, 33406061, 27743338]
}

df = pd.DataFrame(data)

# a) Complete information
print("\nState Information:")
print(df)

# b) State with largest Area
print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax()])

# c) State with largest Population
print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax()])

# d) Calculate population density
df['Density'] = df['Population'] / df['Area']

print("\nWith Population Density:")
print(df)

# e) State with highest density
print("\nState with Highest Population Density:")
print(df.loc[df['Density'].idxmax()])