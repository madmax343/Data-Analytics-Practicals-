
import pandas as pd

# Take number of students
n = int(input("Enter number of students: "))

names = []
ages = []
departments = []
dates = []

# Take input from user
for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    date = input("Enter Admission Date (DD-MM-YYYY): ")

    names.append(name)
    ages.append(age)
    departments.append(department)
    dates.append(date)

# Create DataFrame
data = {
    "Name": names,
    "Age": ages,
    "Department": departments,
    "Admission_Date": dates
}

df = pd.DataFrame(data)

print("\nOriginal Data:")
print(df)

print("\nOriginal Data Types:")
print(df.dtypes)

# 1. DATA TYPE CONVERSION
df["Age"] = df["Age"].astype(int)

# 2. STRING MANIPULATION
# Remove extra spaces from Name
df["Name"] = df["Name"].str.strip()

# Convert Name into Title Case
df["Name"] = df["Name"].str.title()

# Convert Department into Title Case
df["Department"] = df["Department"].str.title()

# 3. DATE TYPE TRANSFORMATION
df["Admission_Date"] = pd.to_datetime(
    df["Admission_Date"],
    format="%d-%m-%Y"
)

# Extract year, month, and day
df["Year"] = df["Admission_Date"].dt.year
df["Month"] = df["Admission_Date"].dt.month
df["Day"] = df["Admission_Date"].dt.day

# DISPLAY TRANSFORMED DATA
print("\nTransformed Data:")
print(df)

print("\nTransformed Data Types:")
print(df.dtypes)
