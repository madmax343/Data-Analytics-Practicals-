import pandas as pd

df = pd.DataFrame({
    "Customer Name": ["Jaydip", "Rupesh", "Ritesh", "Deep"],
    "Mobile Model": ["Samsung A15", "Redmi Note 13", "Realme 12", "Vivo Y28"],
    "Mobile Price": [15000, 18000, 16000, 14000]
})

print("Original Data:\n", df)

# Data Subsetting
print("\nSubset (Mobile Price > 15000):\n",
      df[df["Mobile Price"] > 15000])

# Sorting in Ascending Order
print("\nSorted by Mobile Price (Ascending):\n",
      df.sort_values("Mobile Price"))

# Sorting in Descending Order
print("\nSorted by Mobile Price (Descending):\n",
      df.sort_values("Mobile Price", ascending=False))

# Grouping
print("\nGrouped (Average Mobile Price by Mobile Model):\n",
      df.groupby("Mobile Model")["Mobile Price"].mean())

# Statistical Operations
print("\nMean =", df["Mobile Price"].mean())
print("Median =", df["Mobile Price"].median())
print("Mode =")
print(df["Mobile Price"].mode())